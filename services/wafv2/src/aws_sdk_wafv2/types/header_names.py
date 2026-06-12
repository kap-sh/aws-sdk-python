"""Generated from Smithy shape ``com.amazonaws.wafv2#HeaderNames``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.field_to_match_data

HeaderNames: TypeAlias = list[
    "aws_sdk_wafv2.types.field_to_match_data.FieldToMatchData"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HeaderNames) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> HeaderNames:
    return list(data)
