# 深層思考
1. 把Project分成三部份： 
    第一部份：
    1.  用SQLModel建立一個父系Class及三個子系Class，並建立SQL Database名叫ikea_furniture.db，包含以下資料:

    # IKEA傢俬基本Class
    -   Product ID (str) # Primary Key (Link to 子系Class的Product ID做成Index, [不可重覆])
    -   Category  (str) # (Linking to 子系Class的Catrgory，用以分類傢俬)
    -   Brand (str)
    -   Name (str)
    -   Color (str)
    -   Style (str)
    -   Materials (str)
    -   Length (float)
    -   Width (float)
    -   Height (float)
    -   Weight (float)
    -   Serial No. (int)
    -   Country of Origin (str)
    -   Price (float)
    -   Warranty (int)
    -   Assembly Require (bool)
    -   Have Stock (bool)
    -   QC (bool)

    2.  建立三套子系，父系Class有的資料子系Class不需要有，只列表父系Class沒有而子系Class有的特殊Feilds
        #   Category = Wardrobes(書櫃)
            -   Product ID (str) # Primary Key (Link to 父系Class的Product ID做成Index，[不可重覆])
            -   Category  (str) # (相等於父系Class的Category，分類為Wardrobes)
            -   Depth_Length (float)
            -   Hanging (bool)
            -   Structure (str)
            -   Function Features (str)
            -   Installation (str)
            -   Load Capacity (str)
            -   Advanced Technologies (str)

        #   Category = Desk(書枱)
            -   Product ID (str) # Primary Key (Link to 父系Class的Product ID做成Index，[不可重覆])
            -   Category  (str) # (相等於父系Class的Category，分類為Desk)
            -   Design Features (str)
            -   Ergonomics (str)
            -   Additional Options (str)

        #   Category = TV_Cabinet(電視櫃)
            -   Product ID (str) # Primary Key (Link to 父系Class的Product ID做成Index，[不可重覆])
            -   Category  (str) # (相等於父系Class的Category，分類TV_Cabinet)
            -   Design Features (str)
            -   Compatibility (str)
            -   Additional Features (str)

