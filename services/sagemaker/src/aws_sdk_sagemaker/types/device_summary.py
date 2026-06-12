"""Generated from Smithy shape ``com.amazonaws.sagemaker#DeviceSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.device_arn
    import aws_sdk_sagemaker.types.device_description
    import aws_sdk_sagemaker.types.edge_model_summaries
    import aws_sdk_sagemaker.types.edge_version
    import aws_sdk_sagemaker.types.entity_name
    import aws_sdk_sagemaker.types.thing_name
    import aws_sdk_sagemaker.types.timestamp


class DeviceSummary(TypedDict):
    device_name: NotRequired["aws_sdk_sagemaker.types.entity_name.EntityName"]
    """<p>The unique identifier of the device.</p>"""
    device_arn: NotRequired["aws_sdk_sagemaker.types.device_arn.DeviceArn"]
    """<p>Amazon Resource Name (ARN) of the device.</p>"""
    description: NotRequired[
        "aws_sdk_sagemaker.types.device_description.DeviceDescription"
    ]
    """<p>A description of the device.</p>"""
    device_fleet_name: NotRequired["aws_sdk_sagemaker.types.entity_name.EntityName"]
    """<p>The name of the fleet the device belongs to.</p>"""
    iot_thing_name: NotRequired["aws_sdk_sagemaker.types.thing_name.ThingName"]
    """<p>The Amazon Web Services Internet of Things (IoT) object thing name associated with the device..</p>"""
    registration_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>The timestamp of the last registration or de-reregistration.</p>"""
    latest_heartbeat: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>The last heartbeat received from the device.</p>"""
    models: NotRequired[
        "aws_sdk_sagemaker.types.edge_model_summaries.EdgeModelSummaries"
    ]
    """<p>Models on the device.</p>"""
    agent_version: NotRequired["aws_sdk_sagemaker.types.edge_version.EdgeVersion"]
    """<p>Edge Manager agent version.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeviceSummary) -> dict:
    out: dict = {}
    if "device_name" in value:
        out["DeviceName"] = value["device_name"]
    if "device_arn" in value:
        out["DeviceArn"] = value["device_arn"]
    if "description" in value:
        out["Description"] = value["description"]
    if "device_fleet_name" in value:
        out["DeviceFleetName"] = value["device_fleet_name"]
    if "iot_thing_name" in value:
        out["IotThingName"] = value["iot_thing_name"]
    if "registration_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["RegistrationTime"] = (
            aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["registration_time"]
            )
        )
    if "latest_heartbeat" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["LatestHeartbeat"] = (
            aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["latest_heartbeat"]
            )
        )
    if "models" in value:
        import aws_sdk_sagemaker.types.edge_model_summaries

        out["Models"] = (
            aws_sdk_sagemaker.types.edge_model_summaries.serialize_aws_json_1_1(
                value["models"]
            )
        )
    if "agent_version" in value:
        out["AgentVersion"] = value["agent_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeviceSummary:
    out: DeviceSummary = {}  # type: ignore[typeddict-item]
    if "DeviceName" in data:
        out["device_name"] = data["DeviceName"]
    if "DeviceArn" in data:
        out["device_arn"] = data["DeviceArn"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "DeviceFleetName" in data:
        out["device_fleet_name"] = data["DeviceFleetName"]
    if "IotThingName" in data:
        out["iot_thing_name"] = data["IotThingName"]
    if "RegistrationTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["registration_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["RegistrationTime"]
            )
        )
    if "LatestHeartbeat" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["latest_heartbeat"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LatestHeartbeat"]
            )
        )
    if "Models" in data:
        import aws_sdk_sagemaker.types.edge_model_summaries

        out["models"] = (
            aws_sdk_sagemaker.types.edge_model_summaries.deserialize_aws_json_1_1(
                data["Models"]
            )
        )
    if "AgentVersion" in data:
        out["agent_version"] = data["AgentVersion"]
    return out
