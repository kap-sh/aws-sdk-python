"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ListHarnessesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.harness_summaries
    import aws_sdk_bedrock_agentcore_control.types.next_token


class ListHarnessesResponse(TypedDict):
    harnesses: (
        "aws_sdk_bedrock_agentcore_control.types.harness_summaries.HarnessSummaries"
    )
    """<p>The list of harness summaries.</p>"""
    next_token: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.next_token.NextToken"
    ]
    """<p>The token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListHarnessesResponse) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agentcore_control.types.harness_summaries

    out["harnesses"] = (
        aws_sdk_bedrock_agentcore_control.types.harness_summaries.serialize_json(
            value["harnesses"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListHarnessesResponse:
    out: ListHarnessesResponse = {}  # type: ignore[typeddict-item]
    if "harnesses" in data:
        import aws_sdk_bedrock_agentcore_control.types.harness_summaries

        out["harnesses"] = (
            aws_sdk_bedrock_agentcore_control.types.harness_summaries.deserialize_json(
                data["harnesses"]
            )
        )
    else:
        raise DeserializationError("ListHarnessesResponse.harnesses required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
