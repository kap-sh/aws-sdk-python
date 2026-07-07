"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ListRegistryRecordsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.descriptor_type
    import aws_sdk_bedrock_agentcore_control.types.max_results
    import aws_sdk_bedrock_agentcore_control.types.next_token
    import aws_sdk_bedrock_agentcore_control.types.registry_identifier
    import aws_sdk_bedrock_agentcore_control.types.registry_record_name
    import aws_sdk_bedrock_agentcore_control.types.registry_record_status


class ListRegistryRecordsRequest(TypedDict, closed=True):
    registry_id: (
        "aws_sdk_bedrock_agentcore_control.types.registry_identifier.RegistryIdentifier"
    )
    """<p>The identifier of the registry to list records from. You can specify either the Amazon Resource Name (ARN) or the ID of the registry.</p>"""
    max_results: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.max_results.MaxResults"
    ]
    """<p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>"""
    next_token: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.next_token.NextToken"
    ]
    """<p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>"""
    name: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.registry_record_name.RegistryRecordName"
    ]
    """<p>Filter registry records by name.</p>"""
    status: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.registry_record_status.RegistryRecordStatus"
    ]
    """<p>Filter registry records by their current status. Possible values include <code>CREATING</code>, <code>DRAFT</code>, <code>APPROVED</code>, <code>PENDING_APPROVAL</code>, <code>REJECTED</code>, <code>DEPRECATED</code>, <code>UPDATING</code>, <code>CREATE_FAILED</code>, and <code>UPDATE_FAILED</code>.</p>"""
    descriptor_type: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.descriptor_type.DescriptorType"
    ]
    """<p>Filter registry records by their descriptor type. Possible values are <code>MCP</code>, <code>A2A</code>, <code>CUSTOM</code>, and <code>AGENT_SKILLS</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRegistryRecordsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListRegistryRecordsRequest:
    out: ListRegistryRecordsRequest = {}  # type: ignore[typeddict-item]
    return out
