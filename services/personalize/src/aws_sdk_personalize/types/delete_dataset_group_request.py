"""Generated from Smithy shape ``com.amazonaws.personalize#DeleteDatasetGroupRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_personalize.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_personalize.types.arn


class DeleteDatasetGroupRequest(TypedDict):
    dataset_group_arn: "aws_sdk_personalize.types.arn.Arn"
    """<p>The ARN of the dataset group to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteDatasetGroupRequest) -> dict:
    out: dict = {}
    out["datasetGroupArn"] = value["dataset_group_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteDatasetGroupRequest:
    out: DeleteDatasetGroupRequest = {}  # type: ignore[typeddict-item]
    if "datasetGroupArn" in data:
        out["dataset_group_arn"] = data["datasetGroupArn"]
    else:
        raise DeserializationError(
            "DeleteDatasetGroupRequest.dataset_group_arn required"
        )
    return out
