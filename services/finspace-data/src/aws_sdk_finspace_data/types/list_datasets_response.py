"""Generated from Smithy shape ``com.amazonaws.finspacedata#ListDatasetsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_finspace_data.types.dataset_list
    import aws_sdk_finspace_data.types.pagination_token


class ListDatasetsResponse(TypedDict):
    datasets: NotRequired["aws_sdk_finspace_data.types.dataset_list.DatasetList"]
    """<p>List of Datasets.</p>"""
    next_token: NotRequired[
        "aws_sdk_finspace_data.types.pagination_token.PaginationToken"
    ]
    """<p>A token that indicates where a results page should begin.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDatasetsResponse) -> dict:
    out: dict = {}
    if "datasets" in value:
        import aws_sdk_finspace_data.types.dataset_list

        out["datasets"] = aws_sdk_finspace_data.types.dataset_list.serialize_json(
            value["datasets"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDatasetsResponse:
    out: ListDatasetsResponse = {}  # type: ignore[typeddict-item]
    if "datasets" in data:
        import aws_sdk_finspace_data.types.dataset_list

        out["datasets"] = aws_sdk_finspace_data.types.dataset_list.deserialize_json(
            data["datasets"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
