"""Generated from Smithy shape ``com.amazonaws.inspector#PreviewAgentsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_inspector.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector.types.agent_preview_list
    import aws_sdk_inspector.types.pagination_token


class PreviewAgentsResponse(TypedDict):
    agent_previews: "aws_sdk_inspector.types.agent_preview_list.AgentPreviewList"
    """<p>The resulting list of agents.</p>"""
    next_token: NotRequired["aws_sdk_inspector.types.pagination_token.PaginationToken"]
    """<p> When a response is generated, if there is more data to be listed, this parameter is present in the response and contains the value to use for the <b>nextToken</b> parameter in a subsequent pagination request. If there is no more data to be listed, this parameter is set to null.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PreviewAgentsResponse) -> dict:
    out: dict = {}
    import aws_sdk_inspector.types.agent_preview_list

    out["agentPreviews"] = (
        aws_sdk_inspector.types.agent_preview_list.serialize_aws_json_1_1(
            value["agent_previews"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PreviewAgentsResponse:
    out: PreviewAgentsResponse = {}  # type: ignore[typeddict-item]
    if "agentPreviews" in data:
        import aws_sdk_inspector.types.agent_preview_list

        out["agent_previews"] = (
            aws_sdk_inspector.types.agent_preview_list.deserialize_aws_json_1_1(
                data["agentPreviews"]
            )
        )
    else:
        raise DeserializationError("PreviewAgentsResponse.agent_previews required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
