"""Generated from Smithy shape ``com.amazonaws.greengrass#FunctionDefaultConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_greengrass.types.function_default_execution_config


class FunctionDefaultConfig(TypedDict, closed=True):
    execution: NotRequired[
        "capo_greengrass.types.function_default_execution_config.FunctionDefaultExecutionConfig"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: FunctionDefaultConfig) -> dict:
    out: dict = {}
    if "execution" in value:
        import capo_greengrass.types.function_default_execution_config

        out["Execution"] = (
            capo_greengrass.types.function_default_execution_config.serialize_json(
                value["execution"]
            )
        )
    return out


def deserialize_json(data: dict) -> FunctionDefaultConfig:
    out: FunctionDefaultConfig = {}  # type: ignore[typeddict-item]
    if "Execution" in data:
        import capo_greengrass.types.function_default_execution_config

        out["execution"] = (
            capo_greengrass.types.function_default_execution_config.deserialize_json(
                data["Execution"]
            )
        )
    return out
