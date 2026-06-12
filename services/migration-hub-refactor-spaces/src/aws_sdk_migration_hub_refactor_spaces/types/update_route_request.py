"""Generated from Smithy shape ``com.amazonaws.migrationhubrefactorspaces#UpdateRouteRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_migration_hub_refactor_spaces.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_migration_hub_refactor_spaces.types.application_id
    import aws_sdk_migration_hub_refactor_spaces.types.environment_id
    import aws_sdk_migration_hub_refactor_spaces.types.route_activation_state
    import aws_sdk_migration_hub_refactor_spaces.types.route_id


class UpdateRouteRequest(TypedDict):
    environment_identifier: (
        "aws_sdk_migration_hub_refactor_spaces.types.environment_id.EnvironmentId"
    )
    """<p> The ID of the environment in which the route is being updated. </p>"""
    application_identifier: (
        "aws_sdk_migration_hub_refactor_spaces.types.application_id.ApplicationId"
    )
    """<p> The ID of the application within which the route is being updated. </p>"""
    route_identifier: "aws_sdk_migration_hub_refactor_spaces.types.route_id.RouteId"
    """<p> The unique identifier of the route to update. </p>"""
    activation_state: "aws_sdk_migration_hub_refactor_spaces.types.route_activation_state.RouteActivationState"
    """<p> If set to <code>ACTIVE</code>, traffic is forwarded to this route’s service after the route is updated. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRouteRequest) -> dict:
    out: dict = {}
    out["ActivationState"] = value["activation_state"]
    return out


def deserialize_json(data: dict) -> UpdateRouteRequest:
    out: UpdateRouteRequest = {}  # type: ignore[typeddict-item]
    if "ActivationState" in data:
        out["activation_state"] = data["ActivationState"]
    else:
        raise DeserializationError("UpdateRouteRequest.activation_state required")
    return out
