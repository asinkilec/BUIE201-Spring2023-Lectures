class City:
    def __init__(self, name, type=None, language=None):
        self.name = name
        self.type = type
        self.language = language
        self.schools = []
        
    def __repr__(self):
        if self.type is None and self.language is None:
            return f"({self.name})"
        elif self.language is None:
            return f"({self.name}, {self.type})"
        else:
            return f"({self.name}, {self.type}, {self.language})"
    
    def add_school(self, school):
        self.schools.append(school)

class School:
    def __init__(self, name):
        self.name = name
        
    def __repr__(self):
        return self.name

class University(School):
    pass

class HighSchool(School):
    def __init__(self, name, language):
        super().__init__(name)
        self.language = language
        
    def __repr__(self):
        return f"{self.name}, {self.language}"

class Map:
    def __init__(self):
        self.cities = {}
        
    def add_city(self, city):
        self.cities[city.name] = city
        
    def __repr__(self):
        city_strs = []
        for city in sorted(self.cities.values(), key=lambda c: c.name):
            city_str = f"{city.name} => "
            connections = []
            for conn in sorted(self.cities.values(), key=lambda c: c.name):
                if conn == city:
                    continue
                if conn.type is not None:
                    if conn.language is not None:
                        conn_str = f"({conn.name}, {conn.type}, {conn.language})"
                    else:
                        conn_str = f"({conn.name}, {conn.type})"
                else:
                    conn_str = f"({conn.name})"
                connections.append(conn_str)
            if city.schools:
                schools_str = ", ".join([str(school) for school in city.schools])
                city_str += f", {schools_str}"
            city_str += ", ".join(connections)
            city_strs.append(city_str)
        return "; ".join(city_strs)

def Run():
    m = Map()
    C1 = City("Istanbul")
    C2 = City("Konya")

    C1.add_school(University("BU"))
    C2.add_school(University("Selcuk"))
    C1.add_school(University("ITU"))
    C1.add_school(HighSchool("DSI", "German"))
    C1.add_school(HighSchool("GS", "French"))
    C2.add_school(HighSchool("KAL", "English"))

    m.add_city(C1)
    m.add_city(C2)

    return str(m)

Run()