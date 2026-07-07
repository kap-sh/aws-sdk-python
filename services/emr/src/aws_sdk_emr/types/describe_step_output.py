"""Generated from Smithy shape ``com.amazonaws.emr#DescribeStepOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_emr.types.step


class DescribeStepOutput(TypedDict, closed=True):
    step: NotRequired["aws_sdk_emr.types.step.Step"]
    """<p>The step details for the requested step identifier.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeStepOutput) -> dict:
    out: dict = {}
    if "step" in value:
        import aws_sdk_emr.types.step

        out["Step"] = aws_sdk_emr.types.step.serialize_aws_json_1_1(value["step"])
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeStepOutput:
    out: DescribeStepOutput = {}  # type: ignore[typeddict-item]
    if "Step" in data:
        import aws_sdk_emr.types.step

        out["step"] = aws_sdk_emr.types.step.deserialize_aws_json_1_1(data["Step"])
    return out
