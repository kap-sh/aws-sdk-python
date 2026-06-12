"""Generated from Smithy shape ``com.amazonaws.codebuild#DeleteSourceCredentialsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.non_empty_string


class DeleteSourceCredentialsOutput(TypedDict):
    arn: NotRequired["aws_sdk_codebuild.types.non_empty_string.NonEmptyString"]
    """<p> The Amazon Resource Name (ARN) of the token. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteSourceCredentialsOutput) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteSourceCredentialsOutput:
    out: DeleteSourceCredentialsOutput = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    return out
