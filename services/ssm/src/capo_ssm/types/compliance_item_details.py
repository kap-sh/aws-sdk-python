"""Generated from Smithy shape ``com.amazonaws.ssm#ComplianceItemDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.attribute_name
    import capo_ssm.types.attribute_value

ComplianceItemDetails: TypeAlias = dict[
    "capo_ssm.types.attribute_name.AttributeName",
    "capo_ssm.types.attribute_value.AttributeValue",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: ComplianceItemDetails) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> ComplianceItemDetails:
    out: ComplianceItemDetails = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out
