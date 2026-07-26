"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsLambdaFunctionLayer``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.integer
    import capo_securityhub.types.non_empty_string


class AwsLambdaFunctionLayer(TypedDict, closed=True):
    arn: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The ARN of the function layer.</p>"""
    code_size: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p>The size of the layer archive in bytes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsLambdaFunctionLayer) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "code_size" in value:
        out["CodeSize"] = value["code_size"]
    return out


def deserialize_json(data: dict) -> AwsLambdaFunctionLayer:
    out: AwsLambdaFunctionLayer = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "CodeSize" in data:
        out["code_size"] = data["CodeSize"]
    return out
