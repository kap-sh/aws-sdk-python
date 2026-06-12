"""Generated from Smithy shape ``com.amazonaws.xray#ErrorStatistics``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_xray.types.nullable_long


class ErrorStatistics(TypedDict):
    throttle_count: NotRequired["aws_sdk_xray.types.nullable_long.NullableLong"]
    """<p>The number of requests that failed with a 429 throttling status code.</p>"""
    other_count: NotRequired["aws_sdk_xray.types.nullable_long.NullableLong"]
    """<p>The number of requests that failed with untracked 4xx Client Error status codes.</p>"""
    total_count: NotRequired["aws_sdk_xray.types.nullable_long.NullableLong"]
    """<p>The total number of requests that failed with a 4xx Client Error status code.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ErrorStatistics) -> dict:
    out: dict = {}
    if "throttle_count" in value:
        out["ThrottleCount"] = value["throttle_count"]
    if "other_count" in value:
        out["OtherCount"] = value["other_count"]
    if "total_count" in value:
        out["TotalCount"] = value["total_count"]
    return out


def deserialize_json(data: dict) -> ErrorStatistics:
    out: ErrorStatistics = {}  # type: ignore[typeddict-item]
    if "ThrottleCount" in data:
        out["throttle_count"] = data["ThrottleCount"]
    if "OtherCount" in data:
        out["other_count"] = data["OtherCount"]
    if "TotalCount" in data:
        out["total_count"] = data["TotalCount"]
    return out
