"""Generated from Smithy shape ``com.amazonaws.comprehend#DescribeDatasetRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_comprehend.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.comprehend_dataset_arn


class DescribeDatasetRequest(TypedDict):
    dataset_arn: "aws_sdk_comprehend.types.comprehend_dataset_arn.ComprehendDatasetArn"
    """<p>The ARN of the dataset.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDatasetRequest) -> dict:
    out: dict = {}
    out["DatasetArn"] = value["dataset_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDatasetRequest:
    out: DescribeDatasetRequest = {}  # type: ignore[typeddict-item]
    if "DatasetArn" in data:
        out["dataset_arn"] = data["DatasetArn"]
    else:
        raise DeserializationError("DescribeDatasetRequest.dataset_arn required")
    return out
