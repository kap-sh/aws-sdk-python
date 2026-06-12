"""Generated from Smithy shape ``com.amazonaws.securityhub#StandardsSubscriptionArns``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string

StandardsSubscriptionArns: TypeAlias = list[
    "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
]


# --- restJson1 ser/de ---
def serialize_json(value: StandardsSubscriptionArns) -> list:
    return list(value)


def deserialize_json(data: list) -> StandardsSubscriptionArns:
    return list(data)
