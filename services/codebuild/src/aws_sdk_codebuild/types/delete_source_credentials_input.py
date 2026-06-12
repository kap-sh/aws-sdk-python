"""Generated from Smithy shape ``com.amazonaws.codebuild#DeleteSourceCredentialsInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_codebuild.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.non_empty_string


class DeleteSourceCredentialsInput(TypedDict):
    arn: "aws_sdk_codebuild.types.non_empty_string.NonEmptyString"
    """<p> The Amazon Resource Name (ARN) of the token.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteSourceCredentialsInput) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteSourceCredentialsInput:
    out: DeleteSourceCredentialsInput = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("DeleteSourceCredentialsInput.arn required")
    return out
