"""Generated from Smithy shape ``com.amazonaws.ssm#DescribeInstancePatchStatesForPatchGroupRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.instance_patch_state_filter_list
    import aws_sdk_ssm.types.next_token
    import aws_sdk_ssm.types.patch_compliance_max_results
    import aws_sdk_ssm.types.patch_group


class DescribeInstancePatchStatesForPatchGroupRequest(TypedDict):
    patch_group: "aws_sdk_ssm.types.patch_group.PatchGroup"
    """<p>The name of the patch group for which the patch state information should be retrieved.</p>"""
    filters: NotRequired[
        "aws_sdk_ssm.types.instance_patch_state_filter_list.InstancePatchStateFilterList"
    ]
    r"""<p>Each entry in the array is a structure containing:</p> <ul> <li> <p>Key (string between 1 and 200 characters)</p> </li> <li> <p>Values (array containing a single string)</p> </li> <li> <p>Type (string \"Equal\", \"NotEqual\", \"LessThan\", \"GreaterThan\")</p> </li> </ul>"""
    next_token: NotRequired["aws_sdk_ssm.types.next_token.NextToken"]
    """<p>The token for the next set of items to return. (You received this token from a previous call.)</p>"""
    max_results: NotRequired[
        "aws_sdk_ssm.types.patch_compliance_max_results.PatchComplianceMaxResults"
    ]
    """<p>The maximum number of patches to return (per page).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DescribeInstancePatchStatesForPatchGroupRequest,
) -> dict:
    out: dict = {}
    out["PatchGroup"] = value["patch_group"]
    if "filters" in value:
        import aws_sdk_ssm.types.instance_patch_state_filter_list

        out["Filters"] = (
            aws_sdk_ssm.types.instance_patch_state_filter_list.serialize_aws_json_1_1(
                value["filters"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DescribeInstancePatchStatesForPatchGroupRequest:
    out: DescribeInstancePatchStatesForPatchGroupRequest = {}  # type: ignore[typeddict-item]
    if "PatchGroup" in data:
        out["patch_group"] = data["PatchGroup"]
    else:
        raise DeserializationError(
            "DescribeInstancePatchStatesForPatchGroupRequest.patch_group required"
        )
    if "Filters" in data:
        import aws_sdk_ssm.types.instance_patch_state_filter_list

        out["filters"] = (
            aws_sdk_ssm.types.instance_patch_state_filter_list.deserialize_aws_json_1_1(
                data["Filters"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
