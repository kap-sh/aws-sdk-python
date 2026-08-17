"""Generated from Smithy shape ``com.amazonaws.ssm#DescribeEffectivePatchesForPatchBaselineResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.effective_patch_list
    import capo_ssm.types.next_token


class DescribeEffectivePatchesForPatchBaselineResult(TypedDict, closed=True):
    effective_patches: NotRequired[
        "capo_ssm.types.effective_patch_list.EffectivePatchList"
    ]
    """<p>An array of patches and patch status.</p>"""
    next_token: NotRequired["capo_ssm.types.next_token.NextToken"]
    """<p>The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DescribeEffectivePatchesForPatchBaselineResult,
) -> dict:
    out: dict = {}
    if "effective_patches" in value:
        import capo_ssm.types.effective_patch_list

        out["EffectivePatches"] = (
            capo_ssm.types.effective_patch_list.serialize_aws_json_1_1(
                value["effective_patches"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DescribeEffectivePatchesForPatchBaselineResult:
    out: DescribeEffectivePatchesForPatchBaselineResult = {}  # type: ignore[typeddict-item]
    if data.get("EffectivePatches") is not None:
        import capo_ssm.types.effective_patch_list

        out["effective_patches"] = (
            capo_ssm.types.effective_patch_list.deserialize_aws_json_1_1(
                data["EffectivePatches"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
