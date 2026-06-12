"""Generated from Smithy shape ``com.amazonaws.codebuild#DeleteFleetInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_codebuild.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.non_empty_string


class DeleteFleetInput(TypedDict):
    arn: "aws_sdk_codebuild.types.non_empty_string.NonEmptyString"
    """<p>The ARN of the compute fleet.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteFleetInput) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteFleetInput:
    out: DeleteFleetInput = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("DeleteFleetInput.arn required")
    return out
