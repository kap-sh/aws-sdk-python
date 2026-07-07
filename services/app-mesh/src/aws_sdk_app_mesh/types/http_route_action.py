"""Generated from Smithy shape ``com.amazonaws.appmesh#HttpRouteAction``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_app_mesh.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.weighted_targets


class HttpRouteAction(TypedDict, closed=True):
    weighted_targets: "aws_sdk_app_mesh.types.weighted_targets.WeightedTargets"
    """<p>An object that represents the targets that traffic is routed to when a request matches the route.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HttpRouteAction) -> dict:
    out: dict = {}
    import aws_sdk_app_mesh.types.weighted_targets

    out["weightedTargets"] = aws_sdk_app_mesh.types.weighted_targets.serialize_json(
        value["weighted_targets"]
    )
    return out


def deserialize_json(data: dict) -> HttpRouteAction:
    out: HttpRouteAction = {}  # type: ignore[typeddict-item]
    if "weightedTargets" in data:
        import aws_sdk_app_mesh.types.weighted_targets

        out["weighted_targets"] = (
            aws_sdk_app_mesh.types.weighted_targets.deserialize_json(
                data["weightedTargets"]
            )
        )
    else:
        raise DeserializationError("HttpRouteAction.weighted_targets required")
    return out