2.  第二部份：
    導入以下資料到ikea_furniture.db中
    # Brainstorming: 將此部份分支一個Python，以方便將來作Data Entry

    ikea_wardrobes = [
    IkeaWardrobe(
        name="PAX",
        brand="IKEA",
        product_id="W001",
        color="White",
        style="Modern",
        materials="Particleboard",
        length=200.0,
        width=60.0,
        height=236.0,
        weight=45.5,
        serial_no=1001,
        country_of_origin="Sweden",
        price=299.99,
        warranty=10,
        have_stock=True,
        qc=True,
        depth_length=58.0,
        hanging=True,
        structure="Modular",
        function_features="Adjustable Shelves",
        installation="Wall-mounted",
        load_capacity="50 kg",
        advanced_technologies=["Soft-closing hinges"]
    ),
    IkeaWardrobe(
        name="BRIMNES",
        brand="IKEA",
        product_id="W002",
        color="Black-Brown",
        style="Contemporary",
        materials="Fiberboard",
        length=180.0,
        width=55.0,
        height=220.0,
        weight=30.0,
        serial_no=1002,
        country_of_origin="China",
        price=199.50,
        warranty=10,
        have_stock=True,
        qc=True,
        depth_length=50.0,
        hanging=True,
        structure="Freestanding",
        function_features="Mirrored Doors",
        installation="Free-standing",
        load_capacity="40 kg",
        advanced_technologies=[]
    ),
    IkeaWardrobe(
        name="PLATSA",
        brand="IKEA",
        product_id="W003",
        color="Oak Veneer",
        style="Scandinavian",
        materials="Wood",
        length=150.0,
        width=55.0,
        height=200.0,
        weight=25.0,
        serial_no=1003,
        country_of_origin="Poland",
        price=149.99,
        warranty=5,
        have_stock=True,
        qc=True,
        depth_length=53.0,
        hanging=False,
        structure="Modular",
        function_features="Drawers Included",
        installation="Wall-mounted",
        load_capacity="30 kg",
        advanced_technologies=[]
    ),
    IkeaWardrobe(
        name="KLEPPSTAD",
        brand="IKEA",
        product_id="W004",
        color="Gray",
        style="Minimalist",
        materials="Metal/Glass",
        length=160.0,
        width=50.0,
        height=210.0,
        weight=20.5,
        serial_no=1004,
        country_of_origin="Germany",
        price=89.99,
        warranty=10,
        have_stock=True,
        qc=True,
        depth_length=48.0,
        hanging=True,
        structure="Frame with doors",
        function_features="Glass Doors",
        installation="Free-standing",
        load_capacity="25 kg",
        advanced_technologies=[]
    ),
    IkeaWardrobe(
        name="ALGOT",
        brand="IKEA",
        product_id="W005",
        color="Stainless Steel",
        style="Industrial",
        materials="Metal",
        length=140.0,
        width=45.0,
        height=190.0,
        weight=15.0,
        serial_no=1005,
        country_of_origin="USA",
        price=79.99,
        warranty=5,
        have_stock=True,
        qc=True,
        depth_length=40.0,
        hanging=True,
        structure="Wall system",
        function_features="Customizable Uprights",
        installation="Wall-mounted",
        load_capacity="20 kg",
        advanced_technologies=[]
    ),
    IkeaWardrobe(
        name="HEMNES",
        brand="IKEA",
        product_id="W006",
        color="Red",
        style="Traditional",
        materials="Solid Pine",
        length=170.0,
        width=60.0,
        height=215.0,
        weight=40.0,
        serial_no=1006,
        country_of_origin="Vietnam",
        price=249.99,
        warranty=10,
        have_stock=True,
        qc=True,
        depth_length=55.0,
        hanging=True,
        structure="Freestanding",
        function_features="Shoe Storage",
        installation="Free-standing",
        load_capacity="45 kg",
        advanced_technologies=[]
    ),
    IkeaWardrobe(
        name="NORDLI",
        brand="IKEA",
        product_id="W007",
        color="Dark Blue",
        style="Mid-Century",
        materials="Wood/Metal",
        length=190.0,
        width=65.0,
        height=240.0,
        weight=55.0,
        serial_no=1007,
        country_of_origin="Sweden",
        price=349.99,
        warranty=10,
        have_stock=True,
        qc=True,
        depth_length=60.0,
        hanging=True,
        structure="Modular",
        function_features="LED Lighting",
        installation="Wall-mounted",
        load_capacity="60 kg",
        advanced_technologies=["Motion Sensor Lights"]
    ),
    IkeaWardrobe(
        name="BOAXEL",
        brand="IKEA",
        product_id="W008",
        color="Green",
        style="Rustic",
        materials="Bamboo",
        length=130.0,
        width=40.0,
        height=180.0,
        weight=10.0,
        serial_no=1008,
        country_of_origin="Indonesia",
        price=69.99,
        warranty=5,
        have_stock=True,
        qc=True,
        depth_length=35.0,
        hanging=False,
        structure="Freestanding",
        function_features="Foldable Design",
        installation="Free-standing",
        load_capacity="15 kg",
        advanced_technologies=[]
    ),
    IkeaWardrobe(
        name="TYSsedal",
        brand="IKEA",
        product_id="W009",
        color="Beige",
        style="Classic",
        materials="Plywood",
        length=165.0,
        width=58.0,
        height=205.0,
        weight=28.0,
        serial_no=1009,
        country_of_origin="Malaysia",
        price=129.99,
        warranty=10,
        have_stock=True,
        qc=True,
        depth_length=50.0,
        hanging=True,
        structure="Sliding Doors",
        function_features="Shoe Rack",
        installation="Free-standing",
        load_capacity="35 kg",
        advanced_technologies=[]
    ),
    IkeaWardrobe(
        name="SLARHÖLL",
        brand="IKEA",
        product_id="W010",
        color="Yellow",
        style="Retro",
        materials="Plastic/Metal",
        length=155.0,
        width=52.0,
        height=195.0,
        weight=18.5,
        serial_no=1010,
        country_of_origin="Turkey",
        price=89.99,
        warranty=5,
        have_stock=True,
        qc=True,
        depth_length=45.0,
        hanging=False,
        structure="Cube System",
        function_features="Removable Bins",
        installation="Wall-mounted",
        load_capacity="25 kg",
        advanced_technologies=[]
    )
]

