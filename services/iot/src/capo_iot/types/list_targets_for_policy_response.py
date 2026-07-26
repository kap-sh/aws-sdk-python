"""Generated from Smithy shape ``com.amazonaws.iot#ListTargetsForPolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.marker
    import capo_iot.types.policy_targets


class ListTargetsForPolicyResponse(TypedDict, closed=True):
    targets: NotRequired["capo_iot.types.policy_targets.PolicyTargets"]
    """<p>The policy targets.</p>"""
    next_marker: NotRequired["capo_iot.types.marker.Marker"]
    """<p>A marker used to get the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTargetsForPolicyResponse) -> dict:
    out: dict = {}
    if "targets" in value:
        import capo_iot.types.policy_targets

        out["targets"] = capo_iot.types.policy_targets.serialize_json(value["targets"])
    if "next_marker" in value:
        out["nextMarker"] = value["next_marker"]
    return out


def deserialize_json(data: dict) -> ListTargetsForPolicyResponse:
    out: ListTargetsForPolicyResponse = {}  # type: ignore[typeddict-item]
    if "targets" in data:
        import capo_iot.types.policy_targets

        out["targets"] = capo_iot.types.policy_targets.deserialize_json(data["targets"])
    if "nextMarker" in data:
        out["next_marker"] = data["nextMarker"]
    return out
