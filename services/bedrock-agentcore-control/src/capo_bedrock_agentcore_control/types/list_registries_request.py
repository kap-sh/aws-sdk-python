"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ListRegistriesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.max_results
    import capo_bedrock_agentcore_control.types.next_token
    import capo_bedrock_agentcore_control.types.registry_authorizer_type
    import capo_bedrock_agentcore_control.types.registry_status


class ListRegistriesRequest(TypedDict, closed=True):
    max_results: NotRequired[
        "capo_bedrock_agentcore_control.types.max_results.MaxResults"
    ]
    """<p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>"""
    next_token: NotRequired["capo_bedrock_agentcore_control.types.next_token.NextToken"]
    """<p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>"""
    status: NotRequired[
        "capo_bedrock_agentcore_control.types.registry_status.RegistryStatus"
    ]
    """<p>Filter registries by their current status. Possible values include <code>CREATING</code>, <code>READY</code>, <code>UPDATING</code>, <code>CREATE_FAILED</code>, <code>UPDATE_FAILED</code>, <code>DELETING</code>, and <code>DELETE_FAILED</code>.</p>"""
    authorizer_type: NotRequired[
        "capo_bedrock_agentcore_control.types.registry_authorizer_type.RegistryAuthorizerType"
    ]
    """<p>Filter registries by their authorizer type. Possible values are <code>CUSTOM_JWT</code> and <code>AWS_IAM</code>. For more information about authorizer types, see the <code>RegistryAuthorizerType</code> enum.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRegistriesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListRegistriesRequest:
    out: ListRegistriesRequest = {}  # type: ignore[typeddict-item]
    return out
