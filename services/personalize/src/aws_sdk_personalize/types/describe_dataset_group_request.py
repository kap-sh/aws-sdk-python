"""Generated from Smithy shape ``com.amazonaws.personalize#DescribeDatasetGroupRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_personalize.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_personalize.types.arn


class DescribeDatasetGroupRequest(TypedDict):
    dataset_group_arn: "aws_sdk_personalize.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the dataset group to describe.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDatasetGroupRequest) -> dict:
    out: dict = {}
    out["datasetGroupArn"] = value["dataset_group_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDatasetGroupRequest:
    out: DescribeDatasetGroupRequest = {}  # type: ignore[typeddict-item]
    if "datasetGroupArn" in data:
        out["dataset_group_arn"] = data["datasetGroupArn"]
    else:
        raise DeserializationError(
            "DescribeDatasetGroupRequest.dataset_group_arn required"
        )
    return out
