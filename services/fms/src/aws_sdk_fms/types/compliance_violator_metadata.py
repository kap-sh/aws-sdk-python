"""Generated from Smithy shape ``com.amazonaws.fms#ComplianceViolatorMetadata``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_fms.types.length_bounded_string

ComplianceViolatorMetadata: TypeAlias = dict[
    "aws_sdk_fms.types.length_bounded_string.LengthBoundedString",
    "aws_sdk_fms.types.length_bounded_string.LengthBoundedString",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: ComplianceViolatorMetadata) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> ComplianceViolatorMetadata:
    out: ComplianceViolatorMetadata = {}
    for key, value in data.items():
        out[key] = value
    return out
