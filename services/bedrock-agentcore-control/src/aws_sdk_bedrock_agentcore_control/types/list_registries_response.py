"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ListRegistriesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.next_token
    import aws_sdk_bedrock_agentcore_control.types.registry_summary_list


class ListRegistriesResponse(TypedDict):
    registries: "aws_sdk_bedrock_agentcore_control.types.registry_summary_list.RegistrySummaryList"
    """<p>The list of registry summaries. For details about the fields in each summary, see the <code>RegistrySummary</code> data type.</p>"""
    next_token: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.next_token.NextToken"
    ]
    """<p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, use this token when making another request in the <code>nextToken</code> field to return the next batch of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRegistriesResponse) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agentcore_control.types.registry_summary_list

    out["registries"] = (
        aws_sdk_bedrock_agentcore_control.types.registry_summary_list.serialize_json(
            value["registries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListRegistriesResponse:
    out: ListRegistriesResponse = {}  # type: ignore[typeddict-item]
    if "registries" in data:
        import aws_sdk_bedrock_agentcore_control.types.registry_summary_list

        out["registries"] = (
            aws_sdk_bedrock_agentcore_control.types.registry_summary_list.deserialize_json(
                data["registries"]
            )
        )
    else:
        raise DeserializationError("ListRegistriesResponse.registries required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
