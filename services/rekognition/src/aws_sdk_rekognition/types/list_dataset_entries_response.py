"""Generated from Smithy shape ``com.amazonaws.rekognition#ListDatasetEntriesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.dataset_entries
    import aws_sdk_rekognition.types.extended_pagination_token


class ListDatasetEntriesResponse(TypedDict, closed=True):
    dataset_entries: NotRequired[
        "aws_sdk_rekognition.types.dataset_entries.DatasetEntries"
    ]
    """<p> A list of entries (images) in the dataset. </p>"""
    next_token: NotRequired[
        "aws_sdk_rekognition.types.extended_pagination_token.ExtendedPaginationToken"
    ]
    """<p>If the previous response was incomplete (because there is more results to retrieve), Amazon Rekognition Custom Labels returns a pagination token in the response. You can use this pagination token to retrieve the next set of results. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDatasetEntriesResponse) -> dict:
    out: dict = {}
    if "dataset_entries" in value:
        import aws_sdk_rekognition.types.dataset_entries

        out["DatasetEntries"] = (
            aws_sdk_rekognition.types.dataset_entries.serialize_aws_json_1_1(
                value["dataset_entries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDatasetEntriesResponse:
    out: ListDatasetEntriesResponse = {}  # type: ignore[typeddict-item]
    if "DatasetEntries" in data:
        import aws_sdk_rekognition.types.dataset_entries

        out["dataset_entries"] = (
            aws_sdk_rekognition.types.dataset_entries.deserialize_aws_json_1_1(
                data["DatasetEntries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
