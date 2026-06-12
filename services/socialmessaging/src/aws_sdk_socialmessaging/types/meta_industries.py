"""Generated from Smithy shape ``com.amazonaws.socialmessaging#MetaIndustries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_socialmessaging.types.meta_industry

MetaIndustries: TypeAlias = list[
    "aws_sdk_socialmessaging.types.meta_industry.MetaIndustry"
]


# --- restJson1 ser/de ---
def serialize_json(value: MetaIndustries) -> list:
    return list(value)


def deserialize_json(data: list) -> MetaIndustries:
    return list(data)
