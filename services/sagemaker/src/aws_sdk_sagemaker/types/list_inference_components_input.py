"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListInferenceComponentsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.endpoint_name
    import aws_sdk_sagemaker.types.inference_component_name_contains
    import aws_sdk_sagemaker.types.inference_component_sort_key
    import aws_sdk_sagemaker.types.inference_component_status
    import aws_sdk_sagemaker.types.max_results
    import aws_sdk_sagemaker.types.order_key
    import aws_sdk_sagemaker.types.pagination_token
    import aws_sdk_sagemaker.types.timestamp
    import aws_sdk_sagemaker.types.variant_name


class ListInferenceComponentsInput(TypedDict):
    sort_by: NotRequired[
        "aws_sdk_sagemaker.types.inference_component_sort_key.InferenceComponentSortKey"
    ]
    """<p>The field by which to sort the inference components in the response. The default is <code>CreationTime</code>.</p>"""
    sort_order: NotRequired["aws_sdk_sagemaker.types.order_key.OrderKey"]
    """<p>The sort order for results. The default is <code>Descending</code>.</p>"""
    next_token: NotRequired["aws_sdk_sagemaker.types.pagination_token.PaginationToken"]
    """<p>A token that you use to get the next set of results following a truncated response. If the response to the previous request was truncated, that response provides the value for this token.</p>"""
    max_results: NotRequired["aws_sdk_sagemaker.types.max_results.MaxResults"]
    """<p>The maximum number of inference components to return in the response. This value defaults to 10.</p>"""
    name_contains: NotRequired[
        "aws_sdk_sagemaker.types.inference_component_name_contains.InferenceComponentNameContains"
    ]
    """<p>Filters the results to only those inference components with a name that contains the specified string.</p>"""
    creation_time_before: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>Filters the results to only those inference components that were created before the specified time.</p>"""
    creation_time_after: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>Filters the results to only those inference components that were created after the specified time.</p>"""
    last_modified_time_before: NotRequired[
        "aws_sdk_sagemaker.types.timestamp.Timestamp"
    ]
    """<p>Filters the results to only those inference components that were updated before the specified time.</p>"""
    last_modified_time_after: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>Filters the results to only those inference components that were updated after the specified time.</p>"""
    status_equals: NotRequired[
        "aws_sdk_sagemaker.types.inference_component_status.InferenceComponentStatus"
    ]
    """<p>Filters the results to only those inference components with the specified status.</p>"""
    endpoint_name_equals: NotRequired[
        "aws_sdk_sagemaker.types.endpoint_name.EndpointName"
    ]
    """<p>An endpoint name to filter the listed inference components. The response includes only those inference components that are hosted at the specified endpoint.</p>"""
    variant_name_equals: NotRequired["aws_sdk_sagemaker.types.variant_name.VariantName"]
    """<p>A production variant name to filter the listed inference components. The response includes only those inference components that are hosted at the specified variant.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListInferenceComponentsInput) -> dict:
    out: dict = {}
    if "sort_by" in value:
        import aws_sdk_sagemaker.types.inference_component_sort_key

        out["SortBy"] = (
            aws_sdk_sagemaker.types.inference_component_sort_key.serialize_aws_json_1_1(
                value["sort_by"]
            )
        )
    if "sort_order" in value:
        import aws_sdk_sagemaker.types.order_key

        out["SortOrder"] = aws_sdk_sagemaker.types.order_key.serialize_aws_json_1_1(
            value["sort_order"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "name_contains" in value:
        out["NameContains"] = value["name_contains"]
    if "creation_time_before" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["CreationTimeBefore"] = (
            aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["creation_time_before"]
            )
        )
    if "creation_time_after" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["CreationTimeAfter"] = (
            aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["creation_time_after"]
            )
        )
    if "last_modified_time_before" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["LastModifiedTimeBefore"] = (
            aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["last_modified_time_before"]
            )
        )
    if "last_modified_time_after" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["LastModifiedTimeAfter"] = (
            aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["last_modified_time_after"]
            )
        )
    if "status_equals" in value:
        import aws_sdk_sagemaker.types.inference_component_status

        out["StatusEquals"] = (
            aws_sdk_sagemaker.types.inference_component_status.serialize_aws_json_1_1(
                value["status_equals"]
            )
        )
    if "endpoint_name_equals" in value:
        out["EndpointNameEquals"] = value["endpoint_name_equals"]
    if "variant_name_equals" in value:
        out["VariantNameEquals"] = value["variant_name_equals"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListInferenceComponentsInput:
    out: ListInferenceComponentsInput = {}  # type: ignore[typeddict-item]
    if "SortBy" in data:
        import aws_sdk_sagemaker.types.inference_component_sort_key

        out["sort_by"] = (
            aws_sdk_sagemaker.types.inference_component_sort_key.deserialize_aws_json_1_1(
                data["SortBy"]
            )
        )
    if "SortOrder" in data:
        import aws_sdk_sagemaker.types.order_key

        out["sort_order"] = aws_sdk_sagemaker.types.order_key.deserialize_aws_json_1_1(
            data["SortOrder"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NameContains" in data:
        out["name_contains"] = data["NameContains"]
    if "CreationTimeBefore" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["creation_time_before"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTimeBefore"]
            )
        )
    if "CreationTimeAfter" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["creation_time_after"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTimeAfter"]
            )
        )
    if "LastModifiedTimeBefore" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["last_modified_time_before"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTimeBefore"]
            )
        )
    if "LastModifiedTimeAfter" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["last_modified_time_after"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTimeAfter"]
            )
        )
    if "StatusEquals" in data:
        import aws_sdk_sagemaker.types.inference_component_status

        out["status_equals"] = (
            aws_sdk_sagemaker.types.inference_component_status.deserialize_aws_json_1_1(
                data["StatusEquals"]
            )
        )
    if "EndpointNameEquals" in data:
        out["endpoint_name_equals"] = data["EndpointNameEquals"]
    if "VariantNameEquals" in data:
        out["variant_name_equals"] = data["VariantNameEquals"]
    return out
