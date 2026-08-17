"""Generated from Smithy shape ``com.amazonaws.lambda#CodeSigningConfigList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lambda.types.code_signing_config

CodeSigningConfigList: TypeAlias = list[
    "capo_lambda.types.code_signing_config.CodeSigningConfig"
]


# --- restJson1 ser/de ---
def serialize_json(value: CodeSigningConfigList) -> list:
    import capo_lambda.types.code_signing_config

    out: list = []
    for item in value:
        out.append(capo_lambda.types.code_signing_config.serialize_json(item))
    return out


def deserialize_json(data: list) -> CodeSigningConfigList:
    import capo_lambda.types.code_signing_config

    out: CodeSigningConfigList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_lambda.types.code_signing_config.deserialize_json(item))
    return out
