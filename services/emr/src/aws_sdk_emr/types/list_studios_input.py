"""Generated from Smithy shape ``com.amazonaws.emr#ListStudiosInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_emr.types.marker


class ListStudiosInput(TypedDict, closed=True):
    marker: NotRequired["aws_sdk_emr.types.marker.Marker"]
    """<p>The pagination token that indicates the set of results to retrieve.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListStudiosInput) -> dict:
    out: dict = {}
    if "marker" in value:
        out["Marker"] = value["marker"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListStudiosInput:
    out: ListStudiosInput = {}  # type: ignore[typeddict-item]
    if "Marker" in data:
        out["marker"] = data["Marker"]
    return out
