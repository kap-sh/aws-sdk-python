"""Generated from Smithy shape ``com.amazonaws.migrationhubrefactorspaces#DeleteRouteResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_migration_hub_refactor_spaces.types.application_id
    import aws_sdk_migration_hub_refactor_spaces.types.resource_arn
    import aws_sdk_migration_hub_refactor_spaces.types.route_id
    import aws_sdk_migration_hub_refactor_spaces.types.route_state
    import aws_sdk_migration_hub_refactor_spaces.types.service_id
    import aws_sdk_migration_hub_refactor_spaces.types.timestamp


class DeleteRouteResponse(TypedDict, closed=True):
    route_id: NotRequired[
        "aws_sdk_migration_hub_refactor_spaces.types.route_id.RouteId"
    ]
    """<p>The ID of the route to delete.</p>"""
    arn: NotRequired[
        "aws_sdk_migration_hub_refactor_spaces.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the route.</p>"""
    service_id: NotRequired[
        "aws_sdk_migration_hub_refactor_spaces.types.service_id.ServiceId"
    ]
    """<p>The ID of the service that the route belongs to.</p>"""
    application_id: NotRequired[
        "aws_sdk_migration_hub_refactor_spaces.types.application_id.ApplicationId"
    ]
    """<p>The ID of the application that the route belongs to.</p>"""
    state: NotRequired[
        "aws_sdk_migration_hub_refactor_spaces.types.route_state.RouteState"
    ]
    """<p>The current state of the route. </p>"""
    last_updated_time: NotRequired[
        "aws_sdk_migration_hub_refactor_spaces.types.timestamp.Timestamp"
    ]
    """<p>A timestamp that indicates when the route was last updated. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteRouteResponse) -> dict:
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


def deserialize_json(data: dict) -> DeleteRouteResponse:
    out: DeleteRouteResponse = {}  # type: ignore[typeddict-item]
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
