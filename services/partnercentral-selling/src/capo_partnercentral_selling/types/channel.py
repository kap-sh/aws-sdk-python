"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#Channel``."""

from typing import Literal, TypeAlias, cast

Channel: TypeAlias = Literal[
    "AWS Marketing Central",
    "Content Syndication",
    "Display",
    "Email",
    "Live Event",
    "Out Of Home (OOH)",
    "Print",
    "Search",
    "Social",
    "Telemarketing",
    "TV",
    "Video",
    "Virtual Event",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Channel) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> Channel:
    return cast(Channel, data)
