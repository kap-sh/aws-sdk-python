"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Policy``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.input_policy


class Policy(TypedDict):
    http_inputs: NotRequired["aws_sdk_mediaconvert.types.input_policy.InputPolicy"]
    """Allow or disallow jobs that specify HTTP inputs."""
    https_inputs: NotRequired["aws_sdk_mediaconvert.types.input_policy.InputPolicy"]
    """Allow or disallow jobs that specify HTTPS inputs."""
    s3_inputs: NotRequired["aws_sdk_mediaconvert.types.input_policy.InputPolicy"]
    """Allow or disallow jobs that specify Amazon S3 inputs."""


# --- restJson1 ser/de ---
def serialize_json(value: Policy) -> dict:
    out: dict = {}
    if "http_inputs" in value:
        import aws_sdk_mediaconvert.types.input_policy

        out["httpInputs"] = aws_sdk_mediaconvert.types.input_policy.serialize_json(
            value["http_inputs"]
        )
    if "https_inputs" in value:
        import aws_sdk_mediaconvert.types.input_policy

        out["httpsInputs"] = aws_sdk_mediaconvert.types.input_policy.serialize_json(
            value["https_inputs"]
        )
    if "s3_inputs" in value:
        import aws_sdk_mediaconvert.types.input_policy

        out["s3Inputs"] = aws_sdk_mediaconvert.types.input_policy.serialize_json(
            value["s3_inputs"]
        )
    return out


def deserialize_json(data: dict) -> Policy:
    out: Policy = {}  # type: ignore[typeddict-item]
    if "httpInputs" in data:
        import aws_sdk_mediaconvert.types.input_policy

        out["http_inputs"] = aws_sdk_mediaconvert.types.input_policy.deserialize_json(
            data["httpInputs"]
        )
    if "httpsInputs" in data:
        import aws_sdk_mediaconvert.types.input_policy

        out["https_inputs"] = aws_sdk_mediaconvert.types.input_policy.deserialize_json(
            data["httpsInputs"]
        )
    if "s3Inputs" in data:
        import aws_sdk_mediaconvert.types.input_policy

        out["s3_inputs"] = aws_sdk_mediaconvert.types.input_policy.deserialize_json(
            data["s3Inputs"]
        )
    return out
