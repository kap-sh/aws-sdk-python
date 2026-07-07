"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateAppResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.app_arn


class CreateAppResponse(TypedDict, closed=True):
    app_arn: NotRequired["aws_sdk_sagemaker.types.app_arn.AppArn"]
    """<p>The Amazon Resource Name (ARN) of the app.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateAppResponse) -> dict:
    out: dict = {}
    if "app_arn" in value:
        out["AppArn"] = value["app_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateAppResponse:
    out: CreateAppResponse = {}  # type: ignore[typeddict-item]
    if "AppArn" in data:
        out["app_arn"] = data["AppArn"]
    return out
