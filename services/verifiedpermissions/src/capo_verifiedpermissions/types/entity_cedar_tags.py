"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#EntityCedarTags``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.cedar_tag_value

EntityCedarTags: TypeAlias = dict[
    "str", "capo_verifiedpermissions.types.cedar_tag_value.CedarTagValue"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(input_to_serialize: EntityCedarTags) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_verifiedpermissions.types.cedar_tag_value

        out[key] = (
            capo_verifiedpermissions.types.cedar_tag_value.serialize_aws_json_1_0(value)
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> EntityCedarTags:
    out: EntityCedarTags = {}
    for key, value in data.items():
        import capo_verifiedpermissions.types.cedar_tag_value

        out[key] = (
            capo_verifiedpermissions.types.cedar_tag_value.deserialize_aws_json_1_0(
                value
            )
        )
    return out
