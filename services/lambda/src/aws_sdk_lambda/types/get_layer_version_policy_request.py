"""Generated from Smithy shape ``com.amazonaws.lambda#GetLayerVersionPolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lambda.types.layer_name
    import aws_sdk_lambda.types.layer_version_number


class GetLayerVersionPolicyRequest(TypedDict):
    layer_name: "aws_sdk_lambda.types.layer_name.LayerName"
    """<p>The name or Amazon Resource Name (ARN) of the layer.</p>"""
    version_number: "aws_sdk_lambda.types.layer_version_number.LayerVersionNumber"
    """<p>The version number.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetLayerVersionPolicyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetLayerVersionPolicyRequest:
    out: GetLayerVersionPolicyRequest = {}  # type: ignore[typeddict-item]
    return out
