"""Generated from Smithy shape ``com.amazonaws.ssm#DescribeInstancePropertiesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ssm.types.describe_instance_properties_max_results
    import aws_sdk_ssm.types.instance_property_filter_list
    import aws_sdk_ssm.types.instance_property_string_filter_list
    import aws_sdk_ssm.types.next_token


class DescribeInstancePropertiesRequest(TypedDict):
    instance_property_filter_list: NotRequired[
        "aws_sdk_ssm.types.instance_property_filter_list.InstancePropertyFilterList"
    ]
    """<p>An array of instance property filters.</p>"""
    filters_with_operator: NotRequired[
        "aws_sdk_ssm.types.instance_property_string_filter_list.InstancePropertyStringFilterList"
    ]
    """<p>The request filters to use with the operator.</p>"""
    max_results: NotRequired[
        "aws_sdk_ssm.types.describe_instance_properties_max_results.DescribeInstancePropertiesMaxResults"
    ]
    """<p>The maximum number of items to return for the call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>"""
    next_token: NotRequired["aws_sdk_ssm.types.next_token.NextToken"]
    """<p>The token provided by a previous request to use to return the next set of properties.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeInstancePropertiesRequest) -> dict:
    out: dict = {}
    if "instance_property_filter_list" in value:
        import aws_sdk_ssm.types.instance_property_filter_list

        out["InstancePropertyFilterList"] = (
            aws_sdk_ssm.types.instance_property_filter_list.serialize_aws_json_1_1(
                value["instance_property_filter_list"]
            )
        )
    if "filters_with_operator" in value:
        import aws_sdk_ssm.types.instance_property_string_filter_list

        out["FiltersWithOperator"] = (
            aws_sdk_ssm.types.instance_property_string_filter_list.serialize_aws_json_1_1(
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
        import aws_sdk_ssm.types.instance_property_filter_list

        out["instance_property_filter_list"] = (
            aws_sdk_ssm.types.instance_property_filter_list.deserialize_aws_json_1_1(
                data["InstancePropertyFilterList"]
            )
        )
    if "FiltersWithOperator" in data:
        import aws_sdk_ssm.types.instance_property_string_filter_list

        out["filters_with_operator"] = (
            aws_sdk_ssm.types.instance_property_string_filter_list.deserialize_aws_json_1_1(
                data["FiltersWithOperator"]
            )
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
