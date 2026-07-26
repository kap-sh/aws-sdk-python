"""Generated from Smithy shape ``com.amazonaws.cognitosync#ListDatasetsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_sync.types.dataset_list
    import capo_cognito_sync.types.integer
    import capo_cognito_sync.types.string


class ListDatasetsResponse(TypedDict, closed=True):
    datasets: NotRequired["capo_cognito_sync.types.dataset_list.DatasetList"]
    """A set of datasets."""
    count: "capo_cognito_sync.types.integer.Integer"
    """Number of datasets returned."""
    next_token: NotRequired["capo_cognito_sync.types.string.String"]
    """A pagination token for obtaining the next page of results."""


# --- restJson1 ser/de ---
def serialize_json(value: ListDatasetsResponse) -> dict:
    out: dict = {}
    if "datasets" in value:
        import capo_cognito_sync.types.dataset_list

        out["Datasets"] = capo_cognito_sync.types.dataset_list.serialize_json(
            value["datasets"]
        )
    out["Count"] = value.get("count", 0)
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDatasetsResponse:
    out: ListDatasetsResponse = {}  # type: ignore[typeddict-item]
    if "Datasets" in data:
        import capo_cognito_sync.types.dataset_list

        out["datasets"] = capo_cognito_sync.types.dataset_list.deserialize_json(
            data["Datasets"]
        )
    if "Count" in data:
        out["count"] = data["Count"]
    else:
        out["count"] = 0
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
