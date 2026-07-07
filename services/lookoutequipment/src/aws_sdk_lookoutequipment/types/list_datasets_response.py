"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#ListDatasetsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lookoutequipment.types.dataset_summaries
    import aws_sdk_lookoutequipment.types.next_token


class ListDatasetsResponse(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_lookoutequipment.types.next_token.NextToken"]
    """<p> An opaque pagination token indicating where to continue the listing of datasets. </p>"""
    dataset_summaries: NotRequired[
        "aws_sdk_lookoutequipment.types.dataset_summaries.DatasetSummaries"
    ]
    """<p>Provides information about the specified dataset, including creation time, dataset ARN, and status. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListDatasetsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "dataset_summaries" in value:
        import aws_sdk_lookoutequipment.types.dataset_summaries

        out["DatasetSummaries"] = (
            aws_sdk_lookoutequipment.types.dataset_summaries.serialize_aws_json_1_0(
                value["dataset_summaries"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListDatasetsResponse:
    out: ListDatasetsResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "DatasetSummaries" in data:
        import aws_sdk_lookoutequipment.types.dataset_summaries

        out["dataset_summaries"] = (
            aws_sdk_lookoutequipment.types.dataset_summaries.deserialize_aws_json_1_0(
                data["DatasetSummaries"]
            )
        )
    return out
