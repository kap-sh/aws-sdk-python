"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#InputSessionStateSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.active_context_list
    import capo_lex_models_v2.types.runtime_hints
    import capo_lex_models_v2.types.string_map


class InputSessionStateSpecification(TypedDict, closed=True):
    session_attributes: NotRequired["capo_lex_models_v2.types.string_map.StringMap"]
    """<p>Session attributes for the session state.</p>"""
    active_contexts: NotRequired[
        "capo_lex_models_v2.types.active_context_list.ActiveContextList"
    ]
    """<p>Active contexts for the session state.</p>"""
    runtime_hints: NotRequired["capo_lex_models_v2.types.runtime_hints.RuntimeHints"]
    """<p>Runtime hints for the session state.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InputSessionStateSpecification) -> dict:
    out: dict = {}
    if "session_attributes" in value:
        import capo_lex_models_v2.types.string_map

        out["sessionAttributes"] = capo_lex_models_v2.types.string_map.serialize_json(
            value["session_attributes"]
        )
    if "active_contexts" in value:
        import capo_lex_models_v2.types.active_context_list

        out["activeContexts"] = (
            capo_lex_models_v2.types.active_context_list.serialize_json(
                value["active_contexts"]
            )
        )
    if "runtime_hints" in value:
        import capo_lex_models_v2.types.runtime_hints

        out["runtimeHints"] = capo_lex_models_v2.types.runtime_hints.serialize_json(
            value["runtime_hints"]
        )
    return out


def deserialize_json(data: dict) -> InputSessionStateSpecification:
    out: InputSessionStateSpecification = {}  # type: ignore[typeddict-item]
    if "sessionAttributes" in data:
        import capo_lex_models_v2.types.string_map

        out["session_attributes"] = (
            capo_lex_models_v2.types.string_map.deserialize_json(
                data["sessionAttributes"]
            )
        )
    if "activeContexts" in data:
        import capo_lex_models_v2.types.active_context_list

        out["active_contexts"] = (
            capo_lex_models_v2.types.active_context_list.deserialize_json(
                data["activeContexts"]
            )
        )
    if "runtimeHints" in data:
        import capo_lex_models_v2.types.runtime_hints

        out["runtime_hints"] = capo_lex_models_v2.types.runtime_hints.deserialize_json(
            data["runtimeHints"]
        )
    return out
