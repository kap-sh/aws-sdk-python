"""Generated from Smithy shape ``com.amazonaws.ssm#DescribeAvailablePatchesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm.types.next_token
    import aws_sdk_ssm.types.patch_list


class DescribeAvailablePatchesResult(TypedDict, closed=True):
    patches: NotRequired["aws_sdk_ssm.types.patch_list.PatchList"]
    """<p>An array of patches. Each entry in the array is a patch structure.</p>"""
    next_token: NotRequired["aws_sdk_ssm.types.next_token.NextToken"]
    """<p>The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAvailablePatchesResult) -> dict:
    out: dict = {}
    if "patches" in value:
        import aws_sdk_ssm.types.patch_list

        out["Patches"] = aws_sdk_ssm.types.patch_list.serialize_aws_json_1_1(
            value["patches"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAvailablePatchesResult:
    out: DescribeAvailablePatchesResult = {}  # type: ignore[typeddict-item]
    if "Patches" in data:
        import aws_sdk_ssm.types.patch_list

        out["patches"] = aws_sdk_ssm.types.patch_list.deserialize_aws_json_1_1(
            data["Patches"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
