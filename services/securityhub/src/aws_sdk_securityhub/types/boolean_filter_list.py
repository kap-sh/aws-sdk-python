"""Generated from Smithy shape ``com.amazonaws.securityhub#BooleanFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.boolean_filter

BooleanFilterList: TypeAlias = list[
    "aws_sdk_securityhub.types.boolean_filter.BooleanFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: BooleanFilterList) -> list:
    import aws_sdk_securityhub.types.boolean_filter

    out: list = []
    for item in value:
        out.append(aws_sdk_securityhub.types.boolean_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> BooleanFilterList:
    import aws_sdk_securityhub.types.boolean_filter

    out: BooleanFilterList = []
    for item in data:
        out.append(aws_sdk_securityhub.types.boolean_filter.deserialize_json(item))
    return out
