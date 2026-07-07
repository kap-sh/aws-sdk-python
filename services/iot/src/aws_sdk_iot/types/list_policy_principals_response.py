"""Generated from Smithy shape ``com.amazonaws.iot#ListPolicyPrincipalsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.marker
    import aws_sdk_iot.types.principals


class ListPolicyPrincipalsResponse(TypedDict, closed=True):
    principals: NotRequired["aws_sdk_iot.types.principals.Principals"]
    """<p>The descriptions of the principals.</p>"""
    next_marker: NotRequired["aws_sdk_iot.types.marker.Marker"]
    """<p>The marker for the next set of results, or null if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPolicyPrincipalsResponse) -> dict:
    out: dict = {}
    if "principals" in value:
        import aws_sdk_iot.types.principals

        out["principals"] = aws_sdk_iot.types.principals.serialize_json(
            value["principals"]
        )
    if "next_marker" in value:
        out["nextMarker"] = value["next_marker"]
    return out


def deserialize_json(data: dict) -> ListPolicyPrincipalsResponse:
    out: ListPolicyPrincipalsResponse = {}  # type: ignore[typeddict-item]
    if "principals" in data:
        import aws_sdk_iot.types.principals

        out["principals"] = aws_sdk_iot.types.principals.deserialize_json(
            data["principals"]
        )
    if "nextMarker" in data:
        out["next_marker"] = data["nextMarker"]
    return out
