"""Generated from Smithy shape ``com.amazonaws.lambda#FunctionEventInvokeConfigList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lambda.types.function_event_invoke_config

FunctionEventInvokeConfigList: TypeAlias = list[
    "capo_lambda.types.function_event_invoke_config.FunctionEventInvokeConfig"
]


# --- restJson1 ser/de ---
def serialize_json(value: FunctionEventInvokeConfigList) -> list:
    import capo_lambda.types.function_event_invoke_config

    out: list = []
    for item in value:
        out.append(capo_lambda.types.function_event_invoke_config.serialize_json(item))
    return out


def deserialize_json(data: list) -> FunctionEventInvokeConfigList:
    import capo_lambda.types.function_event_invoke_config

    out: FunctionEventInvokeConfigList = []
    for item in data:
        out.append(
            capo_lambda.types.function_event_invoke_config.deserialize_json(item)
        )
    return out
