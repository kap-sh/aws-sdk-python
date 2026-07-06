"""Generated from Smithy shape ``com.amazonaws.codebuild#DeleteReportInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_codebuild.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.non_empty_string


class DeleteReportInput(TypedDict, closed=True):
    arn: "aws_sdk_codebuild.types.non_empty_string.NonEmptyString"
    """<p> The ARN of the report to delete. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteReportInput) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteReportInput:
    out: DeleteReportInput = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("DeleteReportInput.arn required")
    return out
