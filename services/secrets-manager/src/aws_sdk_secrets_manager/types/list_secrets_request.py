"""Generated from Smithy shape ``com.amazonaws.secretsmanager#ListSecretsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_secrets_manager.types.boolean_type
    import aws_sdk_secrets_manager.types.filters_list_type
    import aws_sdk_secrets_manager.types.max_results_type
    import aws_sdk_secrets_manager.types.next_token_type
    import aws_sdk_secrets_manager.types.sort_by_type
    import aws_sdk_secrets_manager.types.sort_order_type


class ListSecretsRequest(TypedDict):
    include_planned_deletion: "aws_sdk_secrets_manager.types.boolean_type.BooleanType"
    """<p>Specifies whether to include secrets scheduled for deletion. By default, secrets scheduled for deletion aren't included.</p>"""
    max_results: NotRequired[
        "aws_sdk_secrets_manager.types.max_results_type.MaxResultsType"
    ]
    """<p>The number of results to include in the response.</p> <p>If there are more results available, in the response, Secrets Manager includes <code>NextToken</code>. To get the next results, call <code>ListSecrets</code> again with the value from <code>NextToken</code>.</p>"""
    next_token: NotRequired[
        "aws_sdk_secrets_manager.types.next_token_type.NextTokenType"
    ]
    """<p>A token that indicates where the output should continue from, if a previous call did not show all results. To get the next results, call <code>ListSecrets</code> again with this value.</p>"""
    filters: NotRequired[
        "aws_sdk_secrets_manager.types.filters_list_type.FiltersListType"
    ]
    """<p>The filters to apply to the list of secrets.</p>"""
    sort_order: NotRequired[
        "aws_sdk_secrets_manager.types.sort_order_type.SortOrderType"
    ]
    """<p>Secrets are listed by <code>CreatedDate</code>. </p>"""
    sort_by: NotRequired["aws_sdk_secrets_manager.types.sort_by_type.SortByType"]
    """<p>If not specified, secrets are listed by <code>CreatedDate</code>.</p>"""
