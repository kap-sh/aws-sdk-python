"""Generated from Smithy shape ``com.amazonaws.lambda#GetLayerVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_lambda.types.layer_name
    import aws_sdk_lambda.types.layer_version_number


class GetLayerVersionRequest(TypedDict, closed=True):
    layer_name: "aws_sdk_lambda.types.layer_name.LayerName"
    """<p>The name or Amazon Resource Name (ARN) of the layer.</p>"""
    version_number: "aws_sdk_lambda.types.layer_version_number.LayerVersionNumber"
    """<p>The version number.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetLayerVersionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetLayerVersionRequest:
    out: GetLayerVersionRequest = {}  # type: ignore[typeddict-item]
    return out
