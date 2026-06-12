"""Generated from Smithy shape ``com.amazonaws.greengrass#FunctionExecutionConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.function_isolation_mode
    import aws_sdk_greengrass.types.function_run_as_config


class FunctionExecutionConfig(TypedDict):
    isolation_mode: NotRequired[
        "aws_sdk_greengrass.types.function_isolation_mode.FunctionIsolationMode"
    ]
    run_as: NotRequired[
        "aws_sdk_greengrass.types.function_run_as_config.FunctionRunAsConfig"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: FunctionExecutionConfig) -> dict:
    out: dict = {}
    if "isolation_mode" in value:
        import aws_sdk_greengrass.types.function_isolation_mode

        out["IsolationMode"] = (
            aws_sdk_greengrass.types.function_isolation_mode.serialize_json(
                value["isolation_mode"]
            )
        )
    if "run_as" in value:
        import aws_sdk_greengrass.types.function_run_as_config

        out["RunAs"] = aws_sdk_greengrass.types.function_run_as_config.serialize_json(
            value["run_as"]
        )
    return out


def deserialize_json(data: dict) -> FunctionExecutionConfig:
    out: FunctionExecutionConfig = {}  # type: ignore[typeddict-item]
    if "IsolationMode" in data:
        import aws_sdk_greengrass.types.function_isolation_mode

        out["isolation_mode"] = (
            aws_sdk_greengrass.types.function_isolation_mode.deserialize_json(
                data["IsolationMode"]
            )
        )
    if "RunAs" in data:
        import aws_sdk_greengrass.types.function_run_as_config

        out["run_as"] = (
            aws_sdk_greengrass.types.function_run_as_config.deserialize_json(
                data["RunAs"]
            )
        )
    return out
