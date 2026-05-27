"""Generated from Smithy shape ``com.amazonaws.eks#ClientStat``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_eks.types.integer
    import aws_sdk_eks.types.string
    import aws_sdk_eks.types.timestamp


class ClientStat(TypedDict):
    user_agent: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The user agent of the Kubernetes client using the deprecated resource.</p>"""
    number_of_requests_last30_days: "aws_sdk_eks.types.integer.Integer"
    """<p>The number of requests from the Kubernetes client seen over the last 30 days.</p>"""
    last_request_time: NotRequired["aws_sdk_eks.types.timestamp.Timestamp"]
    """<p>The timestamp of the last request seen from the Kubernetes client.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ClientStat) -> dict:
    out: dict = {}
    if "user_agent" in value:
        out["userAgent"] = value["user_agent"]
    out["numberOfRequestsLast30Days"] = value.get("number_of_requests_last30_days", 0)
    if "last_request_time" in value:
        import aws_sdk_eks.types.timestamp

        out["lastRequestTime"] = aws_sdk_eks.types.timestamp.serialize_json(
            value["last_request_time"]
        )
    return out


def deserialize_json(data: dict) -> ClientStat:
    out: ClientStat = {}  # type: ignore[typeddict-item]
    if "userAgent" in data:
        out["user_agent"] = data["userAgent"]
    if "numberOfRequestsLast30Days" in data:
        out["number_of_requests_last30_days"] = data["numberOfRequestsLast30Days"]
    else:
        out["number_of_requests_last30_days"] = 0
    if "lastRequestTime" in data:
        import aws_sdk_eks.types.timestamp

        out["last_request_time"] = aws_sdk_eks.types.timestamp.deserialize_json(
            data["lastRequestTime"]
        )
    return out
