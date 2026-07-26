"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#ListDatasetsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lookoutequipment.types.dataset_name
    import capo_lookoutequipment.types.max_results
    import capo_lookoutequipment.types.next_token


class ListDatasetsRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_lookoutequipment.types.next_token.NextToken"]
    """<p> An opaque pagination token indicating where to continue the listing of datasets. </p>"""
    max_results: NotRequired["capo_lookoutequipment.types.max_results.MaxResults"]
    """<p> Specifies the maximum number of datasets to list. </p>"""
    dataset_name_begins_with: NotRequired[
        "capo_lookoutequipment.types.dataset_name.DatasetName"
    ]
    """<p>The beginning of the name of the datasets to be listed. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListDatasetsRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "dataset_name_begins_with" in value:
        out["DatasetNameBeginsWith"] = value["dataset_name_begins_with"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListDatasetsRequest:
    out: ListDatasetsRequest = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "DatasetNameBeginsWith" in data:
        out["dataset_name_begins_with"] = data["DatasetNameBeginsWith"]
    return out
