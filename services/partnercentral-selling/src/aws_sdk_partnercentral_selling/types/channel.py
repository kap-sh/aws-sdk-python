"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#Channel``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_partnercentral_selling.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
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
    )
)


def serialize_aws_json_1_0(value: Channel) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> Channel:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Channel value: {data!r}")
    return cast(Channel, data)
