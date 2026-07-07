"""Generated from Smithy shape ``com.amazonaws.lambda#ImageConfigResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lambda.types.image_config
    import aws_sdk_lambda.types.image_config_error


class ImageConfigResponse(TypedDict, closed=True):
    image_config: NotRequired["aws_sdk_lambda.types.image_config.ImageConfig"]
    """<p>Configuration values that override the container image Dockerfile.</p>"""
    error: NotRequired["aws_sdk_lambda.types.image_config_error.ImageConfigError"]
    """<p>Error response to <code>GetFunctionConfiguration</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImageConfigResponse) -> dict:
    out: dict = {}
    if "image_config" in value:
        import aws_sdk_lambda.types.image_config

        out["ImageConfig"] = aws_sdk_lambda.types.image_config.serialize_json(
            value["image_config"]
        )
    if "error" in value:
        import aws_sdk_lambda.types.image_config_error

        out["Error"] = aws_sdk_lambda.types.image_config_error.serialize_json(
            value["error"]
        )
    return out


def deserialize_json(data: dict) -> ImageConfigResponse:
    out: ImageConfigResponse = {}  # type: ignore[typeddict-item]
    if "ImageConfig" in data:
        import aws_sdk_lambda.types.image_config

        out["image_config"] = aws_sdk_lambda.types.image_config.deserialize_json(
            data["ImageConfig"]
        )
    if "Error" in data:
        import aws_sdk_lambda.types.image_config_error

        out["error"] = aws_sdk_lambda.types.image_config_error.deserialize_json(
            data["Error"]
        )
    return out
