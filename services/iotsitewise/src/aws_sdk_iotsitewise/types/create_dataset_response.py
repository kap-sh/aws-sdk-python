"""Generated from Smithy shape ``com.amazonaws.iotsitewise#CreateDatasetResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.arn
    import aws_sdk_iotsitewise.types.dataset_status
    import aws_sdk_iotsitewise.types.id


class CreateDatasetResponse(TypedDict):
    dataset_id: "aws_sdk_iotsitewise.types.id.ID"
    """<p>The ID of the dataset.</p>"""
    dataset_arn: "aws_sdk_iotsitewise.types.arn.ARN"
    """<p>The <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html\">ARN</a> of the dataset. The format is <code>arn:${Partition}:iotsitewise:${Region}:${Account}:dataset/${DatasetId}</code>.</p>"""
    dataset_status: "aws_sdk_iotsitewise.types.dataset_status.DatasetStatus"
    """<p>The status of the dataset. This contains the state and any error messages. State is <code>CREATING</code> after a successfull call to this API, and any associated error message. The state is <code>ACTIVE</code> when ready to use.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDatasetResponse) -> dict:
    out: dict = {}
    out["datasetId"] = value["dataset_id"]
    out["datasetArn"] = value["dataset_arn"]
    import aws_sdk_iotsitewise.types.dataset_status

    out["datasetStatus"] = aws_sdk_iotsitewise.types.dataset_status.serialize_json(
        value["dataset_status"]
    )
    return out


def deserialize_json(data: dict) -> CreateDatasetResponse:
    out: CreateDatasetResponse = {}  # type: ignore[typeddict-item]
    if "datasetId" in data:
        out["dataset_id"] = data["datasetId"]
    else:
        raise DeserializationError("CreateDatasetResponse.dataset_id required")
    if "datasetArn" in data:
        out["dataset_arn"] = data["datasetArn"]
    else:
        raise DeserializationError("CreateDatasetResponse.dataset_arn required")
    if "datasetStatus" in data:
        import aws_sdk_iotsitewise.types.dataset_status

        out["dataset_status"] = (
            aws_sdk_iotsitewise.types.dataset_status.deserialize_json(
                data["datasetStatus"]
            )
        )
    else:
        raise DeserializationError("CreateDatasetResponse.dataset_status required")
    return out
