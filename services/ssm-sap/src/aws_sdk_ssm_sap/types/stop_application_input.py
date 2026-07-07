"""Generated from Smithy shape ``com.amazonaws.ssmsap#StopApplicationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ssm_sap.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm_sap.types.application_id
    import aws_sdk_ssm_sap.types.connected_entity_type


class StopApplicationInput(TypedDict, closed=True):
    application_id: "aws_sdk_ssm_sap.types.application_id.ApplicationId"
    """<p>The ID of the application.</p>"""
    stop_connected_entity: NotRequired[
        "aws_sdk_ssm_sap.types.connected_entity_type.ConnectedEntityType"
    ]
    """<p>Specify the <code>ConnectedEntityType</code>. Accepted type is <code>DBMS</code>.</p> <p>If this parameter is included, the connected DBMS (Database Management System) will be stopped.</p>"""
    include_ec2_instance_shutdown: NotRequired["bool"]
    """<p>Boolean. If included and if set to <code>True</code>, the StopApplication operation will shut down the associated Amazon EC2 instance in addition to the application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopApplicationInput) -> dict:
    out: dict = {}
    out["ApplicationId"] = value["application_id"]
    if "stop_connected_entity" in value:
        import aws_sdk_ssm_sap.types.connected_entity_type

        out["StopConnectedEntity"] = (
            aws_sdk_ssm_sap.types.connected_entity_type.serialize_json(
                value["stop_connected_entity"]
            )
        )
    if "include_ec2_instance_shutdown" in value:
        out["IncludeEc2InstanceShutdown"] = value["include_ec2_instance_shutdown"]
    return out


def deserialize_json(data: dict) -> StopApplicationInput:
    out: StopApplicationInput = {}  # type: ignore[typeddict-item]
    if "ApplicationId" in data:
        out["application_id"] = data["ApplicationId"]
    else:
        raise DeserializationError("StopApplicationInput.application_id required")
    if "StopConnectedEntity" in data:
        import aws_sdk_ssm_sap.types.connected_entity_type

        out["stop_connected_entity"] = (
            aws_sdk_ssm_sap.types.connected_entity_type.deserialize_json(
                data["StopConnectedEntity"]
            )
        )
    if "IncludeEc2InstanceShutdown" in data:
        out["include_ec2_instance_shutdown"] = data["IncludeEc2InstanceShutdown"]
    return out
