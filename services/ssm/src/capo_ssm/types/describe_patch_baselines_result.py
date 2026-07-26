"""Generated from Smithy shape ``com.amazonaws.ssm#DescribePatchBaselinesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.next_token
    import capo_ssm.types.patch_baseline_identity_list


class DescribePatchBaselinesResult(TypedDict, closed=True):
    baseline_identities: NotRequired[
        "capo_ssm.types.patch_baseline_identity_list.PatchBaselineIdentityList"
    ]
    """<p>An array of <code>PatchBaselineIdentity</code> elements.</p>"""
    next_token: NotRequired["capo_ssm.types.next_token.NextToken"]
    """<p>The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribePatchBaselinesResult) -> dict:
    out: dict = {}
    if "baseline_identities" in value:
        import capo_ssm.types.patch_baseline_identity_list

        out["BaselineIdentities"] = (
            capo_ssm.types.patch_baseline_identity_list.serialize_aws_json_1_1(
                value["baseline_identities"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribePatchBaselinesResult:
    out: DescribePatchBaselinesResult = {}  # type: ignore[typeddict-item]
    if "BaselineIdentities" in data:
        import capo_ssm.types.patch_baseline_identity_list

        out["baseline_identities"] = (
            capo_ssm.types.patch_baseline_identity_list.deserialize_aws_json_1_1(
                data["BaselineIdentities"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
