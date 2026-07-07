"""Generated from Smithy shape ``com.amazonaws.kms#ListKeysRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kms.types.limit_type
    import aws_sdk_kms.types.marker_type


class ListKeysRequest(TypedDict, closed=True):
    limit: NotRequired["aws_sdk_kms.types.limit_type.LimitType"]
    """<p>Use this parameter to specify the maximum number of items to return. When this value is present, KMS does not return more than the specified number of items, but it might return fewer.</p> <p>This value is optional. If you include a value, it must be between 1 and 1000, inclusive. If you do not include a value, it defaults to 100.</p>"""
    marker: NotRequired["aws_sdk_kms.types.marker_type.MarkerType"]
    """<p>Use this parameter in a subsequent request after you receive a response with truncated results. Set it to the value of <code>NextMarker</code> from the truncated response you just received.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListKeysRequest) -> dict:
    out: dict = {}
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "marker" in value:
        out["Marker"] = value["marker"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListKeysRequest:
    out: ListKeysRequest = {}  # type: ignore[typeddict-item]
    if "Limit" in data:
        out["limit"] = data["Limit"]
    if "Marker" in data:
        out["marker"] = data["Marker"]
    return out
