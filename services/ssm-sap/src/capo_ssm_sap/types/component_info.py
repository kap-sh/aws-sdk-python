"""Generated from Smithy shape ``com.amazonaws.ssmsap#ComponentInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ssm_sap.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ssm_sap.types.component_type
    import capo_ssm_sap.types.instance_id
    import capo_ssm_sap.types.sid


class ComponentInfo(TypedDict, closed=True):
    component_type: "capo_ssm_sap.types.component_type.ComponentType"
    """<p>This string is the type of the component.</p> <p>Accepted value is <code>WD</code>.</p>"""
    sid: "capo_ssm_sap.types.sid.SID"
    """<p>This string is the SAP System ID of the component.</p> <p>Accepted values are alphanumeric.</p>"""
    ec2_instance_id: "capo_ssm_sap.types.instance_id.InstanceId"
    """<p>This is the Amazon EC2 instance on which your SAP component is running.</p> <p>Accepted values are alphanumeric.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ComponentInfo) -> dict:
    out: dict = {}
    import capo_ssm_sap.types.component_type

    out["ComponentType"] = capo_ssm_sap.types.component_type.serialize_json(
        value["component_type"]
    )
    out["Sid"] = value["sid"]
    out["Ec2InstanceId"] = value["ec2_instance_id"]
    return out


def deserialize_json(data: dict) -> ComponentInfo:
    out: ComponentInfo = {}  # type: ignore[typeddict-item]
    if "ComponentType" in data:
        import capo_ssm_sap.types.component_type

        out["component_type"] = capo_ssm_sap.types.component_type.deserialize_json(
            data["ComponentType"]
        )
    else:
        raise DeserializationError("ComponentInfo.component_type required")
    if "Sid" in data:
        out["sid"] = data["Sid"]
    else:
        raise DeserializationError("ComponentInfo.sid required")
    if "Ec2InstanceId" in data:
        out["ec2_instance_id"] = data["Ec2InstanceId"]
    else:
        raise DeserializationError("ComponentInfo.ec2_instance_id required")
    return out
