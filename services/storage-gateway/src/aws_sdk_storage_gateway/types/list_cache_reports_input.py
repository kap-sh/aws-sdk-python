"""Generated from Smithy shape ``com.amazonaws.storagegateway#ListCacheReportsInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.marker


class ListCacheReportsInput(TypedDict):
    marker: NotRequired["aws_sdk_storage_gateway.types.marker.Marker"]
    """<p>Opaque pagination token returned from a previous <code>ListCacheReports</code> operation. If present, <code>Marker</code> specifies where to continue the list from after a previous call to <code>ListCacheReports</code>. Optional.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListCacheReportsInput) -> dict:
    out: dict = {}
    if "marker" in value:
        out["Marker"] = value["marker"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListCacheReportsInput:
    out: ListCacheReportsInput = {}  # type: ignore[typeddict-item]
    if "Marker" in data:
        out["marker"] = data["Marker"]
    return out
