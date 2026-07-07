"""Generated from Smithy shape ``com.amazonaws.ssm#CreatePatchBaselineResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm.types.baseline_id


class CreatePatchBaselineResult(TypedDict, closed=True):
    baseline_id: NotRequired["aws_sdk_ssm.types.baseline_id.BaselineId"]
    """<p>The ID of the created patch baseline.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreatePatchBaselineResult) -> dict:
    out: dict = {}
    if "baseline_id" in value:
        out["BaselineId"] = value["baseline_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreatePatchBaselineResult:
    out: CreatePatchBaselineResult = {}  # type: ignore[typeddict-item]
    if "BaselineId" in data:
        out["baseline_id"] = data["BaselineId"]
    return out
