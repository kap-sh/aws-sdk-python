"""Generated from Smithy shape ``com.amazonaws.iot#ListTargetsForPolicyResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.marker
    import aws_sdk_iot.types.policy_targets


class ListTargetsForPolicyResponse(TypedDict):
    targets: NotRequired["aws_sdk_iot.types.policy_targets.PolicyTargets"]
    """<p>The policy targets.</p>"""
    next_marker: NotRequired["aws_sdk_iot.types.marker.Marker"]
    """<p>A marker used to get the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTargetsForPolicyResponse) -> dict:
    out: dict = {}
    if "targets" in value:
        import aws_sdk_iot.types.policy_targets

        out["targets"] = aws_sdk_iot.types.policy_targets.serialize_json(
            value["targets"]
        )
    if "next_marker" in value:
        out["nextMarker"] = value["next_marker"]
    return out


def deserialize_json(data: dict) -> ListTargetsForPolicyResponse:
    out: ListTargetsForPolicyResponse = {}  # type: ignore[typeddict-item]
    if "targets" in data:
        import aws_sdk_iot.types.policy_targets

        out["targets"] = aws_sdk_iot.types.policy_targets.deserialize_json(
            data["targets"]
        )
    if "nextMarker" in data:
        out["next_marker"] = data["nextMarker"]
    return out
