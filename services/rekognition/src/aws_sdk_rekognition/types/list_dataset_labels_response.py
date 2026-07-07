"""Generated from Smithy shape ``com.amazonaws.rekognition#ListDatasetLabelsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.dataset_label_descriptions
    import aws_sdk_rekognition.types.extended_pagination_token


class ListDatasetLabelsResponse(TypedDict, closed=True):
    dataset_label_descriptions: NotRequired[
        "aws_sdk_rekognition.types.dataset_label_descriptions.DatasetLabelDescriptions"
    ]
    """<p> A list of the labels in the dataset. </p>"""
    next_token: NotRequired[
        "aws_sdk_rekognition.types.extended_pagination_token.ExtendedPaginationToken"
    ]
    """<p>If the previous response was incomplete (because there is more results to retrieve), Amazon Rekognition Custom Labels returns a pagination token in the response. You can use this pagination token to retrieve the next set of results. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDatasetLabelsResponse) -> dict:
    out: dict = {}
    if "dataset_label_descriptions" in value:
        import aws_sdk_rekognition.types.dataset_label_descriptions

        out["DatasetLabelDescriptions"] = (
            aws_sdk_rekognition.types.dataset_label_descriptions.serialize_aws_json_1_1(
                value["dataset_label_descriptions"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDatasetLabelsResponse:
    out: ListDatasetLabelsResponse = {}  # type: ignore[typeddict-item]
    if "DatasetLabelDescriptions" in data:
        import aws_sdk_rekognition.types.dataset_label_descriptions

        out["dataset_label_descriptions"] = (
            aws_sdk_rekognition.types.dataset_label_descriptions.deserialize_aws_json_1_1(
                data["DatasetLabelDescriptions"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
