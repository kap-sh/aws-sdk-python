"""Generated from Smithy shape ``com.amazonaws.rekognition#DescribeDatasetResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.dataset_description


class DescribeDatasetResponse(TypedDict):
    dataset_description: NotRequired[
        "aws_sdk_rekognition.types.dataset_description.DatasetDescription"
    ]
    """<p> The description for the dataset. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDatasetResponse) -> dict:
    out: dict = {}
    if "dataset_description" in value:
        import aws_sdk_rekognition.types.dataset_description

        out["DatasetDescription"] = (
            aws_sdk_rekognition.types.dataset_description.serialize_aws_json_1_1(
                value["dataset_description"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDatasetResponse:
    out: DescribeDatasetResponse = {}  # type: ignore[typeddict-item]
    if "DatasetDescription" in data:
        import aws_sdk_rekognition.types.dataset_description

        out["dataset_description"] = (
            aws_sdk_rekognition.types.dataset_description.deserialize_aws_json_1_1(
                data["DatasetDescription"]
            )
        )
    return out
