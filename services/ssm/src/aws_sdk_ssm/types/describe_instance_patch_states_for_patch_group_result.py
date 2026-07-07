"""Generated from Smithy shape ``com.amazonaws.ssm#DescribeInstancePatchStatesForPatchGroupResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm.types.instance_patch_states_list
    import aws_sdk_ssm.types.next_token


class DescribeInstancePatchStatesForPatchGroupResult(TypedDict, closed=True):
    instance_patch_states: NotRequired[
        "aws_sdk_ssm.types.instance_patch_states_list.InstancePatchStatesList"
    ]
    """<p>The high-level patch state for the requested managed nodes. </p>"""
    next_token: NotRequired["aws_sdk_ssm.types.next_token.NextToken"]
    """<p>The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DescribeInstancePatchStatesForPatchGroupResult,
) -> dict:
    out: dict = {}
    if "instance_patch_states" in value:
        import aws_sdk_ssm.types.instance_patch_states_list

        out["InstancePatchStates"] = (
            aws_sdk_ssm.types.instance_patch_states_list.serialize_aws_json_1_1(
                value["instance_patch_states"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DescribeInstancePatchStatesForPatchGroupResult:
    out: DescribeInstancePatchStatesForPatchGroupResult = {}  # type: ignore[typeddict-item]
    if "InstancePatchStates" in data:
        import aws_sdk_ssm.types.instance_patch_states_list

        out["instance_patch_states"] = (
            aws_sdk_ssm.types.instance_patch_states_list.deserialize_aws_json_1_1(
                data["InstancePatchStates"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
