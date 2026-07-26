"""Generated from Smithy shape ``com.amazonaws.lambda#LayerVersionContentOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.long
    import capo_lambda.types.string


class LayerVersionContentOutput(TypedDict, closed=True):
    location: NotRequired["capo_lambda.types.string.String"]
    """<p>A link to the layer archive in Amazon S3 that is valid for 10 minutes.</p>"""
    code_sha256: NotRequired["capo_lambda.types.string.String"]
    """<p>The SHA-256 hash of the layer archive.</p>"""
    code_size: "capo_lambda.types.long.Long"
    """<p>The size of the layer archive in bytes.</p>"""
    signing_profile_version_arn: NotRequired["capo_lambda.types.string.String"]
    """<p>The Amazon Resource Name (ARN) for a signing profile version.</p>"""
    signing_job_arn: NotRequired["capo_lambda.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of a signing job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LayerVersionContentOutput) -> dict:
    out: dict = {}
    if "location" in value:
        out["Location"] = value["location"]
    if "code_sha256" in value:
        out["CodeSha256"] = value["code_sha256"]
    out["CodeSize"] = value.get("code_size", 0)
    if "signing_profile_version_arn" in value:
        out["SigningProfileVersionArn"] = value["signing_profile_version_arn"]
    if "signing_job_arn" in value:
        out["SigningJobArn"] = value["signing_job_arn"]
    return out


def deserialize_json(data: dict) -> LayerVersionContentOutput:
    out: LayerVersionContentOutput = {}  # type: ignore[typeddict-item]
    if "Location" in data:
        out["location"] = data["Location"]
    if "CodeSha256" in data:
        out["code_sha256"] = data["CodeSha256"]
    if "CodeSize" in data:
        out["code_size"] = data["CodeSize"]
    else:
        out["code_size"] = 0
    if "SigningProfileVersionArn" in data:
        out["signing_profile_version_arn"] = data["SigningProfileVersionArn"]
    if "SigningJobArn" in data:
        out["signing_job_arn"] = data["SigningJobArn"]
    return out
