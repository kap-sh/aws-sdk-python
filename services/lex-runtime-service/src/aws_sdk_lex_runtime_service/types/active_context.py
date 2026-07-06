"""Generated from Smithy shape ``com.amazonaws.lexruntimeservice#ActiveContext``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_lex_runtime_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_runtime_service.types.active_context_name
    import aws_sdk_lex_runtime_service.types.active_context_parameters_map
    import aws_sdk_lex_runtime_service.types.active_context_time_to_live


class ActiveContext(TypedDict, closed=True):
    name: "aws_sdk_lex_runtime_service.types.active_context_name.ActiveContextName"
    """<p>The name of the context.</p>"""
    time_to_live: "aws_sdk_lex_runtime_service.types.active_context_time_to_live.ActiveContextTimeToLive"
    """<p>The length of time or number of turns that a context remains active.</p>"""
    parameters: "aws_sdk_lex_runtime_service.types.active_context_parameters_map.ActiveContextParametersMap"
    """<p>State variables for the current context. You can use these values as default values for slots in subsequent events.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ActiveContext) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import aws_sdk_lex_runtime_service.types.active_context_time_to_live

    out["timeToLive"] = (
        aws_sdk_lex_runtime_service.types.active_context_time_to_live.serialize_json(
            value["time_to_live"]
        )
    )
    import aws_sdk_lex_runtime_service.types.active_context_parameters_map

    out["parameters"] = (
        aws_sdk_lex_runtime_service.types.active_context_parameters_map.serialize_json(
            value["parameters"]
        )
    )
    return out


def deserialize_json(data: dict) -> ActiveContext:
    out: ActiveContext = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("ActiveContext.name required")
    if "timeToLive" in data:
        import aws_sdk_lex_runtime_service.types.active_context_time_to_live

        out["time_to_live"] = (
            aws_sdk_lex_runtime_service.types.active_context_time_to_live.deserialize_json(
                data["timeToLive"]
            )
        )
    else:
        raise DeserializationError("ActiveContext.time_to_live required")
    if "parameters" in data:
        import aws_sdk_lex_runtime_service.types.active_context_parameters_map

        out["parameters"] = (
            aws_sdk_lex_runtime_service.types.active_context_parameters_map.deserialize_json(
                data["parameters"]
            )
        )
    else:
        raise DeserializationError("ActiveContext.parameters required")
    return out
