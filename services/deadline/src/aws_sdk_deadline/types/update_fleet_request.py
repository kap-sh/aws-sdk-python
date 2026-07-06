"""Generated from Smithy shape ``com.amazonaws.deadline#UpdateFleetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_deadline.types.client_token
    import aws_sdk_deadline.types.description
    import aws_sdk_deadline.types.farm_id
    import aws_sdk_deadline.types.fleet_configuration
    import aws_sdk_deadline.types.fleet_id
    import aws_sdk_deadline.types.host_configuration
    import aws_sdk_deadline.types.iam_role_arn
    import aws_sdk_deadline.types.min_zero_max_integer
    import aws_sdk_deadline.types.resource_name


class UpdateFleetRequest(TypedDict, closed=True):
    farm_id: "aws_sdk_deadline.types.farm_id.FarmId"
    """<p>The farm ID to update.</p>"""
    fleet_id: "aws_sdk_deadline.types.fleet_id.FleetId"
    """<p>The fleet ID to update.</p>"""
    client_token: NotRequired["aws_sdk_deadline.types.client_token.ClientToken"]
    """<p>The unique token which the server uses to recognize retries of the same request.</p>"""
    display_name: NotRequired["aws_sdk_deadline.types.resource_name.ResourceName"]
    """<p>The display name of the fleet to update.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>"""
    description: NotRequired["aws_sdk_deadline.types.description.Description"]
    """<p>The description of the fleet to update.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>"""
    role_arn: NotRequired["aws_sdk_deadline.types.iam_role_arn.IamRoleArn"]
    """<p>The IAM role ARN that the fleet's workers assume while running jobs.</p>"""
    min_worker_count: NotRequired[
        "aws_sdk_deadline.types.min_zero_max_integer.MinZeroMaxInteger"
    ]
    """<p>The minimum number of workers in the fleet.</p>"""
    max_worker_count: NotRequired[
        "aws_sdk_deadline.types.min_zero_max_integer.MinZeroMaxInteger"
    ]
    """<p>The maximum number of workers in the fleet.</p> <p>Deadline Cloud limits the number of workers to less than or equal to the fleet's maximum worker count. The service maintains eventual consistency for the worker count. If you make multiple rapid calls to <code>CreateWorker</code> before the field updates, you might exceed your fleet's maximum worker count. For example, if your <code>maxWorkerCount</code> is 10 and you currently have 9 workers, making two quick <code>CreateWorker</code> calls might successfully create 2 workers instead of 1, resulting in 11 total workers.</p>"""
    configuration: NotRequired[
        "aws_sdk_deadline.types.fleet_configuration.FleetConfiguration"
    ]
    """<p>The fleet configuration to update.</p>"""
    host_configuration: NotRequired[
        "aws_sdk_deadline.types.host_configuration.HostConfiguration"
    ]
    """<p>Provides a script that runs as a worker is starting up that you can use to provide additional configuration for workers in your fleet.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateFleetRequest) -> dict:
    out: dict = {}
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "description" in value:
        out["description"] = value["description"]
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "min_worker_count" in value:
        out["minWorkerCount"] = value["min_worker_count"]
    if "max_worker_count" in value:
        out["maxWorkerCount"] = value["max_worker_count"]
    if "configuration" in value:
        import aws_sdk_deadline.types.fleet_configuration

        out["configuration"] = (
            aws_sdk_deadline.types.fleet_configuration.serialize_json(
                value["configuration"]
            )
        )
    if "host_configuration" in value:
        import aws_sdk_deadline.types.host_configuration

        out["hostConfiguration"] = (
            aws_sdk_deadline.types.host_configuration.serialize_json(
                value["host_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateFleetRequest:
    out: UpdateFleetRequest = {}  # type: ignore[typeddict-item]
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    if "description" in data:
        out["description"] = data["description"]
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    if "minWorkerCount" in data:
        out["min_worker_count"] = data["minWorkerCount"]
    if "maxWorkerCount" in data:
        out["max_worker_count"] = data["maxWorkerCount"]
    if "configuration" in data:
        import aws_sdk_deadline.types.fleet_configuration

        out["configuration"] = (
            aws_sdk_deadline.types.fleet_configuration.deserialize_json(
                data["configuration"]
            )
        )
    if "hostConfiguration" in data:
        import aws_sdk_deadline.types.host_configuration

        out["host_configuration"] = (
            aws_sdk_deadline.types.host_configuration.deserialize_json(
                data["hostConfiguration"]
            )
        )
    return out
