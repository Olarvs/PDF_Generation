sample_data = [
    {
        "name": f"Employee {i}",
        "email": f"employee{i}@samplecompany.com",
        "department": f"Department {i % 5 + 1}",
        "position": f"Position {i % 10 + 1}"
    }
    for i in range(1, 101)
]
