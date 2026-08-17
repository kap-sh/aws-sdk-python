"""Generated from Smithy shape ``com.amazonaws.ssm#GetPatchBaselineForPatchGroupResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.baseline_id
    import capo_ssm.types.operating_system
    import capo_ssm.types.patch_group


class GetPatchBaselineForPatchGroupResult(TypedDict, closed=True):
    baseline_id: NotRequired["capo_ssm.types.baseline_id.BaselineId"]
    """<p>The ID of the patch baseline that should be used for the patch group.</p>"""
    patch_group: NotRequired["capo_ssm.types.patch_group.PatchGroup"]
    """<p>The name of the patch group.</p>"""
    operating_system: NotRequired["capo_ssm.types.operating_system.OperatingSystem"]
    """<p>The operating system rule specified for patch groups using the patch baseline.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetPatchBaselineForPatchGroupResult) -> dict:
    out: dict = {}
    if "baseline_id" in value:
        out["BaselineId"] = value["baseline_id"]
    if "patch_group" in value:
        out["PatchGroup"] = value["patch_group"]
    if "operating_system" in value:
        import capo_ssm.types.operating_system

        out["OperatingSystem"] = capo_ssm.types.operating_system.serialize_aws_json_1_1(
            value["operating_system"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetPatchBaselineForPatchGroupResult:
    out: GetPatchBaselineForPatchGroupResult = {}  # type: ignore[typeddict-item]
    if data.get("BaselineId") is not None:
        out["baseline_id"] = data["BaselineId"]
    if data.get("PatchGroup") is not None:
        out["patch_group"] = data["PatchGroup"]
    if data.get("OperatingSystem") is not None:
        import capo_ssm.types.operating_system

        out["operating_system"] = (
            capo_ssm.types.operating_system.deserialize_aws_json_1_1(
                data["OperatingSystem"]
            )
        )
    return out
