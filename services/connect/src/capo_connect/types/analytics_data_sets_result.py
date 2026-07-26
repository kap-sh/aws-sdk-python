"""Generated from Smithy shape ``com.amazonaws.connect#AnalyticsDataSetsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.data_set_id
    import capo_connect.types.string


class AnalyticsDataSetsResult(TypedDict, closed=True):
    data_set_id: NotRequired["capo_connect.types.data_set_id.DataSetId"]
    """<p>The identifier of the dataset.</p>"""
    data_set_name: NotRequired["capo_connect.types.string.String"]
    """<p>The name of the dataset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnalyticsDataSetsResult) -> dict:
    out: dict = {}
    if "data_set_id" in value:
        out["DataSetId"] = value["data_set_id"]
    if "data_set_name" in value:
        out["DataSetName"] = value["data_set_name"]
    return out


def deserialize_json(data: dict) -> AnalyticsDataSetsResult:
    out: AnalyticsDataSetsResult = {}  # type: ignore[typeddict-item]
    if "DataSetId" in data:
        out["data_set_id"] = data["DataSetId"]
    if "DataSetName" in data:
        out["data_set_name"] = data["DataSetName"]
    return out
