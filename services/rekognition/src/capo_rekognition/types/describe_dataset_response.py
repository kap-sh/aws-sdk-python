"""Generated from Smithy shape ``com.amazonaws.rekognition#DescribeDatasetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.dataset_description


class DescribeDatasetResponse(TypedDict, closed=True):
    dataset_description: NotRequired[
        "capo_rekognition.types.dataset_description.DatasetDescription"
    ]
    """<p> The description for the dataset. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDatasetResponse) -> dict:
    out: dict = {}
    if "dataset_description" in value:
        import capo_rekognition.types.dataset_description

        out["DatasetDescription"] = (
            capo_rekognition.types.dataset_description.serialize_aws_json_1_1(
                value["dataset_description"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDatasetResponse:
    out: DescribeDatasetResponse = {}  # type: ignore[typeddict-item]
    if "DatasetDescription" in data:
        import capo_rekognition.types.dataset_description

        out["dataset_description"] = (
            capo_rekognition.types.dataset_description.deserialize_aws_json_1_1(
                data["DatasetDescription"]
            )
        )
    return out
