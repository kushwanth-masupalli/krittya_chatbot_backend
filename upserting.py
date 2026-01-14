from pinecone import Pinecone

pc = Pinecone(api_key="pcsk_4o9kCn_UCiQQtp9DhCvVJeA2iGXVL7K3QmLgcRjcpfpLiFUy5DS7z1n8QxFdKzt3DQ53RB")

index_name = "krittay-vd"

index = pc.Index(index_name)

# Because your index is integrated with a hosted embedding model, you provide inputs as text 
# and Pinecone converts them to dense vectors automatically.
data = [
    {
        "id": "krittya-1",
        "text": "Krittya provides marketing services with the belief that marketing is the core strength and key differentiator for any business. The company focuses on building strong connections with audiences by understanding their needs and delivering the right solutions in the most effective way."
    },
    {
        "id": "krittya-2",
        "text": "Krittya specializes in branding, digital solutions, market research, strategy, home service marketing, and service-based marketing solutions."
    },
    {
        "id": "krittya-3",
        "text": "Krittya delivers a complete 360 degree marketing solution designed to strengthen brand presence, improve visibility, and drive sustainable growth. Services include continuous monthly SEO optimization, round-the-clock customer support, high-impact turbo boost campaigns for faster visibility, and execution by an experienced team of strategists and creatives."
    },
    {
        "id": "krittya-4",
        "text": "Brands often struggle with standing out in competitive markets, maintaining consistent messaging across platforms, and building meaningful audience connections. Krittya solves these challenges through in-depth audience research, goal-aligned creative strategies, and continuous iteration until client satisfaction is achieved."
    },
    {
        "id": "krittya-5",
        "text": "Krittya follows a structured workflow starting with deep discovery to understand brand vision, challenges, and goals. This is followed by strategic planning covering SEO, content, social media, and advertising. Campaigns are executed with precision, continuously optimized through performance tracking, and refined flexibly based on feedback."
    },
    {
        "id": "krittya-6",
        "text": "Krittya emphasizes user-friendly interfaces and strong encryption, ensuring simplicity, clarity, and reliability across all solutions."
    },
    {
        "id": "krittya-7",
        "text": "Clients can speak directly with a team member instead of filling out forms. Support is available via phone at +91 80132 97449 or email at hello@krittya.com."
    },
    {
        "id": "krittya-8",
        "text": "Krittya offers core services including content marketing, social marketing, branding, market research, advertising, and digital solutions to help businesses grow and establish a strong online presence."
    },
    {
        "id": "krittya-9",
        "text": "Krittya positions itself as a thoughtful, research-driven marketing partner that understands audiences deeply and communicates with them at the most suitable time."
    },
    {
        "id": "krittya-10",
        "text": "Krittya has been helping businesses grow since 2017 and highlights professional staff, strong client satisfaction, high ROI performance, and a commitment to understanding and delivering tailored solutions."
    },
    {
        "id": "krittya-11",
        "text": "Krittya offers version one service structures with defined service categories, experience metrics, structured pricing plans, and a process including project initialization, real-time data-driven solutions, and market development."
    },
    {
        "id": "krittya-12",
        "text": "Krittya provides pricing on monthly and yearly commitments. The regular plan costs 35 dollars per month, while the premium plan costs 99 dollars per month and includes extended support and hosting benefits."
    },
    {
        "id": "krittya-13",
        "text": "Krittya can be contacted via phone at +91 81000 24327. The office is located at Park Plaza, Mother Teresa Sarani, Park Street, Kolkata 700016. Email communication is available through hello@krittya.com and krittyamarketing@gmail.com."
    },
    {
        "id": "krittya-14",
        "text": "Krittya is trusted by global brands such as jQuery, Envato, Instagram, Bootstrap, and Dribbble."
    }
]


index.upsert_records(
    namespace="example-namespace",
    records=data
)