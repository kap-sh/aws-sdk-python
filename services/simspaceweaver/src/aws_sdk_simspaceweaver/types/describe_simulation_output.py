"""Generated from Smithy shape ``com.amazonaws.simspaceweaver#DescribeSimulationOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_simspaceweaver.types.description
    import aws_sdk_simspaceweaver.types.live_simulation_state
    import aws_sdk_simspaceweaver.types.logging_configuration
    import aws_sdk_simspaceweaver.types.optional_string
    import aws_sdk_simspaceweaver.types.role_arn
    import aws_sdk_simspaceweaver.types.s3_location
    import aws_sdk_simspaceweaver.types.sim_space_weaver_arn
    import aws_sdk_simspaceweaver.types.sim_space_weaver_resource_name
    import aws_sdk_simspaceweaver.types.simulation_status
    import aws_sdk_simspaceweaver.types.simulation_target_status
    import aws_sdk_simspaceweaver.types.time_to_live_string
    import aws_sdk_simspaceweaver.types.timestamp
    import aws_sdk_simspaceweaver.types.uuid


class DescribeSimulationOutput(TypedDict):
    name: NotRequired[
        "aws_sdk_simspaceweaver.types.sim_space_weaver_resource_name.SimSpaceWeaverResourceName"
    ]
    """<p>The name of the simulation.</p>"""
    execution_id: NotRequired["aws_sdk_simspaceweaver.types.uuid.UUID"]
    """<p>A universally unique identifier (UUID) for this simulation.</p>"""
    arn: NotRequired[
        "aws_sdk_simspaceweaver.types.sim_space_weaver_arn.SimSpaceWeaverArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the simulation. For more information about ARNs, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i>.</p>"""
    description: NotRequired["aws_sdk_simspaceweaver.types.description.Description"]
    """<p>The description of the simulation.</p>"""
    role_arn: NotRequired["aws_sdk_simspaceweaver.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of the Identity and Access Management (IAM) role that the simulation assumes to perform actions. For more information about ARNs, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i>. For more information about IAM roles, see <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html\">IAM roles</a> in the <i>Identity and Access Management User Guide</i>.</p>"""
    creation_time: NotRequired["aws_sdk_simspaceweaver.types.timestamp.Timestamp"]
    """<p>The time when the simulation was created, expressed as the number of seconds and milliseconds in UTC since the Unix epoch (0:0:0.000, January 1, 1970).</p>"""
    status: NotRequired[
        "aws_sdk_simspaceweaver.types.simulation_status.SimulationStatus"
    ]
    """<p>The current lifecycle state of the simulation.</p>"""
    target_status: NotRequired[
        "aws_sdk_simspaceweaver.types.simulation_target_status.SimulationTargetStatus"
    ]
    """<p>The desired lifecycle state of the simulation.</p>"""
    schema_s3_location: NotRequired[
        "aws_sdk_simspaceweaver.types.s3_location.S3Location"
    ]
    """<p>The location of the simulation schema in Amazon Simple Storage Service (Amazon S3). For more information about Amazon S3, see the <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html\"> <i>Amazon Simple Storage Service User Guide</i> </a>.</p>"""
    schema_error: NotRequired[
        "aws_sdk_simspaceweaver.types.optional_string.OptionalString"
    ]
    """<p>An error message that SimSpace Weaver returns only if there is a problem with the simulation schema.</p>"""
    logging_configuration: NotRequired[
        "aws_sdk_simspaceweaver.types.logging_configuration.LoggingConfiguration"
    ]
    """<p>Settings that control how SimSpace Weaver handles your simulation log data.</p>"""
    live_simulation_state: NotRequired[
        "aws_sdk_simspaceweaver.types.live_simulation_state.LiveSimulationState"
    ]
    """<p>A collection of additional state information, such as domain and clock configuration.</p>"""
    maximum_duration: NotRequired[
        "aws_sdk_simspaceweaver.types.time_to_live_string.TimeToLiveString"
    ]
    """<p>The maximum running time of the simulation, specified as a number of minutes (m or M), hours (h or H), or days (d or D). The simulation stops when it reaches this limit. The maximum value is <code>14D</code>, or its equivalent in the other units. The default value is <code>14D</code>. A value equivalent to <code>0</code> makes the simulation immediately transition to <code>Stopping</code> as soon as it reaches <code>Started</code>.</p>"""
    snapshot_s3_location: NotRequired[
        "aws_sdk_simspaceweaver.types.s3_location.S3Location"
    ]
    start_error: NotRequired[
        "aws_sdk_simspaceweaver.types.optional_string.OptionalString"
    ]
    """<p>An error message that SimSpace Weaver returns only if a problem occurs when the simulation is in the <code>STARTING</code> state.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeSimulationOutput) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "execution_id" in value:
        out["ExecutionId"] = value["execution_id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "description" in value:
        out["Description"] = value["description"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "creation_time" in value:
        import aws_sdk_simspaceweaver.types.timestamp

        out["CreationTime"] = aws_sdk_simspaceweaver.types.timestamp.serialize_json(
            value["creation_time"]
        )
    if "status" in value:
        out["Status"] = value["status"]
    if "target_status" in value:
        out["TargetStatus"] = value["target_status"]
    if "schema_s3_location" in value:
        import aws_sdk_simspaceweaver.types.s3_location

        out["SchemaS3Location"] = (
            aws_sdk_simspaceweaver.types.s3_location.serialize_json(
                value["schema_s3_location"]
            )
        )
    if "schema_error" in value:
        out["SchemaError"] = value["schema_error"]
    if "logging_configuration" in value:
        import aws_sdk_simspaceweaver.types.logging_configuration

        out["LoggingConfiguration"] = (
            aws_sdk_simspaceweaver.types.logging_configuration.serialize_json(
                value["logging_configuration"]
            )
        )
    if "live_simulation_state" in value:
        import aws_sdk_simspaceweaver.types.live_simulation_state

        out["LiveSimulationState"] = (
            aws_sdk_simspaceweaver.types.live_simulation_state.serialize_json(
                value["live_simulation_state"]
            )
        )
    if "maximum_duration" in value:
        out["MaximumDuration"] = value["maximum_duration"]
    if "snapshot_s3_location" in value:
        import aws_sdk_simspaceweaver.types.s3_location

        out["SnapshotS3Location"] = (
            aws_sdk_simspaceweaver.types.s3_location.serialize_json(
                value["snapshot_s3_location"]
            )
        )
    if "start_error" in value:
        out["StartError"] = value["start_error"]
    return out


def deserialize_json(data: dict) -> DescribeSimulationOutput:
    out: DescribeSimulationOutput = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "ExecutionId" in data:
        out["execution_id"] = data["ExecutionId"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    if "CreationTime" in data:
        import aws_sdk_simspaceweaver.types.timestamp

        out["creation_time"] = aws_sdk_simspaceweaver.types.timestamp.deserialize_json(
            data["CreationTime"]
        )
    if "Status" in data:
        out["status"] = data["Status"]
    if "TargetStatus" in data:
        out["target_status"] = data["TargetStatus"]
    if "SchemaS3Location" in data:
        import aws_sdk_simspaceweaver.types.s3_location

        out["schema_s3_location"] = (
            aws_sdk_simspaceweaver.types.s3_location.deserialize_json(
                data["SchemaS3Location"]
            )
        )
    if "SchemaError" in data:
        out["schema_error"] = data["SchemaError"]
    if "LoggingConfiguration" in data:
        import aws_sdk_simspaceweaver.types.logging_configuration

        out["logging_configuration"] = (
            aws_sdk_simspaceweaver.types.logging_configuration.deserialize_json(
                data["LoggingConfiguration"]
            )
        )
    if "LiveSimulationState" in data:
        import aws_sdk_simspaceweaver.types.live_simulation_state

        out["live_simulation_state"] = (
            aws_sdk_simspaceweaver.types.live_simulation_state.deserialize_json(
                data["LiveSimulationState"]
            )
        )
    if "MaximumDuration" in data:
        out["maximum_duration"] = data["MaximumDuration"]
    if "SnapshotS3Location" in data:
        import aws_sdk_simspaceweaver.types.s3_location

        out["snapshot_s3_location"] = (
            aws_sdk_simspaceweaver.types.s3_location.deserialize_json(
                data["SnapshotS3Location"]
            )
        )
    if "StartError" in data:
        out["start_error"] = data["StartError"]
    return out
