"""Generated from Smithy shape ``com.amazonaws.secretsmanager#BatchGetSecretValueRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_secrets_manager.types.filters_list_type
    import capo_secrets_manager.types.max_results_batch_type
    import capo_secrets_manager.types.next_token_type
    import capo_secrets_manager.types.secret_id_list_type


class BatchGetSecretValueRequest(TypedDict, closed=True):
    secret_id_list: NotRequired[
        "capo_secrets_manager.types.secret_id_list_type.SecretIdListType"
    ]
    """<p>The ARN or names of the secrets to retrieve. You must include <code>Filters</code> or <code>SecretIdList</code>, but not both.</p>"""
    filters: NotRequired["capo_secrets_manager.types.filters_list_type.FiltersListType"]
    """<p>The filters to choose which secrets to retrieve. You must include <code>Filters</code> or <code>SecretIdList</code>, but not both.</p>"""
    max_results: NotRequired[
        "capo_secrets_manager.types.max_results_batch_type.MaxResultsBatchType"
    ]
    """<p>The number of results to include in the response.</p> <p>If there are more results available, in the response, Secrets Manager includes <code>NextToken</code>. To get the next results, call <code>BatchGetSecretValue</code> again with the value from <code>NextToken</code>. To use this parameter, you must also use the <code>Filters</code> parameter.</p>"""
    next_token: NotRequired["capo_secrets_manager.types.next_token_type.NextTokenType"]
    """<p>A token that indicates where the output should continue from, if a previous call did not show all results. To get the next results, call <code>BatchGetSecretValue</code> again with this value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetSecretValueRequest) -> dict:
    out: dict = {}
    if "secret_id_list" in value:
        import capo_secrets_manager.types.secret_id_list_type

        out["SecretIdList"] = (
            capo_secrets_manager.types.secret_id_list_type.serialize_aws_json_1_1(
                value["secret_id_list"]
            )
        )
    if "filters" in value:
        import capo_secrets_manager.types.filters_list_type

        out["Filters"] = (
            capo_secrets_manager.types.filters_list_type.serialize_aws_json_1_1(
                value["filters"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetSecretValueRequest:
    out: BatchGetSecretValueRequest = {}  # type: ignore[typeddict-item]
    if "SecretIdList" in data:
        import capo_secrets_manager.types.secret_id_list_type

        out["secret_id_list"] = (
            capo_secrets_manager.types.secret_id_list_type.deserialize_aws_json_1_1(
                data["SecretIdList"]
            )
        )
    if "Filters" in data:
        import capo_secrets_manager.types.filters_list_type

        out["filters"] = (
            capo_secrets_manager.types.filters_list_type.deserialize_aws_json_1_1(
                data["Filters"]
            )
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
