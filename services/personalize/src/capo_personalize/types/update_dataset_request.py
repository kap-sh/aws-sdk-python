"""Generated from Smithy shape ``com.amazonaws.personalize#UpdateDatasetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_personalize.errors import DeserializationError

if TYPE_CHECKING:
    import capo_personalize.types.arn


class UpdateDatasetRequest(TypedDict, closed=True):
    dataset_arn: "capo_personalize.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the dataset that you want to update.</p>"""
    schema_arn: "capo_personalize.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the new schema you want use.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateDatasetRequest) -> dict:
    out: dict = {}
    out["datasetArn"] = value["dataset_arn"]
    out["schemaArn"] = value["schema_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateDatasetRequest:
    out: UpdateDatasetRequest = {}  # type: ignore[typeddict-item]
    if "datasetArn" in data:
        out["dataset_arn"] = data["datasetArn"]
    else:
        raise DeserializationError("UpdateDatasetRequest.dataset_arn required")
    if "schemaArn" in data:
        out["schema_arn"] = data["schemaArn"]
    else:
        raise DeserializationError("UpdateDatasetRequest.schema_arn required")
    return out
