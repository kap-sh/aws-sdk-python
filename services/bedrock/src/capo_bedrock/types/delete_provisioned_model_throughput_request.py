"""Generated from Smithy shape ``com.amazonaws.bedrock#DeleteProvisionedModelThroughputRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.provisioned_model_id


class DeleteProvisionedModelThroughputRequest(TypedDict, closed=True):
    provisioned_model_id: "capo_bedrock.types.provisioned_model_id.ProvisionedModelId"
    """<p>The Amazon Resource Name (ARN) or name of the Provisioned Throughput.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteProvisionedModelThroughputRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteProvisionedModelThroughputRequest:
    out: DeleteProvisionedModelThroughputRequest = {}  # type: ignore[typeddict-item]
    return out
