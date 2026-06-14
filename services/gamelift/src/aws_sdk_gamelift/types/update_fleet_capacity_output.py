"""Generated from Smithy shape ``com.amazonaws.gamelift#UpdateFleetCapacityOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.fleet_arn
    import aws_sdk_gamelift.types.fleet_id
    import aws_sdk_gamelift.types.location_string_model
    import aws_sdk_gamelift.types.managed_capacity_configuration


class UpdateFleetCapacityOutput(TypedDict):
    fleet_id: NotRequired["aws_sdk_gamelift.types.fleet_id.FleetId"]
    """<p>A unique identifier for the fleet that was updated.</p>"""
    fleet_arn: NotRequired["aws_sdk_gamelift.types.fleet_arn.FleetArn"]
    r"""<p>The Amazon Resource Name (<a href=\"https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html\">ARN</a>) that is assigned to a Amazon GameLift Servers fleet resource and uniquely identifies it. ARNs are unique across all Regions. Format is <code>arn:aws:gamelift:<region>::fleet/fleet-a1234567-b8c9-0d1e-2fa3-b45c6d7e8912</code>. </p>"""
    location: NotRequired[
        "aws_sdk_gamelift.types.location_string_model.LocationStringModel"
    ]
    """<p>The remote location being updated, expressed as an Amazon Web Services Region code, such as <code>us-west-2</code>.</p>"""
    managed_capacity_configuration: NotRequired[
        "aws_sdk_gamelift.types.managed_capacity_configuration.ManagedCapacityConfiguration"
    ]
    """<p>Configuration for Amazon GameLift Servers-managed capacity scaling options.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateFleetCapacityOutput) -> dict:
    out: dict = {}
    if "fleet_id" in value:
        out["FleetId"] = value["fleet_id"]
    if "fleet_arn" in value:
        out["FleetArn"] = value["fleet_arn"]
    if "location" in value:
        out["Location"] = value["location"]
    if "managed_capacity_configuration" in value:
        import aws_sdk_gamelift.types.managed_capacity_configuration

        out["ManagedCapacityConfiguration"] = (
            aws_sdk_gamelift.types.managed_capacity_configuration.serialize_aws_json_1_1(
                value["managed_capacity_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateFleetCapacityOutput:
    out: UpdateFleetCapacityOutput = {}  # type: ignore[typeddict-item]
    if "FleetId" in data:
        out["fleet_id"] = data["FleetId"]
    if "FleetArn" in data:
        out["fleet_arn"] = data["FleetArn"]
    if "Location" in data:
        out["location"] = data["Location"]
    if "ManagedCapacityConfiguration" in data:
        import aws_sdk_gamelift.types.managed_capacity_configuration

        out["managed_capacity_configuration"] = (
            aws_sdk_gamelift.types.managed_capacity_configuration.deserialize_aws_json_1_1(
                data["ManagedCapacityConfiguration"]
            )
        )
    return out
