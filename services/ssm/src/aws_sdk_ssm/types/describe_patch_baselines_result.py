"""Generated from Smithy shape ``com.amazonaws.ssm#DescribePatchBaselinesResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ssm.types.next_token
    import aws_sdk_ssm.types.patch_baseline_identity_list


class DescribePatchBaselinesResult(TypedDict):
    baseline_identities: NotRequired[
        "aws_sdk_ssm.types.patch_baseline_identity_list.PatchBaselineIdentityList"
    ]
    """<p>An array of <code>PatchBaselineIdentity</code> elements.</p>"""
    next_token: NotRequired["aws_sdk_ssm.types.next_token.NextToken"]
    """<p>The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribePatchBaselinesResult) -> dict:
    out: dict = {}
    if "baseline_identities" in value:
        import aws_sdk_ssm.types.patch_baseline_identity_list

        out["BaselineIdentities"] = (
            aws_sdk_ssm.types.patch_baseline_identity_list.serialize_aws_json_1_1(
                value["baseline_identities"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribePatchBaselinesResult:
    out: DescribePatchBaselinesResult = {}  # type: ignore[typeddict-item]
    if "BaselineIdentities" in data:
        import aws_sdk_ssm.types.patch_baseline_identity_list

        out["baseline_identities"] = (
            aws_sdk_ssm.types.patch_baseline_identity_list.deserialize_aws_json_1_1(
                data["BaselineIdentities"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
