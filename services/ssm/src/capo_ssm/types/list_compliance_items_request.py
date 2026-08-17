"""Generated from Smithy shape ``com.amazonaws.ssm#ListComplianceItemsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.compliance_resource_id_list
    import capo_ssm.types.compliance_resource_type_list
    import capo_ssm.types.compliance_string_filter_list
    import capo_ssm.types.max_results
    import capo_ssm.types.next_token


class ListComplianceItemsRequest(TypedDict, closed=True):
    filters: NotRequired[
        "capo_ssm.types.compliance_string_filter_list.ComplianceStringFilterList"
    ]
    """<p>One or more compliance filters. Use a filter to return a more specific list of results.</p>"""
    resource_ids: NotRequired[
        "capo_ssm.types.compliance_resource_id_list.ComplianceResourceIdList"
    ]
    """<p>The ID for the resources from which to get compliance information. Currently, you can only specify one resource ID.</p>"""
    resource_types: NotRequired[
        "capo_ssm.types.compliance_resource_type_list.ComplianceResourceTypeList"
    ]
    """<p>The type of resource from which to get compliance information. Currently, the only supported resource type is <code>ManagedInstance</code>.</p>"""
    next_token: NotRequired["capo_ssm.types.next_token.NextToken"]
    """<p>A token to start the list. Use this token to get the next set of results. </p>"""
    max_results: NotRequired["capo_ssm.types.max_results.MaxResults"]
    """<p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListComplianceItemsRequest) -> dict:
    out: dict = {}
    if "filters" in value:
        import capo_ssm.types.compliance_string_filter_list

        out["Filters"] = (
            capo_ssm.types.compliance_string_filter_list.serialize_aws_json_1_1(
                value["filters"]
            )
        )
    if "resource_ids" in value:
        import capo_ssm.types.compliance_resource_id_list

        out["ResourceIds"] = (
            capo_ssm.types.compliance_resource_id_list.serialize_aws_json_1_1(
                value["resource_ids"]
            )
        )
    if "resource_types" in value:
        import capo_ssm.types.compliance_resource_type_list

        out["ResourceTypes"] = (
            capo_ssm.types.compliance_resource_type_list.serialize_aws_json_1_1(
                value["resource_types"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListComplianceItemsRequest:
    out: ListComplianceItemsRequest = {}  # type: ignore[typeddict-item]
    if data.get("Filters") is not None:
        import capo_ssm.types.compliance_string_filter_list

        out["filters"] = (
            capo_ssm.types.compliance_string_filter_list.deserialize_aws_json_1_1(
                data["Filters"]
            )
        )
    if data.get("ResourceIds") is not None:
        import capo_ssm.types.compliance_resource_id_list

        out["resource_ids"] = (
            capo_ssm.types.compliance_resource_id_list.deserialize_aws_json_1_1(
                data["ResourceIds"]
            )
        )
    if data.get("ResourceTypes") is not None:
        import capo_ssm.types.compliance_resource_type_list

        out["resource_types"] = (
            capo_ssm.types.compliance_resource_type_list.deserialize_aws_json_1_1(
                data["ResourceTypes"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out
