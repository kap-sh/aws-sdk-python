"""Generated from Smithy shape ``com.amazonaws.wafregional#RedactedFields``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_waf_regional.types.field_to_match

RedactedFields: TypeAlias = list[
    "aws_sdk_waf_regional.types.field_to_match.FieldToMatch"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RedactedFields) -> list:
    import aws_sdk_waf_regional.types.field_to_match

    out: list = []
    for item in value:
        out.append(
            aws_sdk_waf_regional.types.field_to_match.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> RedactedFields:
    import aws_sdk_waf_regional.types.field_to_match

    out: RedactedFields = []
    for item in data:
        out.append(
            aws_sdk_waf_regional.types.field_to_match.deserialize_aws_json_1_1(item)
        )
    return out
