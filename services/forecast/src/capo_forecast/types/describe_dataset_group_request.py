"""Generated from Smithy shape ``com.amazonaws.forecast#DescribeDatasetGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_forecast.errors import DeserializationError

if TYPE_CHECKING:
    import capo_forecast.types.arn


class DescribeDatasetGroupRequest(TypedDict, closed=True):
    dataset_group_arn: "capo_forecast.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the dataset group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDatasetGroupRequest) -> dict:
    out: dict = {}
    out["DatasetGroupArn"] = value["dataset_group_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDatasetGroupRequest:
    out: DescribeDatasetGroupRequest = {}  # type: ignore[typeddict-item]
    if "DatasetGroupArn" in data:
        out["dataset_group_arn"] = data["DatasetGroupArn"]
    else:
        raise DeserializationError(
            "DescribeDatasetGroupRequest.dataset_group_arn required"
        )
    return out
