"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#CreateModelResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lookoutequipment.types.model_arn
    import capo_lookoutequipment.types.model_status


class CreateModelResponse(TypedDict, closed=True):
    model_arn: NotRequired["capo_lookoutequipment.types.model_arn.ModelArn"]
    """<p>The Amazon Resource Name (ARN) of the model being created. </p>"""
    status: NotRequired["capo_lookoutequipment.types.model_status.ModelStatus"]
    """<p>Indicates the status of the <code>CreateModel</code> operation. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateModelResponse) -> dict:
    out: dict = {}
    if "model_arn" in value:
        out["ModelArn"] = value["model_arn"]
    if "status" in value:
        import capo_lookoutequipment.types.model_status

        out["Status"] = capo_lookoutequipment.types.model_status.serialize_aws_json_1_0(
            value["status"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateModelResponse:
    out: CreateModelResponse = {}  # type: ignore[typeddict-item]
    if "ModelArn" in data:
        out["model_arn"] = data["ModelArn"]
    if "Status" in data:
        import capo_lookoutequipment.types.model_status

        out["status"] = (
            capo_lookoutequipment.types.model_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    return out
