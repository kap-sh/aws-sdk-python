"""Generated from Smithy shape ``com.amazonaws.migrationhubrefactorspaces#GetRouteRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_migration_hub_refactor_spaces.types.application_id
    import aws_sdk_migration_hub_refactor_spaces.types.environment_id
    import aws_sdk_migration_hub_refactor_spaces.types.route_id


class GetRouteRequest(TypedDict, closed=True):
    environment_identifier: (
        "aws_sdk_migration_hub_refactor_spaces.types.environment_id.EnvironmentId"
    )
    """<p>The ID of the environment.</p>"""
    application_identifier: (
        "aws_sdk_migration_hub_refactor_spaces.types.application_id.ApplicationId"
    )
    """<p>The ID of the application. </p>"""
    route_identifier: "aws_sdk_migration_hub_refactor_spaces.types.route_id.RouteId"
    """<p>The ID of the route.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRouteRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetRouteRequest:
    out: GetRouteRequest = {}  # type: ignore[typeddict-item]
    return out
