"""Generated from Smithy shape ``com.amazonaws.rekognition#ListDatasetLabelsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_rekognition.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.dataset_arn
    import aws_sdk_rekognition.types.extended_pagination_token
    import aws_sdk_rekognition.types.list_dataset_labels_page_size


class ListDatasetLabelsRequest(TypedDict, closed=True):
    dataset_arn: "aws_sdk_rekognition.types.dataset_arn.DatasetArn"
    """<p> The Amazon Resource Name (ARN) of the dataset that you want to use. </p>"""
    next_token: NotRequired[
        "aws_sdk_rekognition.types.extended_pagination_token.ExtendedPaginationToken"
    ]
    """<p>If the previous response was incomplete (because there is more results to retrieve), Amazon Rekognition Custom Labels returns a pagination token in the response. You can use this pagination token to retrieve the next set of results. </p>"""
    max_results: NotRequired[
        "aws_sdk_rekognition.types.list_dataset_labels_page_size.ListDatasetLabelsPageSize"
    ]
    """<p>The maximum number of results to return per paginated call. The largest value you can specify is 100. If you specify a value greater than 100, a ValidationException error occurs. The default value is 100. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDatasetLabelsRequest) -> dict:
    out: dict = {}
    out["DatasetArn"] = value["dataset_arn"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDatasetLabelsRequest:
    out: ListDatasetLabelsRequest = {}  # type: ignore[typeddict-item]
    if "DatasetArn" in data:
        out["dataset_arn"] = data["DatasetArn"]
    else:
        raise DeserializationError("ListDatasetLabelsRequest.dataset_arn required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
