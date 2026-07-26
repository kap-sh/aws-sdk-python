"""Generated from Smithy shape ``com.amazonaws.ssm#DescribeInstancePropertiesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.describe_instance_properties_max_results
    import capo_ssm.types.instance_property_filter_list
    import capo_ssm.types.instance_property_string_filter_list
    import capo_ssm.types.next_token


class DescribeInstancePropertiesRequest(TypedDict, closed=True):
    instance_property_filter_list: NotRequired[
        "capo_ssm.types.instance_property_filter_list.InstancePropertyFilterList"
    ]
    """<p>An array of instance property filters.</p>"""
    filters_with_operator: NotRequired[
        "capo_ssm.types.instance_property_string_filter_list.InstancePropertyStringFilterList"
    ]
    """<p>The request filters to use with the operator.</p>"""
    max_results: NotRequired[
        "capo_ssm.types.describe_instance_properties_max_results.DescribeInstancePropertiesMaxResults"
    ]
    """<p>The maximum number of items to return for the call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>"""
    next_token: NotRequired["capo_ssm.types.next_token.NextToken"]
    """<p>The token provided by a previous request to use to return the next set of properties.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeInstancePropertiesRequest) -> dict:
    out: dict = {}
    if "instance_property_filter_list" in value:
        import capo_ssm.types.instance_property_filter_list

        out["InstancePropertyFilterList"] = (
            capo_ssm.types.instance_property_filter_list.serialize_aws_json_1_1(
                value["instance_property_filter_list"]
            )
        )
    if "filters_with_operator" in value:
        import capo_ssm.types.instance_property_string_filter_list

        out["FiltersWithOperator"] = (
            capo_ssm.types.instance_property_string_filter_list.serialize_aws_json_1_1(
                value["filters_with_operator"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeInstancePropertiesRequest:
    out: DescribeInstancePropertiesRequest = {}  # type: ignore[typeddict-item]
    if "InstancePropertyFilterList" in data:
        import capo_ssm.types.instance_property_filter_list

        out["instance_property_filter_list"] = (
            capo_ssm.types.instance_property_filter_list.deserialize_aws_json_1_1(
                data["InstancePropertyFilterList"]
            )
        )
    if "FiltersWithOperator" in data:
        import capo_ssm.types.instance_property_string_filter_list

        out["filters_with_operator"] = (
            capo_ssm.types.instance_property_string_filter_list.deserialize_aws_json_1_1(
                data["FiltersWithOperator"]
            )
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
