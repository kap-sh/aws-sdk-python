"""Generated from Smithy shape ``com.amazonaws.rekognition#DeleteDatasetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_rekognition.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.dataset_arn


class DeleteDatasetRequest(TypedDict, closed=True):
    dataset_arn: "aws_sdk_rekognition.types.dataset_arn.DatasetArn"
    """<p> The ARN of the Amazon Rekognition Custom Labels dataset that you want to delete. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteDatasetRequest) -> dict:
    out: dict = {}
    out["DatasetArn"] = value["dataset_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteDatasetRequest:
    out: DeleteDatasetRequest = {}  # type: ignore[typeddict-item]
    if "DatasetArn" in data:
        out["dataset_arn"] = data["DatasetArn"]
    else:
        raise DeserializationError("DeleteDatasetRequest.dataset_arn required")
    return out
