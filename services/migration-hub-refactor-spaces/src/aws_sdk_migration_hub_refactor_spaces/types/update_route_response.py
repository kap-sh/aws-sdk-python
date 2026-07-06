"""Generated from Smithy shape ``com.amazonaws.migrationhubrefactorspaces#UpdateRouteResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_migration_hub_refactor_spaces.types.application_id
    import aws_sdk_migration_hub_refactor_spaces.types.resource_arn
    import aws_sdk_migration_hub_refactor_spaces.types.route_id
    import aws_sdk_migration_hub_refactor_spaces.types.route_state
    import aws_sdk_migration_hub_refactor_spaces.types.service_id
    import aws_sdk_migration_hub_refactor_spaces.types.timestamp


class UpdateRouteResponse(TypedDict, closed=True):
    route_id: NotRequired[
        "aws_sdk_migration_hub_refactor_spaces.types.route_id.RouteId"
    ]
    """<p> The unique identifier of the route. </p>"""
    arn: NotRequired[
        "aws_sdk_migration_hub_refactor_spaces.types.resource_arn.ResourceArn"
    ]
    r"""<p> The Amazon Resource Name (ARN) of the route. The format for this ARN is <code>arn:aws:refactor-spaces:<i>region</i>:<i>account-id</i>:<i>resource-type/resource-id</i> </code>. For more information about ARNs, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i>. </p>"""
    service_id: NotRequired[
        "aws_sdk_migration_hub_refactor_spaces.types.service_id.ServiceId"
    ]
    """<p> The ID of service in which the route was created. Traffic that matches this route is forwarded to this service. </p>"""
    application_id: NotRequired[
        "aws_sdk_migration_hub_refactor_spaces.types.application_id.ApplicationId"
    ]
    """<p> The ID of the application in which the route is being updated. </p>"""
    state: NotRequired[
        "aws_sdk_migration_hub_refactor_spaces.types.route_state.RouteState"
    ]
    """<p> The current state of the route. </p>"""
    last_updated_time: NotRequired[
        "aws_sdk_migration_hub_refactor_spaces.types.timestamp.Timestamp"
    ]
    """<p> A timestamp that indicates when the route was last updated. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRouteResponse) -> dict:
    out: dict = {}
    if "route_id" in value:
        out["RouteId"] = value["route_id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "service_id" in value:
        out["ServiceId"] = value["service_id"]
    if "application_id" in value:
        out["ApplicationId"] = value["application_id"]
    if "state" in value:
        out["State"] = value["state"]
    if "last_updated_time" in value:
        import aws_sdk_migration_hub_refactor_spaces.types.timestamp

        out["LastUpdatedTime"] = (
            aws_sdk_migration_hub_refactor_spaces.types.timestamp.serialize_json(
                value["last_updated_time"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateRouteResponse:
    out: UpdateRouteResponse = {}  # type: ignore[typeddict-item]
    if "RouteId" in data:
        out["route_id"] = data["RouteId"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "ServiceId" in data:
        out["service_id"] = data["ServiceId"]
    if "ApplicationId" in data:
        out["application_id"] = data["ApplicationId"]
    if "State" in data:
        out["state"] = data["State"]
    if "LastUpdatedTime" in data:
        import aws_sdk_migration_hub_refactor_spaces.types.timestamp

        out["last_updated_time"] = (
            aws_sdk_migration_hub_refactor_spaces.types.timestamp.deserialize_json(
                data["LastUpdatedTime"]
            )
        )
    return out
