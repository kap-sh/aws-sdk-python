"""Generated from Smithy shape ``com.amazonaws.cleanrooms#IdMappingTableInputReferenceConfig``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.id_mapping_table_input_reference_arn


class IdMappingTableInputReferenceConfig(TypedDict):
    input_reference_arn: "aws_sdk_cleanrooms.types.id_mapping_table_input_reference_arn.IdMappingTableInputReferenceArn"
    """<p>The Amazon Resource Name (ARN) of the referenced resource in Entity Resolution. Valid values are ID mapping workflow ARNs.</p>"""
    manage_resource_policies: "bool"
    """<p>When <code>TRUE</code>, Clean Rooms manages permissions for the ID mapping table resource. </p> <p>When <code>FALSE</code>, the resource owner manages permissions for the ID mapping table resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IdMappingTableInputReferenceConfig) -> dict:
    out: dict = {}
    out["inputReferenceArn"] = value["input_reference_arn"]
    out["manageResourcePolicies"] = value["manage_resource_policies"]
    return out


def deserialize_json(data: dict) -> IdMappingTableInputReferenceConfig:
    out: IdMappingTableInputReferenceConfig = {}  # type: ignore[typeddict-item]
    if "inputReferenceArn" in data:
        out["input_reference_arn"] = data["inputReferenceArn"]
    else:
        raise DeserializationError(
            "IdMappingTableInputReferenceConfig.input_reference_arn required"
        )
    if "manageResourcePolicies" in data:
        out["manage_resource_policies"] = data["manageResourcePolicies"]
    else:
        raise DeserializationError(
            "IdMappingTableInputReferenceConfig.manage_resource_policies required"
        )
    return out
