"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeDeviceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.device_arn
    import capo_sagemaker.types.device_description
    import capo_sagemaker.types.edge_models
    import capo_sagemaker.types.edge_version
    import capo_sagemaker.types.entity_name
    import capo_sagemaker.types.integer
    import capo_sagemaker.types.next_token
    import capo_sagemaker.types.thing_name
    import capo_sagemaker.types.timestamp


class DescribeDeviceResponse(TypedDict, closed=True):
    device_arn: NotRequired["capo_sagemaker.types.device_arn.DeviceArn"]
    """<p>The Amazon Resource Name (ARN) of the device.</p>"""
    device_name: NotRequired["capo_sagemaker.types.entity_name.EntityName"]
    """<p>The unique identifier of the device.</p>"""
    description: NotRequired[
        "capo_sagemaker.types.device_description.DeviceDescription"
    ]
    """<p>A description of the device.</p>"""
    device_fleet_name: NotRequired["capo_sagemaker.types.entity_name.EntityName"]
    """<p>The name of the fleet the device belongs to.</p>"""
    iot_thing_name: NotRequired["capo_sagemaker.types.thing_name.ThingName"]
    """<p>The Amazon Web Services Internet of Things (IoT) object thing name associated with the device.</p>"""
    registration_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The timestamp of the last registration or de-reregistration.</p>"""
    latest_heartbeat: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The last heartbeat received from the device.</p>"""
    models: NotRequired["capo_sagemaker.types.edge_models.EdgeModels"]
    """<p>Models on the device.</p>"""
    max_models: NotRequired["capo_sagemaker.types.integer.Integer"]
    """<p>The maximum number of models.</p>"""
    next_token: NotRequired["capo_sagemaker.types.next_token.NextToken"]
    """<p>The response from the last list when returning a list large enough to need tokening.</p>"""
    agent_version: NotRequired["capo_sagemaker.types.edge_version.EdgeVersion"]
    """<p>Edge Manager agent version.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDeviceResponse) -> dict:
    out: dict = {}
    if "device_arn" in value:
        out["DeviceArn"] = value["device_arn"]
    if "device_name" in value:
        out["DeviceName"] = value["device_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "device_fleet_name" in value:
        out["DeviceFleetName"] = value["device_fleet_name"]
    if "iot_thing_name" in value:
        out["IotThingName"] = value["iot_thing_name"]
    if "registration_time" in value:
        import capo_sagemaker.types.timestamp

        out["RegistrationTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["registration_time"]
        )
    if "latest_heartbeat" in value:
        import capo_sagemaker.types.timestamp

        out["LatestHeartbeat"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["latest_heartbeat"]
        )
    if "models" in value:
        import capo_sagemaker.types.edge_models

        out["Models"] = capo_sagemaker.types.edge_models.serialize_aws_json_1_1(
            value["models"]
        )
    if "max_models" in value:
        out["MaxModels"] = value["max_models"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "agent_version" in value:
        out["AgentVersion"] = value["agent_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDeviceResponse:
    out: DescribeDeviceResponse = {}  # type: ignore[typeddict-item]
    if "DeviceArn" in data:
        out["device_arn"] = data["DeviceArn"]
    if "DeviceName" in data:
        out["device_name"] = data["DeviceName"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "DeviceFleetName" in data:
        out["device_fleet_name"] = data["DeviceFleetName"]
    if "IotThingName" in data:
        out["iot_thing_name"] = data["IotThingName"]
    if "RegistrationTime" in data:
        import capo_sagemaker.types.timestamp

        out["registration_time"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["RegistrationTime"]
            )
        )
    if "LatestHeartbeat" in data:
        import capo_sagemaker.types.timestamp

        out["latest_heartbeat"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LatestHeartbeat"]
            )
        )
    if "Models" in data:
        import capo_sagemaker.types.edge_models

        out["models"] = capo_sagemaker.types.edge_models.deserialize_aws_json_1_1(
            data["Models"]
        )
    if "MaxModels" in data:
        out["max_models"] = data["MaxModels"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "AgentVersion" in data:
        out["agent_version"] = data["AgentVersion"]
    return out
