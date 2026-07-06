"""Generated from Smithy shape ``com.amazonaws.applicationautoscaling#RegisterScalableTargetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_application_auto_scaling.types.xml_string


class RegisterScalableTargetResponse(TypedDict, closed=True):
    scalable_target_arn: NotRequired[
        "aws_sdk_application_auto_scaling.types.xml_string.XmlString"
    ]
    """<p>The ARN of the scalable target.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegisterScalableTargetResponse) -> dict:
    out: dict = {}
    if "scalable_target_arn" in value:
        out["ScalableTargetARN"] = value["scalable_target_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RegisterScalableTargetResponse:
    out: RegisterScalableTargetResponse = {}  # type: ignore[typeddict-item]
    if "ScalableTargetARN" in data:
        out["scalable_target_arn"] = data["ScalableTargetARN"]
    return out
