"""Generated from Smithy shape ``com.amazonaws.secretsmanager#ListSecretsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_secrets_manager.types.boolean_type
    import capo_secrets_manager.types.filters_list_type
    import capo_secrets_manager.types.max_results_type
    import capo_secrets_manager.types.next_token_type
    import capo_secrets_manager.types.sort_by_type
    import capo_secrets_manager.types.sort_order_type


class ListSecretsRequest(TypedDict, closed=True):
    include_planned_deletion: NotRequired[
        "capo_secrets_manager.types.boolean_type.BooleanType"
    ]
    """<p>Specifies whether to include secrets scheduled for deletion. By default, secrets scheduled for deletion aren't included.</p>"""
    max_results: NotRequired[
        "capo_secrets_manager.types.max_results_type.MaxResultsType"
    ]
    """<p>The number of results to include in the response.</p> <p>If there are more results available, in the response, Secrets Manager includes <code>NextToken</code>. To get the next results, call <code>ListSecrets</code> again with the value from <code>NextToken</code>.</p>"""
    next_token: NotRequired["capo_secrets_manager.types.next_token_type.NextTokenType"]
    """<p>A token that indicates where the output should continue from, if a previous call did not show all results. To get the next results, call <code>ListSecrets</code> again with this value.</p>"""
    filters: NotRequired["capo_secrets_manager.types.filters_list_type.FiltersListType"]
    """<p>The filters to apply to the list of secrets.</p>"""
    sort_order: NotRequired["capo_secrets_manager.types.sort_order_type.SortOrderType"]
    """<p>Secrets are listed by <code>CreatedDate</code>. </p>"""
    sort_by: NotRequired["capo_secrets_manager.types.sort_by_type.SortByType"]
    """<p>If not specified, secrets are listed by <code>CreatedDate</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListSecretsRequest) -> dict:
    out: dict = {}
    if "include_planned_deletion" in value:
        out["IncludePlannedDeletion"] = value["include_planned_deletion"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "filters" in value:
        import capo_secrets_manager.types.filters_list_type

        out["Filters"] = (
            capo_secrets_manager.types.filters_list_type.serialize_aws_json_1_1(
                value["filters"]
            )
        )
    if "sort_order" in value:
        import capo_secrets_manager.types.sort_order_type

        out["SortOrder"] = (
            capo_secrets_manager.types.sort_order_type.serialize_aws_json_1_1(
                value["sort_order"]
            )
        )
    if "sort_by" in value:
        import capo_secrets_manager.types.sort_by_type

        out["SortBy"] = capo_secrets_manager.types.sort_by_type.serialize_aws_json_1_1(
            value["sort_by"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListSecretsRequest:
    out: ListSecretsRequest = {}  # type: ignore[typeddict-item]
    if data.get("IncludePlannedDeletion") is not None:
        out["include_planned_deletion"] = data["IncludePlannedDeletion"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("Filters") is not None:
        import capo_secrets_manager.types.filters_list_type

        out["filters"] = (
            capo_secrets_manager.types.filters_list_type.deserialize_aws_json_1_1(
                data["Filters"]
            )
        )
    if data.get("SortOrder") is not None:
        import capo_secrets_manager.types.sort_order_type

        out["sort_order"] = (
            capo_secrets_manager.types.sort_order_type.deserialize_aws_json_1_1(
                data["SortOrder"]
            )
        )
    if data.get("SortBy") is not None:
        import capo_secrets_manager.types.sort_by_type

        out["sort_by"] = (
            capo_secrets_manager.types.sort_by_type.deserialize_aws_json_1_1(
                data["SortBy"]
            )
        )
    return out
