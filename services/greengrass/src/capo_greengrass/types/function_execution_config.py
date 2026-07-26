"""Generated from Smithy shape ``com.amazonaws.greengrass#FunctionExecutionConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_greengrass.types.function_isolation_mode
    import capo_greengrass.types.function_run_as_config


class FunctionExecutionConfig(TypedDict, closed=True):
    isolation_mode: NotRequired[
        "capo_greengrass.types.function_isolation_mode.FunctionIsolationMode"
    ]
    run_as: NotRequired[
        "capo_greengrass.types.function_run_as_config.FunctionRunAsConfig"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: FunctionExecutionConfig) -> dict:
    out: dict = {}
    if "isolation_mode" in value:
        import capo_greengrass.types.function_isolation_mode

        out["IsolationMode"] = (
            capo_greengrass.types.function_isolation_mode.serialize_json(
                value["isolation_mode"]
            )
        )
    if "run_as" in value:
        import capo_greengrass.types.function_run_as_config

        out["RunAs"] = capo_greengrass.types.function_run_as_config.serialize_json(
            value["run_as"]
        )
    return out


def deserialize_json(data: dict) -> FunctionExecutionConfig:
    out: FunctionExecutionConfig = {}  # type: ignore[typeddict-item]
    if "IsolationMode" in data:
        import capo_greengrass.types.function_isolation_mode

        out["isolation_mode"] = (
            capo_greengrass.types.function_isolation_mode.deserialize_json(
                data["IsolationMode"]
            )
        )
    if "RunAs" in data:
        import capo_greengrass.types.function_run_as_config

        out["run_as"] = capo_greengrass.types.function_run_as_config.deserialize_json(
            data["RunAs"]
        )
    return out
