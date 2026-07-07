"""Generated from Smithy shape ``com.amazonaws.codebuild#BatchGetReportsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_codebuild.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.report_arns


class BatchGetReportsInput(TypedDict, closed=True):
    report_arns: "aws_sdk_codebuild.types.report_arns.ReportArns"
    """<p> An array of ARNs that identify the <code>Report</code> objects to return. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetReportsInput) -> dict:
    out: dict = {}
    import aws_sdk_codebuild.types.report_arns

    out["reportArns"] = aws_sdk_codebuild.types.report_arns.serialize_aws_json_1_1(
        value["report_arns"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetReportsInput:
    out: BatchGetReportsInput = {}  # type: ignore[typeddict-item]
    if "reportArns" in data:
        import aws_sdk_codebuild.types.report_arns

        out["report_arns"] = (
            aws_sdk_codebuild.types.report_arns.deserialize_aws_json_1_1(
                data["reportArns"]
            )
        )
    else:
        raise DeserializationError("BatchGetReportsInput.report_arns required")
    return out
