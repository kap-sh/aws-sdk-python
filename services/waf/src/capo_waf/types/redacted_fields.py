"""Generated from Smithy shape ``com.amazonaws.waf#RedactedFields``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_waf.types.field_to_match

RedactedFields: TypeAlias = list["capo_waf.types.field_to_match.FieldToMatch"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RedactedFields) -> list:
    import capo_waf.types.field_to_match

    out: list = []
    for item in value:
        out.append(capo_waf.types.field_to_match.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> RedactedFields:
    import capo_waf.types.field_to_match

    out: RedactedFields = []
    for item in data:
        out.append(capo_waf.types.field_to_match.deserialize_aws_json_1_1(item))
    return out
