"""Generated from Smithy shape ``com.amazonaws.comprehend#DescribeDatasetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.dataset_properties


class DescribeDatasetResponse(TypedDict, closed=True):
    dataset_properties: NotRequired[
        "aws_sdk_comprehend.types.dataset_properties.DatasetProperties"
    ]
    """<p>The dataset properties.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDatasetResponse) -> dict:
    out: dict = {}
    if "dataset_properties" in value:
        import aws_sdk_comprehend.types.dataset_properties

        out["DatasetProperties"] = (
            aws_sdk_comprehend.types.dataset_properties.serialize_aws_json_1_1(
                value["dataset_properties"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDatasetResponse:
    out: DescribeDatasetResponse = {}  # type: ignore[typeddict-item]
    if "DatasetProperties" in data:
        import aws_sdk_comprehend.types.dataset_properties

        out["dataset_properties"] = (
            aws_sdk_comprehend.types.dataset_properties.deserialize_aws_json_1_1(
                data["DatasetProperties"]
            )
        )
    return out
