"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#UpdateActiveModelVersionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lookoutequipment.types.model_arn
    import aws_sdk_lookoutequipment.types.model_name
    import aws_sdk_lookoutequipment.types.model_version
    import aws_sdk_lookoutequipment.types.model_version_arn


class UpdateActiveModelVersionResponse(TypedDict, closed=True):
    model_name: NotRequired["aws_sdk_lookoutequipment.types.model_name.ModelName"]
    """<p>The name of the machine learning model for which the active model version was set.</p>"""
    model_arn: NotRequired["aws_sdk_lookoutequipment.types.model_arn.ModelArn"]
    """<p>The Amazon Resource Name (ARN) of the machine learning model for which the active model version was set.</p>"""
    current_active_version: NotRequired[
        "aws_sdk_lookoutequipment.types.model_version.ModelVersion"
    ]
    """<p>The version that is currently active of the machine learning model for which the active model version was set.</p>"""
    previous_active_version: NotRequired[
        "aws_sdk_lookoutequipment.types.model_version.ModelVersion"
    ]
    """<p>The previous version that was active of the machine learning model for which the active model version was set.</p>"""
    current_active_version_arn: NotRequired[
        "aws_sdk_lookoutequipment.types.model_version_arn.ModelVersionArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the machine learning model version that is the current active model version.</p>"""
    previous_active_version_arn: NotRequired[
        "aws_sdk_lookoutequipment.types.model_version_arn.ModelVersionArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the machine learning model version that was the previous active model version.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateActiveModelVersionResponse) -> dict:
    out: dict = {}
    if "model_name" in value:
        out["ModelName"] = value["model_name"]
    if "model_arn" in value:
        out["ModelArn"] = value["model_arn"]
    if "current_active_version" in value:
        out["CurrentActiveVersion"] = value["current_active_version"]
    if "previous_active_version" in value:
        out["PreviousActiveVersion"] = value["previous_active_version"]
    if "current_active_version_arn" in value:
        out["CurrentActiveVersionArn"] = value["current_active_version_arn"]
    if "previous_active_version_arn" in value:
        out["PreviousActiveVersionArn"] = value["previous_active_version_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateActiveModelVersionResponse:
    out: UpdateActiveModelVersionResponse = {}  # type: ignore[typeddict-item]
    if "ModelName" in data:
        out["model_name"] = data["ModelName"]
    if "ModelArn" in data:
        out["model_arn"] = data["ModelArn"]
    if "CurrentActiveVersion" in data:
        out["current_active_version"] = data["CurrentActiveVersion"]
    if "PreviousActiveVersion" in data:
        out["previous_active_version"] = data["PreviousActiveVersion"]
    if "CurrentActiveVersionArn" in data:
        out["current_active_version_arn"] = data["CurrentActiveVersionArn"]
    if "PreviousActiveVersionArn" in data:
        out["previous_active_version_arn"] = data["PreviousActiveVersionArn"]
    return out
