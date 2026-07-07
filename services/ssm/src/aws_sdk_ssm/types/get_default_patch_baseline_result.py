"""Generated from Smithy shape ``com.amazonaws.ssm#GetDefaultPatchBaselineResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm.types.baseline_id
    import aws_sdk_ssm.types.operating_system


class GetDefaultPatchBaselineResult(TypedDict, closed=True):
    baseline_id: NotRequired["aws_sdk_ssm.types.baseline_id.BaselineId"]
    """<p>The ID of the default patch baseline.</p>"""
    operating_system: NotRequired["aws_sdk_ssm.types.operating_system.OperatingSystem"]
    """<p>The operating system for the returned patch baseline. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDefaultPatchBaselineResult) -> dict:
    out: dict = {}
    if "baseline_id" in value:
        out["BaselineId"] = value["baseline_id"]
    if "operating_system" in value:
        import aws_sdk_ssm.types.operating_system

        out["OperatingSystem"] = (
            aws_sdk_ssm.types.operating_system.serialize_aws_json_1_1(
                value["operating_system"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDefaultPatchBaselineResult:
    out: GetDefaultPatchBaselineResult = {}  # type: ignore[typeddict-item]
    if "BaselineId" in data:
        out["baseline_id"] = data["BaselineId"]
    if "OperatingSystem" in data:
        import aws_sdk_ssm.types.operating_system

        out["operating_system"] = (
            aws_sdk_ssm.types.operating_system.deserialize_aws_json_1_1(
                data["OperatingSystem"]
            )
        )
    return out
