"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#Industry``."""

from typing import Literal, TypeAlias, cast

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
def serialize_aws_json_1_0(value: Industry) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> Industry:
    return cast(Industry, data)