ikea_desks = [
    IkeaDesk(
        name="BEKANT",
        brand="IKEA",
        product_id="D001",
        color="White",
        style="Modern",
        materials="Particleboard",
        length=160.0,
        width=80.0,
        height=72.0,
        weight=30.5,
        serial_no=2001,
        country_of_origin="Sweden",
        price=199.99,
        warranty=5,
        have_stock=True,
        qc=True,
        design_feature="Adjustable height",
        ergonomics="Ergonomic edge",
        additional_options="Cable management"
    ),
    IkeaDesk(
        name="MICKE",
        brand="IKEA",
        product_id="D002",
        color="Black-Brown",
        style="Contemporary",
        materials="Fiberboard",
        length=105.0,
        width=50.0,
        height=75.0,
        weight=25.0,
        serial_no=2002,
        country_of_origin="China",
        price=99.99,
        warranty=2,
        have_stock=True,
        qc=True,
        design_feature="Compact design",
        ergonomics="Rounded corners",
        additional_options="Integrated drawer"
    ),
    IkeaDesk(
        name="MALM",
        brand="IKEA",
        product_id="D003",
        color="Oak Veneer",
        style="Scandinavian",
        materials="Wood",
        length=140.0,
        width=65.0,
        height=73.0,
        weight=28.0,
        serial_no=2003,
        country_of_origin="Poland",
        price=149.99,
        warranty=10,
        have_stock=True,
        qc=True,
        design_feature="Pull-out panel",
        ergonomics="Soft-closing drawers",
        additional_options="File storage"
    ),
    IkeaDesk(
        name="LINNMON",
        brand="IKEA",
        product_id="D004",
        color="Gray",
        style="Minimalist",
        materials="Particleboard/Steel",
        length=120.0,
        width=60.0,
        height=70.0,
        weight=15.0,
        serial_no=2004,
        country_of_origin="Germany",
        price=49.99,
        warranty=1,
        have_stock=True,
        qc=True,
        design_feature="Lightweight",
        ergonomics="Smooth surface",
        additional_options="Leg attachments"
    ),
    IkeaDesk(
        name="TROTTEN",
        brand="IKEA",
        product_id="D005",
        color="Stained Oak",
        style="Industrial",
        materials="Steel/Wood",
        length=150.0,
        width=75.0,
        height=72.0,
        weight=40.0,
        serial_no=2005,
        country_of_origin="USA",
        price=179.99,
        warranty=5,
        have_stock=True,
        qc=True,
        design_feature="Electric height adjustment",
        ergonomics="Memory preset buttons",
        additional_options="Sturdy frame"
    ),
    IkeaDesk(
        name="ALEX",
        brand="IKEA",
        product_id="D006",
        color="Turquoise",
        style="Retro",
        materials="Plywood/Plastic",
        length=100.0,
        width=55.0,
        height=70.0,
        weight=18.5,
        serial_no=2006,
        country_of_origin="Vietnam",
        price=129.99,
        warranty=3,
        have_stock=True,
        qc=True,
        design_feature="Built-in organizer",
        ergonomics="Sliding drawer",
        additional_options="Lockable compartment"
    ),
    IkeaDesk(
        name="VITTSJÖ",
        brand="IKEA",
        product_id="D007",
        color="Black",
        style="Modern",
        materials="Glass/Metal",
        length=110.0,
        width=55.0,
        height=75.0,
        weight=22.0,
        serial_no=2007,
        country_of_origin="Italy",
        price=89.99,
        warranty=2,
        have_stock=True,
        qc=True,
        design_feature="Floating design",
        ergonomics="Tempered glass surface",
        additional_options="Wall anchors included"
    ),
    IkeaDesk(
        name="KULLABERG",
        brand="IKEA",
        product_id="D008",
        color="Natural Bamboo",
        style="Rustic",
        materials="Bamboo/Steel",
        length=130.0,
        width=70.0,
        height=74.0,
        weight=20.0,
        serial_no=2008,
        country_of_origin="Indonesia",
        price=159.99,
        warranty=5,
        have_stock=True,
        qc=True,
        design_feature="Curved edges",
        ergonomics="Anti-slip surface",
        additional_options="Monitor stand"
    ),
    IkeaDesk(
        name="FREDDE",
        brand="IKEA",
        product_id="D009",
        color="Black/Red",
        style="Gaming",
        materials="Particleboard/Plastic",
        length=160.0,
        width=85.0,
        height=150.0,
        weight=50.0,
        serial_no=2009,
        country_of_origin="China",
        price=249.99,
        warranty=5,
        have_stock=True,
        qc=True,
        design_feature="Multi-level design",
        ergonomics="Cable organizers",
        additional_options="Headphone hook"
    ),
    IkeaDesk(
        name="SKARSTA",
        brand="IKEA",
        product_id="D010",
        color="Birch",
        style="Functional",
        materials="Solid Wood",
        length=120.0,
        width=70.0,
        height=72.0,
        weight=35.0,
        serial_no=2010,
        country_of_origin="Norway",
        price=139.99,
        warranty=10,
        have_stock=True,
        qc=True,
        design_feature="Manual crank adjustment",
        ergonomics="Spacious work area",
        additional_options="Drawer unit compatibility"
    )
]

