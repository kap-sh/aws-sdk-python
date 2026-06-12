"""Generated from Smithy shape ``com.amazonaws.eventbridge#LogConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_eventbridge.types.include_detail
    import aws_sdk_eventbridge.types.level


class LogConfig(TypedDict):
    include_detail: NotRequired[
        "aws_sdk_eventbridge.types.include_detail.IncludeDetail"
    ]
    """<p>Whether EventBridge include detailed event information in the records it generates. Detailed data can be useful for troubleshooting and debugging. This information includes details of the event itself, as well as target details.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-bus-logs.html#eb-event-logs-data\">Including detail data in event bus logs</a> in the <i>EventBridge User Guide</i>.</p>"""
    level: NotRequired["aws_sdk_eventbridge.types.level.Level"]
    """<p>The level of logging detail to include. This applies to all log destinations for the event bus.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-bus-logs.html#eb-event-bus-logs-level\">Specifying event bus log level</a> in the <i>EventBridge User Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LogConfig) -> dict:
    out: dict = {}
    if "include_detail" in value:
        import aws_sdk_eventbridge.types.include_detail

        out["IncludeDetail"] = (
            aws_sdk_eventbridge.types.include_detail.serialize_aws_json_1_1(
                value["include_detail"]
            )
        )
    if "level" in value:
        import aws_sdk_eventbridge.types.level

        out["Level"] = aws_sdk_eventbridge.types.level.serialize_aws_json_1_1(
            value["level"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> LogConfig:
    out: LogConfig = {}  # type: ignore[typeddict-item]
    if "IncludeDetail" in data:
        import aws_sdk_eventbridge.types.include_detail

        out["include_detail"] = (
            aws_sdk_eventbridge.types.include_detail.deserialize_aws_json_1_1(
                data["IncludeDetail"]
            )
        )
    if "Level" in data:
        import aws_sdk_eventbridge.types.level

        out["level"] = aws_sdk_eventbridge.types.level.deserialize_aws_json_1_1(
            data["Level"]
        )
    return out
