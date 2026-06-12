"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#CreateModelResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lookoutequipment.types.model_arn
    import aws_sdk_lookoutequipment.types.model_status


class CreateModelResponse(TypedDict):
    model_arn: NotRequired["aws_sdk_lookoutequipment.types.model_arn.ModelArn"]
    """<p>The Amazon Resource Name (ARN) of the model being created. </p>"""
    status: NotRequired["aws_sdk_lookoutequipment.types.model_status.ModelStatus"]
    """<p>Indicates the status of the <code>CreateModel</code> operation. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateModelResponse) -> dict:
    out: dict = {}
    if "model_arn" in value:
        out["ModelArn"] = value["model_arn"]
    if "status" in value:
        import aws_sdk_lookoutequipment.types.model_status

        out["Status"] = (
            aws_sdk_lookoutequipment.types.model_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateModelResponse:
    out: CreateModelResponse = {}  # type: ignore[typeddict-item]
    if "ModelArn" in data:
        out["model_arn"] = data["ModelArn"]
    if "Status" in data:
        import aws_sdk_lookoutequipment.types.model_status

        out["status"] = (
            aws_sdk_lookoutequipment.types.model_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    return out
