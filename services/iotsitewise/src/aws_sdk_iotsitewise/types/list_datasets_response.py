"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ListDatasetsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.dataset_summaries
    import aws_sdk_iotsitewise.types.next_token


class ListDatasetsResponse(TypedDict):
    dataset_summaries: "aws_sdk_iotsitewise.types.dataset_summaries.DatasetSummaries"
    """<p>A list that summarizes the dataset response.</p>"""
    next_token: NotRequired["aws_sdk_iotsitewise.types.next_token.NextToken"]
    """<p>The token for the next set of results, or null if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDatasetsResponse) -> dict:
    out: dict = {}
    import aws_sdk_iotsitewise.types.dataset_summaries

    out["datasetSummaries"] = (
        aws_sdk_iotsitewise.types.dataset_summaries.serialize_json(
            value["dataset_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDatasetsResponse:
    out: ListDatasetsResponse = {}  # type: ignore[typeddict-item]
    if "datasetSummaries" in data:
        import aws_sdk_iotsitewise.types.dataset_summaries

        out["dataset_summaries"] = (
            aws_sdk_iotsitewise.types.dataset_summaries.deserialize_json(
                data["datasetSummaries"]
            )
        )
    else:
        raise DeserializationError("ListDatasetsResponse.dataset_summaries required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
