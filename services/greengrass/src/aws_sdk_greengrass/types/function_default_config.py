"""Generated from Smithy shape ``com.amazonaws.greengrass#FunctionDefaultConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.function_default_execution_config


class FunctionDefaultConfig(TypedDict):
    execution: NotRequired[
        "aws_sdk_greengrass.types.function_default_execution_config.FunctionDefaultExecutionConfig"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: FunctionDefaultConfig) -> dict:
    out: dict = {}
    if "execution" in value:
        import aws_sdk_greengrass.types.function_default_execution_config

        out["Execution"] = (
            aws_sdk_greengrass.types.function_default_execution_config.serialize_json(
                value["execution"]
            )
        )
    return out


def deserialize_json(data: dict) -> FunctionDefaultConfig:
    out: FunctionDefaultConfig = {}  # type: ignore[typeddict-item]
    if "Execution" in data:
        import aws_sdk_greengrass.types.function_default_execution_config

        out["execution"] = (
            aws_sdk_greengrass.types.function_default_execution_config.deserialize_json(
                data["Execution"]
            )
        )
    return out
