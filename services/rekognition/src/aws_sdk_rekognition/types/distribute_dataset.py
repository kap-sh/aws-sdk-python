"""Generated from Smithy shape ``com.amazonaws.rekognition#DistributeDataset``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_rekognition.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.dataset_arn


class DistributeDataset(TypedDict, closed=True):
    arn: "aws_sdk_rekognition.types.dataset_arn.DatasetArn"
    """<p>The Amazon Resource Name (ARN) of the dataset that you want to use. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DistributeDataset) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DistributeDataset:
    out: DistributeDataset = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("DistributeDataset.arn required")
    return out
