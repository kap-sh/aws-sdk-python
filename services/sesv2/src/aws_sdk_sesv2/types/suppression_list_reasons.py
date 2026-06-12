"""Generated from Smithy shape ``com.amazonaws.sesv2#SuppressionListReasons``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.suppression_list_reason

SuppressionListReasons: TypeAlias = list[
    "aws_sdk_sesv2.types.suppression_list_reason.SuppressionListReason"
]


# --- restJson1 ser/de ---
def serialize_json(value: SuppressionListReasons) -> list:
    import aws_sdk_sesv2.types.suppression_list_reason

    out: list = []
    for item in value:
        out.append(aws_sdk_sesv2.types.suppression_list_reason.serialize_json(item))
    return out


def deserialize_json(data: list) -> SuppressionListReasons:
    import aws_sdk_sesv2.types.suppression_list_reason

    out: SuppressionListReasons = []
    for item in data:
        out.append(aws_sdk_sesv2.types.suppression_list_reason.deserialize_json(item))
    return out
