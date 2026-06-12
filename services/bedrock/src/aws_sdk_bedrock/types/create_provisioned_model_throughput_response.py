"""Generated from Smithy shape ``com.amazonaws.bedrock#CreateProvisionedModelThroughputResponse``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.provisioned_model_arn


class CreateProvisionedModelThroughputResponse(TypedDict):
    provisioned_model_arn: (
        "aws_sdk_bedrock.types.provisioned_model_arn.ProvisionedModelArn"
    )
    """<p>The Amazon Resource Name (ARN) for this Provisioned Throughput.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateProvisionedModelThroughputResponse) -> dict:
    out: dict = {}
    out["provisionedModelArn"] = value["provisioned_model_arn"]
    return out


def deserialize_json(data: dict) -> CreateProvisionedModelThroughputResponse:
    out: CreateProvisionedModelThroughputResponse = {}  # type: ignore[typeddict-item]
    if "provisionedModelArn" in data:
        out["provisioned_model_arn"] = data["provisionedModelArn"]
    else:
        raise DeserializationError(
            "CreateProvisionedModelThroughputResponse.provisioned_model_arn required"
        )
    return out
