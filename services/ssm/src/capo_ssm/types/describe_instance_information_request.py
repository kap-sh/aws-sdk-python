"""Generated from Smithy shape ``com.amazonaws.ssm#DescribeInstanceInformationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.instance_information_filter_list
    import capo_ssm.types.instance_information_string_filter_list
    import capo_ssm.types.max_results_ec2_compatible
    import capo_ssm.types.next_token


class DescribeInstanceInformationRequest(TypedDict, closed=True):
    instance_information_filter_list: NotRequired[
        "capo_ssm.types.instance_information_filter_list.InstanceInformationFilterList"
    ]
    """<p>This is a legacy method. We recommend that you don't use this method. Instead, use the <code>Filters</code> data type. <code>Filters</code> enables you to return node information by filtering based on tags applied to managed nodes.</p> <note> <p>Attempting to use <code>InstanceInformationFilterList</code> and <code>Filters</code> leads to an exception error. </p> </note>"""
    filters: NotRequired[
        "capo_ssm.types.instance_information_string_filter_list.InstanceInformationStringFilterList"
    ]
    """<p>One or more filters. Use a filter to return a more specific list of managed nodes. You can filter based on tags applied to your managed nodes. Tag filters can't be combined with other filter types. Use this <code>Filters</code> data type instead of <code>InstanceInformationFilterList</code>, which is deprecated.</p>"""
    max_results: NotRequired[
        "capo_ssm.types.max_results_ec2_compatible.MaxResultsEC2Compatible"
    ]
    """<p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results. The default value is 10 items. </p>"""
    next_token: NotRequired["capo_ssm.types.next_token.NextToken"]
    """<p>The token for the next set of items to return. (You received this token from a previous call.)</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeInstanceInformationRequest) -> dict:
    out: dict = {}
    if "instance_information_filter_list" in value:
        import capo_ssm.types.instance_information_filter_list

        out["InstanceInformationFilterList"] = (
            capo_ssm.types.instance_information_filter_list.serialize_aws_json_1_1(
                value["instance_information_filter_list"]
            )
        )
    if "filters" in value:
        import capo_ssm.types.instance_information_string_filter_list

        out["Filters"] = (
            capo_ssm.types.instance_information_string_filter_list.serialize_aws_json_1_1(
                value["filters"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeInstanceInformationRequest:
    out: DescribeInstanceInformationRequest = {}  # type: ignore[typeddict-item]
    if data.get("InstanceInformationFilterList") is not None:
        import capo_ssm.types.instance_information_filter_list

        out["instance_information_filter_list"] = (
            capo_ssm.types.instance_information_filter_list.deserialize_aws_json_1_1(
                data["InstanceInformationFilterList"]
            )
        )
    if data.get("Filters") is not None:
        import capo_ssm.types.instance_information_string_filter_list

        out["filters"] = (
            capo_ssm.types.instance_information_string_filter_list.deserialize_aws_json_1_1(
                data["Filters"]
            )
        )
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
