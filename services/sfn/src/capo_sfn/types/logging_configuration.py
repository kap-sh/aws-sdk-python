"""Generated from Smithy shape ``com.amazonaws.sfn#LoggingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sfn.types.include_execution_data
    import capo_sfn.types.log_destination_list
    import capo_sfn.types.log_level


class LoggingConfiguration(TypedDict, closed=True):
    level: NotRequired["capo_sfn.types.log_level.LogLevel"]
    """<p>Defines which category of execution history events are logged.</p>"""
    include_execution_data: "capo_sfn.types.include_execution_data.IncludeExecutionData"
    """<p>Determines whether execution data is included in your log. When set to <code>false</code>, data is excluded.</p>"""
    destinations: NotRequired["capo_sfn.types.log_destination_list.LogDestinationList"]
    """<p>An array of objects that describes where your execution history events will be logged. Limited to size 1. Required, if your log level is not set to <code>OFF</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LoggingConfiguration) -> dict:
    out: dict = {}
    if "level" in value:
        import capo_sfn.types.log_level

        out["level"] = capo_sfn.types.log_level.serialize_aws_json_1_0(value["level"])
    out["includeExecutionData"] = value.get("include_execution_data", False)
    if "destinations" in value:
        import capo_sfn.types.log_destination_list

        out["destinations"] = (
            capo_sfn.types.log_destination_list.serialize_aws_json_1_0(
                value["destinations"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> LoggingConfiguration:
    out: LoggingConfiguration = {}  # type: ignore[typeddict-item]
    if "level" in data:
        import capo_sfn.types.log_level

        out["level"] = capo_sfn.types.log_level.deserialize_aws_json_1_0(data["level"])
    if "includeExecutionData" in data:
        out["include_execution_data"] = data["includeExecutionData"]
    else:
        out["include_execution_data"] = False
    if "destinations" in data:
        import capo_sfn.types.log_destination_list

        out["destinations"] = (
            capo_sfn.types.log_destination_list.deserialize_aws_json_1_0(
                data["destinations"]
            )
        )
    return out
