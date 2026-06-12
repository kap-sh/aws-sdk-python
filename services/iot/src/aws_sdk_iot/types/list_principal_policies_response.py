"""Generated from Smithy shape ``com.amazonaws.iot#ListPrincipalPoliciesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.marker
    import aws_sdk_iot.types.policies


class ListPrincipalPoliciesResponse(TypedDict):
    policies: NotRequired["aws_sdk_iot.types.policies.Policies"]
    """<p>The policies.</p>"""
    next_marker: NotRequired["aws_sdk_iot.types.marker.Marker"]
    """<p>The marker for the next set of results, or null if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPrincipalPoliciesResponse) -> dict:
    out: dict = {}
    if "policies" in value:
        import aws_sdk_iot.types.policies

        out["policies"] = aws_sdk_iot.types.policies.serialize_json(value["policies"])
    if "next_marker" in value:
        out["nextMarker"] = value["next_marker"]
    return out


def deserialize_json(data: dict) -> ListPrincipalPoliciesResponse:
    out: ListPrincipalPoliciesResponse = {}  # type: ignore[typeddict-item]
    if "policies" in data:
        import aws_sdk_iot.types.policies

        out["policies"] = aws_sdk_iot.types.policies.deserialize_json(data["policies"])
    if "nextMarker" in data:
        out["next_marker"] = data["nextMarker"]
    return out
