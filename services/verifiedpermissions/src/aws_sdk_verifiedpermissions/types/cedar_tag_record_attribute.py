"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#CedarTagRecordAttribute``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_verifiedpermissions.types.cedar_tag_value

CedarTagRecordAttribute: TypeAlias = dict["str", "aws_sdk_verifiedpermissions.types.cedar_tag_value.CedarTagValue"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(input_to_serialize: CedarTagRecordAttribute) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_verifiedpermissions.types.cedar_tag_value
        out[key] = aws_sdk_verifiedpermissions.types.cedar_tag_value.serialize_aws_json_1_0(value)
    return out


def deserialize_aws_json_1_0(data: dict) -> CedarTagRecordAttribute:
    out: CedarTagRecordAttribute = {}
    for key, value in data.items():
        import aws_sdk_verifiedpermissions.types.cedar_tag_value
        out[key] = aws_sdk_verifiedpermissions.types.cedar_tag_value.deserialize_aws_json_1_0(value)
    return out