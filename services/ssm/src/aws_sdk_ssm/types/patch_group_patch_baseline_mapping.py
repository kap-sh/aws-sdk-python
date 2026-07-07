"""Generated from Smithy shape ``com.amazonaws.ssm#PatchGroupPatchBaselineMapping``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm.types.patch_baseline_identity
    import aws_sdk_ssm.types.patch_group


class PatchGroupPatchBaselineMapping(TypedDict, closed=True):
    patch_group: NotRequired["aws_sdk_ssm.types.patch_group.PatchGroup"]
    """<p>The name of the patch group registered with the patch baseline.</p>"""
    baseline_identity: NotRequired[
        "aws_sdk_ssm.types.patch_baseline_identity.PatchBaselineIdentity"
    ]
    """<p>The patch baseline the patch group is registered with.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PatchGroupPatchBaselineMapping) -> dict:
    out: dict = {}
    if "patch_group" in value:
        out["PatchGroup"] = value["patch_group"]
    if "baseline_identity" in value:
        import aws_sdk_ssm.types.patch_baseline_identity

        out["BaselineIdentity"] = (
            aws_sdk_ssm.types.patch_baseline_identity.serialize_aws_json_1_1(
                value["baseline_identity"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PatchGroupPatchBaselineMapping:
    out: PatchGroupPatchBaselineMapping = {}  # type: ignore[typeddict-item]
    if "PatchGroup" in data:
        out["patch_group"] = data["PatchGroup"]
    if "BaselineIdentity" in data:
        import aws_sdk_ssm.types.patch_baseline_identity

        out["baseline_identity"] = (
            aws_sdk_ssm.types.patch_baseline_identity.deserialize_aws_json_1_1(
                data["BaselineIdentity"]
            )
        )
    return out
