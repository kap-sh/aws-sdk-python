"""Generated from Smithy shape ``com.amazonaws.securityhub#CategoryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string

CategoryList: TypeAlias = list[
    "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
]


# --- restJson1 ser/de ---
def serialize_json(value: CategoryList) -> list:
    return list(value)


def deserialize_json(data: list) -> CategoryList:
    return list(data)
