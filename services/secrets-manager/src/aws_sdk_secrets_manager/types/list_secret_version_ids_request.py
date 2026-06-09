"""Generated from Smithy shape ``com.amazonaws.secretsmanager#ListSecretVersionIdsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_secrets_manager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_secrets_manager.types.boolean_type
    import aws_sdk_secrets_manager.types.max_results_type
    import aws_sdk_secrets_manager.types.next_token_type
    import aws_sdk_secrets_manager.types.secret_id_type


class ListSecretVersionIdsRequest(TypedDict):
    secret_id: "aws_sdk_secrets_manager.types.secret_id_type.SecretIdType"
    """<p>The ARN or name of the secret whose versions you want to list.</p> <p>For an ARN, we recommend that you specify a complete ARN rather than a partial ARN. See <a href=\"https://docs.aws.amazon.com/secretsmanager/latest/userguide/troubleshoot.html#ARN_secretnamehyphen\">Finding a secret from a partial ARN</a>.</p>"""
    max_results: NotRequired[
        "aws_sdk_secrets_manager.types.max_results_type.MaxResultsType"
    ]
    """<p>The number of results to include in the response.</p> <p>If there are more results available, in the response, Secrets Manager includes <code>NextToken</code>. To get the next results, call <code>ListSecretVersionIds</code> again with the value from <code>NextToken</code>. </p>"""
    next_token: NotRequired[
        "aws_sdk_secrets_manager.types.next_token_type.NextTokenType"
    ]
    """<p>A token that indicates where the output should continue from, if a previous call did not show all results. To get the next results, call <code>ListSecretVersionIds</code> again with this value.</p>"""
    include_deprecated: NotRequired[
        "aws_sdk_secrets_manager.types.boolean_type.BooleanType"
    ]
    """<p>Specifies whether to include versions of secrets that don't have any staging labels attached to them. Versions without staging labels are considered deprecated and are subject to deletion by Secrets Manager. By default, versions without staging labels aren't included.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListSecretVersionIdsRequest) -> dict:
    out: dict = {}
    out["SecretId"] = value["secret_id"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "include_deprecated" in value:
        out["IncludeDeprecated"] = value["include_deprecated"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListSecretVersionIdsRequest:
    out: ListSecretVersionIdsRequest = {}  # type: ignore[typeddict-item]
    if "SecretId" in data:
        out["secret_id"] = data["SecretId"]
    else:
        raise DeserializationError("ListSecretVersionIdsRequest.secret_id required")
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "IncludeDeprecated" in data:
        out["include_deprecated"] = data["IncludeDeprecated"]
    return out
