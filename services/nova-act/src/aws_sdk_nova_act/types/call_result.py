"""Generated from Smithy shape ``com.amazonaws.novaact#CallResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_nova_act.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_nova_act.types.call_id
    import aws_sdk_nova_act.types.call_result_contents


class CallResult(TypedDict, closed=True):
    call_id: NotRequired["aws_sdk_nova_act.types.call_id.CallId"]
    """<p>The identifier of the tool call that this result corresponds to.</p>"""
    content: "aws_sdk_nova_act.types.call_result_contents.CallResultContents"
    """<p>The content returned by the tool execution, which can include text or other media types.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CallResult) -> dict:
    out: dict = {}
    if "call_id" in value:
        out["callId"] = value["call_id"]
    import aws_sdk_nova_act.types.call_result_contents

    out["content"] = aws_sdk_nova_act.types.call_result_contents.serialize_json(
        value["content"]
    )
    return out


def deserialize_json(data: dict) -> CallResult:
    out: CallResult = {}  # type: ignore[typeddict-item]
    if "callId" in data:
        out["call_id"] = data["callId"]
    if "content" in data:
        import aws_sdk_nova_act.types.call_result_contents

        out["content"] = aws_sdk_nova_act.types.call_result_contents.deserialize_json(
            data["content"]
        )
    else:
        raise DeserializationError("CallResult.content required")
    return out
