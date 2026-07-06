"""Generated from Smithy shape ``com.amazonaws.tnb#ModifyVnfInfoMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_tnb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_tnb.types.vnf_instance_id


class ModifyVnfInfoMetadata(TypedDict, closed=True):
    vnf_instance_id: "aws_sdk_tnb.types.vnf_instance_id.VnfInstanceId"
    """<p>The network function instance that was updated in the network instance.</p>"""
    vnf_configurable_properties: "object"
    """<p>The configurable properties used during update of the network function instance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ModifyVnfInfoMetadata) -> dict:
    out: dict = {}
    out["vnfInstanceId"] = value["vnf_instance_id"]
    out["vnfConfigurableProperties"] = value["vnf_configurable_properties"]
    return out


def deserialize_json(data: dict) -> ModifyVnfInfoMetadata:
    out: ModifyVnfInfoMetadata = {}  # type: ignore[typeddict-item]
    if "vnfInstanceId" in data:
        out["vnf_instance_id"] = data["vnfInstanceId"]
    else:
        raise DeserializationError("ModifyVnfInfoMetadata.vnf_instance_id required")
    if "vnfConfigurableProperties" in data:
        out["vnf_configurable_properties"] = data["vnfConfigurableProperties"]
    else:
        raise DeserializationError(
            "ModifyVnfInfoMetadata.vnf_configurable_properties required"
        )
    return out
