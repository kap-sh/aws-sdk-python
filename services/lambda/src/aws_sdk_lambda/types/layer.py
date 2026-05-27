"""Generated from Smithy shape ``com.amazonaws.lambda#Layer``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lambda.types.arn
    import aws_sdk_lambda.types.layer_version_arn
    import aws_sdk_lambda.types.long


class Layer(TypedDict):
    arn: NotRequired["aws_sdk_lambda.types.layer_version_arn.LayerVersionArn"]
    """<p>The Amazon Resource Name (ARN) of the function layer.</p>"""
    code_size: "aws_sdk_lambda.types.long.Long"
    """<p>The size of the layer archive in bytes.</p>"""
    signing_profile_version_arn: NotRequired["aws_sdk_lambda.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) for a signing profile version.</p>"""
    signing_job_arn: NotRequired["aws_sdk_lambda.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of a signing job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Layer) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    out["CodeSize"] = value.get("code_size", 0)
    if "signing_profile_version_arn" in value:
        out["SigningProfileVersionArn"] = value["signing_profile_version_arn"]
    if "signing_job_arn" in value:
        out["SigningJobArn"] = value["signing_job_arn"]
    return out


def deserialize_json(data: dict) -> Layer:
    out: Layer = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "CodeSize" in data:
        out["code_size"] = data["CodeSize"]
    else:
        out["code_size"] = 0
    if "SigningProfileVersionArn" in data:
        out["signing_profile_version_arn"] = data["SigningProfileVersionArn"]
    if "SigningJobArn" in data:
        out["signing_job_arn"] = data["SigningJobArn"]
    return out
