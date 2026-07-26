"""Generated from Smithy shape ``com.amazonaws.personalize#ListDatasetsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_personalize.types.datasets
    import capo_personalize.types.next_token


class ListDatasetsResponse(TypedDict, closed=True):
    datasets: NotRequired["capo_personalize.types.datasets.Datasets"]
    """<p>An array of <code>Dataset</code> objects. Each object provides metadata information.</p>"""
    next_token: NotRequired["capo_personalize.types.next_token.NextToken"]
    """<p>A token for getting the next set of datasets (if they exist).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDatasetsResponse) -> dict:
    out: dict = {}
    if "datasets" in value:
        import capo_personalize.types.datasets

        out["datasets"] = capo_personalize.types.datasets.serialize_aws_json_1_1(
            value["datasets"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDatasetsResponse:
    out: ListDatasetsResponse = {}  # type: ignore[typeddict-item]
    if "datasets" in data:
        import capo_personalize.types.datasets

        out["datasets"] = capo_personalize.types.datasets.deserialize_aws_json_1_1(
            data["datasets"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
