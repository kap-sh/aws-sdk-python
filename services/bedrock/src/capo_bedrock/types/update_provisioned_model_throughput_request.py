"""Generated from Smithy shape ``com.amazonaws.bedrock#UpdateProvisionedModelThroughputRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.model_identifier
    import capo_bedrock.types.provisioned_model_id
    import capo_bedrock.types.provisioned_model_name


class UpdateProvisionedModelThroughputRequest(TypedDict, closed=True):
    provisioned_model_id: "capo_bedrock.types.provisioned_model_id.ProvisionedModelId"
    """<p>The Amazon Resource Name (ARN) or name of the Provisioned Throughput to update.</p>"""
    desired_provisioned_model_name: NotRequired[
        "capo_bedrock.types.provisioned_model_name.ProvisionedModelName"
    ]
    """<p>The new name for this Provisioned Throughput.</p>"""
    desired_model_id: NotRequired["capo_bedrock.types.model_identifier.ModelIdentifier"]
    """<p>The Amazon Resource Name (ARN) of the new model to associate with this Provisioned Throughput. You can't specify this field if this Provisioned Throughput is associated with a base model.</p> <p>If this Provisioned Throughput is associated with a custom model, you can specify one of the following options:</p> <ul> <li> <p>The base model from which the custom model was customized.</p> </li> <li> <p>Another custom model that was customized from the same base model as the custom model.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateProvisionedModelThroughputRequest) -> dict:
    out: dict = {}
    if "desired_provisioned_model_name" in value:
        out["desiredProvisionedModelName"] = value["desired_provisioned_model_name"]
    if "desired_model_id" in value:
        out["desiredModelId"] = value["desired_model_id"]
    return out


def deserialize_json(data: dict) -> UpdateProvisionedModelThroughputRequest:
    out: UpdateProvisionedModelThroughputRequest = {}  # type: ignore[typeddict-item]
    if "desiredProvisionedModelName" in data:
        out["desired_provisioned_model_name"] = data["desiredProvisionedModelName"]
    if "desiredModelId" in data:
        out["desired_model_id"] = data["desiredModelId"]
    return out
