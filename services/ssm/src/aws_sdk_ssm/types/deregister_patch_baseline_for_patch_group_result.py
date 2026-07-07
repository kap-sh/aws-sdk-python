"""Generated from Smithy shape ``com.amazonaws.ssm#DeregisterPatchBaselineForPatchGroupResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm.types.baseline_id
    import aws_sdk_ssm.types.patch_group


class DeregisterPatchBaselineForPatchGroupResult(TypedDict, closed=True):
    baseline_id: NotRequired["aws_sdk_ssm.types.baseline_id.BaselineId"]
    """<p>The ID of the patch baseline the patch group was deregistered from.</p>"""
    patch_group: NotRequired["aws_sdk_ssm.types.patch_group.PatchGroup"]
    """<p>The name of the patch group deregistered from the patch baseline.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeregisterPatchBaselineForPatchGroupResult) -> dict:
    out: dict = {}
    if "baseline_id" in value:
        out["BaselineId"] = value["baseline_id"]
    if "patch_group" in value:
        out["PatchGroup"] = value["patch_group"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeregisterPatchBaselineForPatchGroupResult:
    out: DeregisterPatchBaselineForPatchGroupResult = {}  # type: ignore[typeddict-item]
    if "BaselineId" in data:
        out["baseline_id"] = data["BaselineId"]
    if "PatchGroup" in data:
        out["patch_group"] = data["PatchGroup"]
    return out
