"""Generated from Smithy shape ``com.amazonaws.bedrock#GetProvisionedModelThroughputRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.provisioned_model_id


class GetProvisionedModelThroughputRequest(TypedDict):
    provisioned_model_id: (
        "aws_sdk_bedrock.types.provisioned_model_id.ProvisionedModelId"
    )
    """<p>The Amazon Resource Name (ARN) or name of the Provisioned Throughput.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetProvisionedModelThroughputRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetProvisionedModelThroughputRequest:
    out: GetProvisionedModelThroughputRequest = {}  # type: ignore[typeddict-item]
    return out
