"""Generated from Smithy shape ``com.amazonaws.socialmessaging#ListWhatsAppFlowsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_socialmessaging.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_socialmessaging.types.meta_flow_summary_list
    import aws_sdk_socialmessaging.types.next_token


class ListWhatsAppFlowsOutput(TypedDict):
    flows: "aws_sdk_socialmessaging.types.meta_flow_summary_list.MetaFlowSummaryList"
    """<p>A list of Flow summaries.</p>"""
    next_token: NotRequired["aws_sdk_socialmessaging.types.next_token.NextToken"]
    """<p>The token to retrieve the next page of results, if any.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListWhatsAppFlowsOutput) -> dict:
    out: dict = {}
    import aws_sdk_socialmessaging.types.meta_flow_summary_list

    out["flows"] = aws_sdk_socialmessaging.types.meta_flow_summary_list.serialize_json(
        value["flows"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListWhatsAppFlowsOutput:
    out: ListWhatsAppFlowsOutput = {}  # type: ignore[typeddict-item]
    if "flows" in data:
        import aws_sdk_socialmessaging.types.meta_flow_summary_list

        out["flows"] = (
            aws_sdk_socialmessaging.types.meta_flow_summary_list.deserialize_json(
                data["flows"]
            )
        )
    else:
        raise DeserializationError("ListWhatsAppFlowsOutput.flows required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
