"""Generated from Smithy shape ``com.amazonaws.gamelift#GetComputeAccessOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.aws_credentials
    import aws_sdk_gamelift.types.compute_arn
    import aws_sdk_gamelift.types.compute_name_or_arn
    import aws_sdk_gamelift.types.container_identifier_list
    import aws_sdk_gamelift.types.fleet_arn
    import aws_sdk_gamelift.types.fleet_id_or_arn
    import aws_sdk_gamelift.types.session_target


class GetComputeAccessOutput(TypedDict):
    fleet_id: NotRequired["aws_sdk_gamelift.types.fleet_id_or_arn.FleetIdOrArn"]
    """<p>The ID of the fleet that holds the compute resource to be accessed.</p>"""
    fleet_arn: NotRequired["aws_sdk_gamelift.types.fleet_arn.FleetArn"]
    r"""<p>The Amazon Resource Name (<a href=\"https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html\">ARN</a>) that is assigned to a Amazon GameLift Servers fleet resource and uniquely identifies it. ARNs are unique across all Regions. Format is <code>arn:aws:gamelift:<region>::fleet/fleet-a1234567-b8c9-0d1e-2fa3-b45c6d7e8912</code>.</p>"""
    compute_name: NotRequired[
        "aws_sdk_gamelift.types.compute_name_or_arn.ComputeNameOrArn"
    ]
    """<p>The identifier of the compute resource to be accessed. This value might be either a compute name or an instance ID.</p>"""
    compute_arn: NotRequired["aws_sdk_gamelift.types.compute_arn.ComputeArn"]
    r"""<p>The Amazon Resource Name (<a href=\"https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html\">ARN</a>) that is assigned to an Amazon GameLift Servers compute resource and uniquely identifies it. ARNs are unique across all Regions. Format is <code>arn:aws:gamelift:<region>::compute/compute-a1234567-b8c9-0d1e-2fa3-b45c6d7e8912</code>.</p>"""
    credentials: NotRequired["aws_sdk_gamelift.types.aws_credentials.AwsCredentials"]
    """<p>A set of temporary Amazon Web Services credentials for use when connecting to the compute resource with Amazon EC2 Systems Manager (SSM).</p>"""
    target: NotRequired["aws_sdk_gamelift.types.session_target.SessionTarget"]
    """<p>The instance ID where the compute resource is running.</p>"""
    container_identifiers: NotRequired[
        "aws_sdk_gamelift.types.container_identifier_list.ContainerIdentifierList"
    ]
    """<p>For a managed container fleet, a list of containers on the compute. Use the container runtime ID with Docker commands to connect to a specific container. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetComputeAccessOutput) -> dict:
    out: dict = {}
    if "fleet_id" in value:
        out["FleetId"] = value["fleet_id"]
    if "fleet_arn" in value:
        out["FleetArn"] = value["fleet_arn"]
    if "compute_name" in value:
        out["ComputeName"] = value["compute_name"]
    if "compute_arn" in value:
        out["ComputeArn"] = value["compute_arn"]
    if "credentials" in value:
        import aws_sdk_gamelift.types.aws_credentials

        out["Credentials"] = (
            aws_sdk_gamelift.types.aws_credentials.serialize_aws_json_1_1(
                value["credentials"]
            )
        )
    if "target" in value:
        out["Target"] = value["target"]
    if "container_identifiers" in value:
        import aws_sdk_gamelift.types.container_identifier_list

        out["ContainerIdentifiers"] = (
            aws_sdk_gamelift.types.container_identifier_list.serialize_aws_json_1_1(
                value["container_identifiers"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetComputeAccessOutput:
    out: GetComputeAccessOutput = {}  # type: ignore[typeddict-item]
    if "FleetId" in data:
        out["fleet_id"] = data["FleetId"]
    if "FleetArn" in data:
        out["fleet_arn"] = data["FleetArn"]
    if "ComputeName" in data:
        out["compute_name"] = data["ComputeName"]
    if "ComputeArn" in data:
        out["compute_arn"] = data["ComputeArn"]
    if "Credentials" in data:
        import aws_sdk_gamelift.types.aws_credentials

        out["credentials"] = (
            aws_sdk_gamelift.types.aws_credentials.deserialize_aws_json_1_1(
                data["Credentials"]
            )
        )
    if "Target" in data:
        out["target"] = data["Target"]
    if "ContainerIdentifiers" in data:
        import aws_sdk_gamelift.types.container_identifier_list

        out["container_identifiers"] = (
            aws_sdk_gamelift.types.container_identifier_list.deserialize_aws_json_1_1(
                data["ContainerIdentifiers"]
            )
        )
    return out
