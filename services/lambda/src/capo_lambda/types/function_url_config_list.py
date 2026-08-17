"""Generated from Smithy shape ``com.amazonaws.lambda#FunctionUrlConfigList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lambda.types.function_url_config

FunctionUrlConfigList: TypeAlias = list[
    "capo_lambda.types.function_url_config.FunctionUrlConfig"
]


# --- restJson1 ser/de ---
def serialize_json(value: FunctionUrlConfigList) -> list:
    import capo_lambda.types.function_url_config

    out: list = []
    for item in value:
        out.append(capo_lambda.types.function_url_config.serialize_json(item))
    return out


def deserialize_json(data: list) -> FunctionUrlConfigList:
    import capo_lambda.types.function_url_config

    out: FunctionUrlConfigList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_lambda.types.function_url_config.deserialize_json(item))
    return out
