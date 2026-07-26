"""Generated from Smithy shape ``com.amazonaws.emr#GetSessionEndpointInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr.types.cluster_id
    import capo_emr.types.session_id


class GetSessionEndpointInput(TypedDict, closed=True):
    cluster_id: NotRequired["capo_emr.types.cluster_id.ClusterId"]
    """<p>The ID of the cluster that the session belongs to.</p>"""
    session_id: NotRequired["capo_emr.types.session_id.SessionId"]
    """<p>The ID of the session.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetSessionEndpointInput) -> dict:
    out: dict = {}
    if "cluster_id" in value:
        out["ClusterId"] = value["cluster_id"]
    if "session_id" in value:
        out["SessionId"] = value["session_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetSessionEndpointInput:
    out: GetSessionEndpointInput = {}  # type: ignore[typeddict-item]
    if "ClusterId" in data:
        out["cluster_id"] = data["ClusterId"]
    if "SessionId" in data:
        out["session_id"] = data["SessionId"]
    return out
