"""Generated from Smithy shape ``com.amazonaws.sagemaker#DeleteModelCardRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.entity_name


class DeleteModelCardRequest(TypedDict, closed=True):
    model_card_name: NotRequired["aws_sdk_sagemaker.types.entity_name.EntityName"]
    """<p>The name of the model card to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteModelCardRequest) -> dict:
    out: dict = {}
    if "model_card_name" in value:
        out["ModelCardName"] = value["model_card_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteModelCardRequest:
    out: DeleteModelCardRequest = {}  # type: ignore[typeddict-item]
    if "ModelCardName" in data:
        out["model_card_name"] = data["ModelCardName"]
    return out
