"""Generated from Smithy shape ``com.amazonaws.ssm#RegisterPatchBaselineForPatchGroupResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm.types.baseline_id
    import aws_sdk_ssm.types.patch_group


class RegisterPatchBaselineForPatchGroupResult(TypedDict, closed=True):
    baseline_id: NotRequired["aws_sdk_ssm.types.baseline_id.BaselineId"]
    """<p>The ID of the patch baseline the patch group was registered with.</p>"""
    patch_group: NotRequired["aws_sdk_ssm.types.patch_group.PatchGroup"]
    """<p>The name of the patch group registered with the patch baseline.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegisterPatchBaselineForPatchGroupResult) -> dict:
    out: dict = {}
    if "baseline_id" in value:
        out["BaselineId"] = value["baseline_id"]
    if "patch_group" in value:
        out["PatchGroup"] = value["patch_group"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RegisterPatchBaselineForPatchGroupResult:
    out: RegisterPatchBaselineForPatchGroupResult = {}  # type: ignore[typeddict-item]
    if "BaselineId" in data:
        out["baseline_id"] = data["BaselineId"]
    if "PatchGroup" in data:
        out["patch_group"] = data["PatchGroup"]
    return out
