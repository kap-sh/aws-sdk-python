"""Generated from Smithy shape ``com.amazonaws.imagebuilder#CancelImageCreationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_imagebuilder.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.client_token
    import aws_sdk_imagebuilder.types.image_build_version_arn


class CancelImageCreationRequest(TypedDict, closed=True):
    image_build_version_arn: (
        "aws_sdk_imagebuilder.types.image_build_version_arn.ImageBuildVersionArn"
    )
    """<p>The Amazon Resource Name (ARN) of the image that you want to cancel creation for.</p>"""
    client_token: "aws_sdk_imagebuilder.types.client_token.ClientToken"
    r"""<p>Unique, case-sensitive identifier you provide to ensure idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a> in the <i>Amazon EC2 API Reference</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelImageCreationRequest) -> dict:
    out: dict = {}
    out["imageBuildVersionArn"] = value["image_build_version_arn"]
    out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CancelImageCreationRequest:
    out: CancelImageCreationRequest = {}  # type: ignore[typeddict-item]
    if "imageBuildVersionArn" in data:
        out["image_build_version_arn"] = data["imageBuildVersionArn"]
    else:
        raise DeserializationError(
            "CancelImageCreationRequest.image_build_version_arn required"
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    else:
        raise DeserializationError("CancelImageCreationRequest.client_token required")
    return out
