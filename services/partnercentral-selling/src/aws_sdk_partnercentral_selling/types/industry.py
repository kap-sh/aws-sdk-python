"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#Industry``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_partnercentral_selling.errors import DeserializationError

Industry: TypeAlias = Literal[
    "Aerospace",
    "Agriculture",
    "Automotive",
    "Computers and Electronics",
    "Consumer Goods",
    "Education",
    "Energy - Oil and Gas",
    "Energy - Power and Utilities",
    "Financial Services",
    "Gaming",
    "Government",
    "Healthcare",
    "Hospitality",
    "Life Sciences",
    "Manufacturing",
    "Marketing and Advertising",
    "Media and Entertainment",
    "Mining",
    "Non-Profit Organization",
    "Professional Services",
    "Real Estate and Construction",
    "Retail",
    "Software and Internet",
    "Telecommunications",
    "Transportation and Logistics",
    "Travel",
    "Wholesale and Distribution",
    "Other",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Aerospace",
        "Agriculture",
        "Automotive",
        "Computers and Electronics",
        "Consumer Goods",
        "Education",
        "Energy - Oil and Gas",
        "Energy - Power and Utilities",
        "Financial Services",
        "Gaming",
        "Government",
        "Healthcare",
        "Hospitality",
        "Life Sciences",
        "Manufacturing",
        "Marketing and Advertising",
        "Media and Entertainment",
        "Mining",
        "Non-Profit Organization",
        "Professional Services",
        "Real Estate and Construction",
        "Retail",
        "Software and Internet",
        "Telecommunications",
        "Transportation and Logistics",
        "Travel",
        "Wholesale and Distribution",
        "Other",
    )
)


def serialize_aws_json_1_0(value: Industry) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> Industry:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Industry value: {data!r}")
    return cast(Industry, data)
