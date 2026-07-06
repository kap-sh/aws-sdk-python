"""Generated from Smithy shape ``com.amazonaws.sagemaker#GetDeviceFleetReportResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.agent_versions
    import aws_sdk_sagemaker.types.device_fleet_arn
    import aws_sdk_sagemaker.types.device_fleet_description
    import aws_sdk_sagemaker.types.device_stats
    import aws_sdk_sagemaker.types.edge_model_stats
    import aws_sdk_sagemaker.types.edge_output_config
    import aws_sdk_sagemaker.types.entity_name
    import aws_sdk_sagemaker.types.timestamp


class GetDeviceFleetReportResponse(TypedDict, closed=True):
    device_fleet_arn: NotRequired[
        "aws_sdk_sagemaker.types.device_fleet_arn.DeviceFleetArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the device.</p>"""
    device_fleet_name: NotRequired["aws_sdk_sagemaker.types.entity_name.EntityName"]
    """<p>The name of the fleet.</p>"""
    output_config: NotRequired[
        "aws_sdk_sagemaker.types.edge_output_config.EdgeOutputConfig"
    ]
    """<p>The output configuration for storing sample data collected by the fleet.</p>"""
    description: NotRequired[
        "aws_sdk_sagemaker.types.device_fleet_description.DeviceFleetDescription"
    ]
    """<p>Description of the fleet.</p>"""
    report_generated: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>Timestamp of when the report was generated.</p>"""
    device_stats: NotRequired["aws_sdk_sagemaker.types.device_stats.DeviceStats"]
    """<p>Status of devices.</p>"""
    agent_versions: NotRequired["aws_sdk_sagemaker.types.agent_versions.AgentVersions"]
    """<p>The versions of Edge Manager agent deployed on the fleet.</p>"""
    model_stats: NotRequired["aws_sdk_sagemaker.types.edge_model_stats.EdgeModelStats"]
    """<p>Status of model on device.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDeviceFleetReportResponse) -> dict:
    out: dict = {}
    if "device_fleet_arn" in value:
        out["DeviceFleetArn"] = value["device_fleet_arn"]
    if "device_fleet_name" in value:
        out["DeviceFleetName"] = value["device_fleet_name"]
    if "output_config" in value:
        import aws_sdk_sagemaker.types.edge_output_config

        out["OutputConfig"] = (
            aws_sdk_sagemaker.types.edge_output_config.serialize_aws_json_1_1(
                value["output_config"]
            )
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "report_generated" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["ReportGenerated"] = (
            aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["report_generated"]
            )
        )
    if "device_stats" in value:
        import aws_sdk_sagemaker.types.device_stats

        out["DeviceStats"] = (
            aws_sdk_sagemaker.types.device_stats.serialize_aws_json_1_1(
                value["device_stats"]
            )
        )
    if "agent_versions" in value:
        import aws_sdk_sagemaker.types.agent_versions

        out["AgentVersions"] = (
            aws_sdk_sagemaker.types.agent_versions.serialize_aws_json_1_1(
                value["agent_versions"]
            )
        )
    if "model_stats" in value:
        import aws_sdk_sagemaker.types.edge_model_stats

        out["ModelStats"] = (
            aws_sdk_sagemaker.types.edge_model_stats.serialize_aws_json_1_1(
                value["model_stats"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDeviceFleetReportResponse:
    out: GetDeviceFleetReportResponse = {}  # type: ignore[typeddict-item]
    if "DeviceFleetArn" in data:
        out["device_fleet_arn"] = data["DeviceFleetArn"]
    if "DeviceFleetName" in data:
        out["device_fleet_name"] = data["DeviceFleetName"]
    if "OutputConfig" in data:
        import aws_sdk_sagemaker.types.edge_output_config

        out["output_config"] = (
            aws_sdk_sagemaker.types.edge_output_config.deserialize_aws_json_1_1(
                data["OutputConfig"]
            )
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "ReportGenerated" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["report_generated"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["ReportGenerated"]
            )
        )
    if "DeviceStats" in data:
        import aws_sdk_sagemaker.types.device_stats

        out["device_stats"] = (
            aws_sdk_sagemaker.types.device_stats.deserialize_aws_json_1_1(
                data["DeviceStats"]
            )
        )
    if "AgentVersions" in data:
        import aws_sdk_sagemaker.types.agent_versions

        out["agent_versions"] = (
            aws_sdk_sagemaker.types.agent_versions.deserialize_aws_json_1_1(
                data["AgentVersions"]
            )
        )
    if "ModelStats" in data:
        import aws_sdk_sagemaker.types.edge_model_stats

        out["model_stats"] = (
            aws_sdk_sagemaker.types.edge_model_stats.deserialize_aws_json_1_1(
                data["ModelStats"]
            )
        )
    return out
