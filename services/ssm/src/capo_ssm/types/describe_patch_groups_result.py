"""Generated from Smithy shape ``com.amazonaws.ssm#DescribePatchGroupsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.next_token
    import capo_ssm.types.patch_group_patch_baseline_mapping_list


class DescribePatchGroupsResult(TypedDict, closed=True):
    mappings: NotRequired[
        "capo_ssm.types.patch_group_patch_baseline_mapping_list.PatchGroupPatchBaselineMappingList"
    ]
    r"""<p>Each entry in the array contains:</p> <ul> <li> <p> <code>PatchGroup</code>: string (between 1 and 256 characters. Regex: <code>^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$)</code> </p> </li> <li> <p> <code>PatchBaselineIdentity</code>: A <code>PatchBaselineIdentity</code> element.</p> </li> </ul>"""
    next_token: NotRequired["capo_ssm.types.next_token.NextToken"]
    """<p>The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribePatchGroupsResult) -> dict:
    out: dict = {}
    if "mappings" in value:
        import capo_ssm.types.patch_group_patch_baseline_mapping_list

        out["Mappings"] = (
            capo_ssm.types.patch_group_patch_baseline_mapping_list.serialize_aws_json_1_1(
                value["mappings"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribePatchGroupsResult:
    out: DescribePatchGroupsResult = {}  # type: ignore[typeddict-item]
    if data.get("Mappings") is not None:
        import capo_ssm.types.patch_group_patch_baseline_mapping_list

        out["mappings"] = (
            capo_ssm.types.patch_group_patch_baseline_mapping_list.deserialize_aws_json_1_1(
                data["Mappings"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
