"""Generated from Smithy shape ``com.amazonaws.migrationhubrefactorspaces#DefaultRouteInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_migration_hub_refactor_spaces.types.route_activation_state


class DefaultRouteInput(TypedDict):
    activation_state: NotRequired[
        "aws_sdk_migration_hub_refactor_spaces.types.route_activation_state.RouteActivationState"
    ]
    """<p>If set to <code>ACTIVE</code>, traffic is forwarded to this route’s service after the route is created. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DefaultRouteInput) -> dict:
    out: dict = {}
    if "activation_state" in value:
        out["ActivationState"] = value["activation_state"]
    return out


def deserialize_json(data: dict) -> DefaultRouteInput:
    out: DefaultRouteInput = {}  # type: ignore[typeddict-item]
    if "ActivationState" in data:
        out["activation_state"] = data["ActivationState"]
    return out
