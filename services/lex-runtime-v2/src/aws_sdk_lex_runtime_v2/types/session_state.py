"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#SessionState``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_runtime_v2.types.active_contexts_list
    import aws_sdk_lex_runtime_v2.types.dialog_action
    import aws_sdk_lex_runtime_v2.types.intent
    import aws_sdk_lex_runtime_v2.types.non_empty_string
    import aws_sdk_lex_runtime_v2.types.runtime_hints
    import aws_sdk_lex_runtime_v2.types.string_map


class SessionState(TypedDict, closed=True):
    dialog_action: NotRequired[
        "aws_sdk_lex_runtime_v2.types.dialog_action.DialogAction"
    ]
    """<p>The next step that Amazon Lex V2 should take in the conversation with a user.</p>"""
    intent: NotRequired["aws_sdk_lex_runtime_v2.types.intent.Intent"]
    """<p>The active intent that Amazon Lex V2 is processing.</p>"""
    active_contexts: NotRequired[
        "aws_sdk_lex_runtime_v2.types.active_contexts_list.ActiveContextsList"
    ]
    """<p>One or more contexts that indicate to Amazon Lex V2 the context of a request. When a context is active, Amazon Lex V2 considers intents with the matching context as a trigger as the next intent in a session.</p>"""
    session_attributes: NotRequired["aws_sdk_lex_runtime_v2.types.string_map.StringMap"]
    """<p>Map of key/value pairs representing session-specific context information. It contains application information passed between Amazon Lex V2 and a client application.</p>"""
    originating_request_id: NotRequired[
        "aws_sdk_lex_runtime_v2.types.non_empty_string.NonEmptyString"
    ]
    """<p>A unique identifier for a specific request.</p>"""
    runtime_hints: NotRequired[
        "aws_sdk_lex_runtime_v2.types.runtime_hints.RuntimeHints"
    ]
    """<p>Hints for phrases that a customer is likely to use for a slot. Amazon Lex V2 uses the hints to help determine the correct value of a slot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SessionState) -> dict:
    out: dict = {}
    if "dialog_action" in value:
        import aws_sdk_lex_runtime_v2.types.dialog_action

        out["dialogAction"] = aws_sdk_lex_runtime_v2.types.dialog_action.serialize_json(
            value["dialog_action"]
        )
    if "intent" in value:
        import aws_sdk_lex_runtime_v2.types.intent

        out["intent"] = aws_sdk_lex_runtime_v2.types.intent.serialize_json(
            value["intent"]
        )
    if "active_contexts" in value:
        import aws_sdk_lex_runtime_v2.types.active_contexts_list

        out["activeContexts"] = (
            aws_sdk_lex_runtime_v2.types.active_contexts_list.serialize_json(
                value["active_contexts"]
            )
        )
    if "session_attributes" in value:
        import aws_sdk_lex_runtime_v2.types.string_map

        out["sessionAttributes"] = (
            aws_sdk_lex_runtime_v2.types.string_map.serialize_json(
                value["session_attributes"]
            )
        )
    if "originating_request_id" in value:
        out["originatingRequestId"] = value["originating_request_id"]
    if "runtime_hints" in value:
        import aws_sdk_lex_runtime_v2.types.runtime_hints

        out["runtimeHints"] = aws_sdk_lex_runtime_v2.types.runtime_hints.serialize_json(
            value["runtime_hints"]
        )
    return out


def deserialize_json(data: dict) -> SessionState:
    out: SessionState = {}  # type: ignore[typeddict-item]
    if "dialogAction" in data:
        import aws_sdk_lex_runtime_v2.types.dialog_action

        out["dialog_action"] = (
            aws_sdk_lex_runtime_v2.types.dialog_action.deserialize_json(
                data["dialogAction"]
            )
        )
    if "intent" in data:
        import aws_sdk_lex_runtime_v2.types.intent

        out["intent"] = aws_sdk_lex_runtime_v2.types.intent.deserialize_json(
            data["intent"]
        )
    if "activeContexts" in data:
        import aws_sdk_lex_runtime_v2.types.active_contexts_list

        out["active_contexts"] = (
            aws_sdk_lex_runtime_v2.types.active_contexts_list.deserialize_json(
                data["activeContexts"]
            )
        )
    if "sessionAttributes" in data:
        import aws_sdk_lex_runtime_v2.types.string_map

        out["session_attributes"] = (
            aws_sdk_lex_runtime_v2.types.string_map.deserialize_json(
                data["sessionAttributes"]
            )
        )
    if "originatingRequestId" in data:
        out["originating_request_id"] = data["originatingRequestId"]
    if "runtimeHints" in data:
        import aws_sdk_lex_runtime_v2.types.runtime_hints

        out["runtime_hints"] = (
            aws_sdk_lex_runtime_v2.types.runtime_hints.deserialize_json(
                data["runtimeHints"]
            )
        )
    return out