ikea_tv_cabinets = [
    IkeaTV_Cabinet(
        name="LACK",
        brand="IKEA",
        product_id="TV001",
        color="Black",
        style="Modern",
        materials="Particleboard",
        length=160.0,
        width=40.0,
        height=50.0,
        weight=25.5,
        serial_no=3001,
        country_of_origin="Sweden",
        price=79.99,
        warranty=2,
        have_stock=True,
        qc=True,
        design_feature="Minimalist floating design",
        compatibility="Up to 65-inch TVs",
        additional_features="Cable management holes"
    ),
    IkeaTV_Cabinet(
        name="FJÄLLBO",
        brand="IKEA",
        product_id="TV002",
        color="Dark Gray",
        style="Industrial",
        materials="Steel/Wood",
        length=140.0,
        width=45.0,
        height=48.0,
        weight=35.0,
        serial_no=3002,
        country_of_origin="China",
        price=129.99,
        warranty=5,
        have_stock=True,
        qc=True,
        design_feature="Metal frame construction",
        compatibility="Up to 75-inch TVs",
        additional_features="Adjustable shelf levels"
    ),
    IkeaTV_Cabinet(
        name="BERGSNÄS",
        brand="IKEA",
        product_id="TV003",
        color="Oak Veneer",
        style="Scandinavian",
        materials="Plywood",
        length=180.0,
        width=50.0,
        height=55.0,
        weight=28.0,
        serial_no=3003,
        country_of_origin="Poland",
        price=149.99,
        warranty=10,
        have_stock=True,
        qc=True,
        design_feature="Hidden storage compartment",
        compatibility="Up to 70-inch TVs",
        additional_features="Soft-close drawers"
    ),
    IkeaTV_Cabinet(
        name="BRIMNES",
        brand="IKEA",
        product_id="TV004",
        color="White",
        style="Contemporary",
        materials="Fiberboard",
        length=120.0,
        width=38.0,
        height=45.0,
        weight=18.0,
        serial_no=3004,
        country_of_origin="Vietnam",
        price=89.99,
        warranty=3,
        have_stock=True,
        qc=True,
        design_feature="Integrated glass doors",
        compatibility="Up to 55-inch TVs",
        additional_features="LED lighting system"
    ),
    IkeaTV_Cabinet(
        name="HEMNES",
        brand="IKEA",
        product_id="TV005",
        color="Dark Blue",
        style="Traditional",
        materials="Solid Pine",
        length=200.0,
        width=55.0,
        height=60.0,
        weight=40.0,
        serial_no=3005,
        country_of_origin="Lithuania",
        price=199.99,
        warranty=5,
        have_stock=True,
        qc=True,
        design_feature="Cabinet with paneled fronts",
        compatibility="Up to 85-inch TVs",
        additional_features="Lockable storage"
    ),
    IkeaTV_Cabinet(
        name="LÖVBACKEN",
        brand="IKEA",
        product_id="TV006",
        color="Walnut",
        style="Mid-Century",
        materials="Wood/Metal",
        length=150.0,
        width=42.0,
        height=52.0,
        weight=30.5,
        serial_no=3006,
        country_of_origin="Germany",
        price=169.99,
        warranty=5,
        have_stock=True,
        qc=True,
        design_feature="Tapered legs",
        compatibility="Up to 60-inch TVs",
        additional_features="Heat-resistant surface"
    ),
    IkeaTV_Cabinet(
        name="KALLAX",
        brand="IKEA",
        product_id="TV007",
        color="Turquoise",
        style="Modern",
        materials="Particleboard",
        length=147.0,
        width=39.0,
        height=57.0,
        weight=22.0,
        serial_no=3007,
        country_of_origin="USA",
        price=69.99,
        warranty=2,
        have_stock=True,
        qc=True,
        design_feature="Cube storage system",
        compatibility="Up to 50-inch TVs",
        additional_features="Convertible to room divider"
    ),
    IkeaTV_Cabinet(
        name="BESTÅ",
        brand="IKEA",
        product_id="TV008",
        color="High-Gloss Black",
        style="Modern",
        materials="Foil/Wood",
        length=180.0,
        width=48.0,
        height=58.0,
        weight=45.0,
        serial_no=3008,
        country_of_origin="China",
        price=259.99,
        warranty=10,
        have_stock=True,
        qc=True,
        design_feature="Wall-mounted configuration",
        compatibility="Up to 80-inch TVs",
        additional_features="Integrated sound system space"
    ),
    IkeaTV_Cabinet(
        name="MALM",
        brand="IKEA",
        product_id="TV009",
        color="Birch",
        style="Minimalist",
        materials="Fiberboard",
        length=190.0,
        width=50.0,
        height=45.0,
        weight=33.0,
        serial_no=3009,
        country_of_origin="Sweden",
        price=139.99,
        warranty=5,
        have_stock=True,
        qc=True,
        design_feature="Sliding door mechanism",
        compatibility="Up to 65-inch TVs",
        additional_features="Hidden cable organizer"
    ),
    IkeaTV_Cabinet(
        name="TROGEN",
        brand="IKEA",
        product_id="TV010",
        color="Light Gray",
        style="Rustic",
        materials="Reclaimed Wood",
        length=170.0,
        width=47.0,
        height=53.0,
        weight=38.5,
        serial_no=3010,
        country_of_origin="Thailand",
        price=179.99,
        warranty=5,
        have_stock=True,
        qc=True,
        design_feature="Distressed wood finish",
        compatibility="Up to 70-inch TVs",
        additional_features="Wine rack integration"
    )
]

3.  第三部份：
    # Brainstorming: 將此部份分支一個Shopping Cert的Python插件，以方便將來可作不同更改
    從ikea_furniture的資料選擇出[W003, D008, TV009]這三種傢俬，並生成購物車，並把3件傢俬放進購物籃，並計算總金額