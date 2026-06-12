"""Generated from Smithy shape ``com.amazonaws.imagebuilder#RetryImageRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_imagebuilder.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.client_token
    import aws_sdk_imagebuilder.types.image_build_version_arn


class RetryImageRequest(TypedDict):
    image_build_version_arn: (
        "aws_sdk_imagebuilder.types.image_build_version_arn.ImageBuildVersionArn"
    )
    """<p>The source image Amazon Resource Name (ARN) to retry.</p>"""
    client_token: "aws_sdk_imagebuilder.types.client_token.ClientToken"
    """<p>Unique, case-sensitive identifier you provide to ensure idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a> in the <i>Amazon EC2 API Reference</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RetryImageRequest) -> dict:
    out: dict = {}
    out["imageBuildVersionArn"] = value["image_build_version_arn"]
    out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> RetryImageRequest:
    out: RetryImageRequest = {}  # type: ignore[typeddict-item]
    if "imageBuildVersionArn" in data:
        out["image_build_version_arn"] = data["imageBuildVersionArn"]
    else:
        raise DeserializationError("RetryImageRequest.image_build_version_arn required")
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    else:
        raise DeserializationError("RetryImageRequest.client_token required")
    return out
