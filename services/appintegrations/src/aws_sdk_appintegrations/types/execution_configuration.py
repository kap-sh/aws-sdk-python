"""Generated from Smithy shape ``com.amazonaws.appintegrations#ExecutionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_appintegrations.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appintegrations.types.execution_mode
    import aws_sdk_appintegrations.types.on_demand_configuration
    import aws_sdk_appintegrations.types.schedule_configuration


class ExecutionConfiguration(TypedDict, closed=True):
    execution_mode: "aws_sdk_appintegrations.types.execution_mode.ExecutionMode"
    """<p>The mode for data import/export execution.</p>"""
    on_demand_configuration: NotRequired[
        "aws_sdk_appintegrations.types.on_demand_configuration.OnDemandConfiguration"
    ]
    schedule_configuration: NotRequired[
        "aws_sdk_appintegrations.types.schedule_configuration.ScheduleConfiguration"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: ExecutionConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_appintegrations.types.execution_mode

    out["ExecutionMode"] = aws_sdk_appintegrations.types.execution_mode.serialize_json(
        value["execution_mode"]
    )
    if "on_demand_configuration" in value:
        import aws_sdk_appintegrations.types.on_demand_configuration

        out["OnDemandConfiguration"] = (
            aws_sdk_appintegrations.types.on_demand_configuration.serialize_json(
                value["on_demand_configuration"]
            )
        )
    if "schedule_configuration" in value:
        import aws_sdk_appintegrations.types.schedule_configuration

        out["ScheduleConfiguration"] = (
            aws_sdk_appintegrations.types.schedule_configuration.serialize_json(
                value["schedule_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> ExecutionConfiguration:
    out: ExecutionConfiguration = {}  # type: ignore[typeddict-item]
    if "ExecutionMode" in data:
        import aws_sdk_appintegrations.types.execution_mode

        out["execution_mode"] = (
            aws_sdk_appintegrations.types.execution_mode.deserialize_json(
                data["ExecutionMode"]
            )
        )
    else:
        raise DeserializationError("ExecutionConfiguration.execution_mode required")
    if "OnDemandConfiguration" in data:
        import aws_sdk_appintegrations.types.on_demand_configuration

        out["on_demand_configuration"] = (
            aws_sdk_appintegrations.types.on_demand_configuration.deserialize_json(
                data["OnDemandConfiguration"]
            )
        )
    if "ScheduleConfiguration" in data:
        import aws_sdk_appintegrations.types.schedule_configuration

        out["schedule_configuration"] = (
            aws_sdk_appintegrations.types.schedule_configuration.deserialize_json(
                data["ScheduleConfiguration"]
            )
        )
    return out
