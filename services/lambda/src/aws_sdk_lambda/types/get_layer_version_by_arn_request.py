"""Generated from Smithy shape ``com.amazonaws.lambda#GetLayerVersionByArnRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_lambda.types.layer_version_arn


class GetLayerVersionByArnRequest(TypedDict, closed=True):
    arn: "aws_sdk_lambda.types.layer_version_arn.LayerVersionArn"
    """<p>The ARN of the layer version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetLayerVersionByArnRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetLayerVersionByArnRequest:
    out: GetLayerVersionByArnRequest = {}  # type: ignore[typeddict-item]
    return out
