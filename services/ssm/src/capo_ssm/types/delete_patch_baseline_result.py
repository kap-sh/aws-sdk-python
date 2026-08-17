"""Generated from Smithy shape ``com.amazonaws.ssm#DeletePatchBaselineResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.baseline_id


class DeletePatchBaselineResult(TypedDict, closed=True):
    baseline_id: NotRequired["capo_ssm.types.baseline_id.BaselineId"]
    """<p>The ID of the deleted patch baseline.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeletePatchBaselineResult) -> dict:
    out: dict = {}
    if "baseline_id" in value:
        out["BaselineId"] = value["baseline_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeletePatchBaselineResult:
    out: DeletePatchBaselineResult = {}  # type: ignore[typeddict-item]
    if data.get("BaselineId") is not None:
        out["baseline_id"] = data["BaselineId"]
    return out
