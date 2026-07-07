"""Generated from Smithy shape ``com.amazonaws.iotevents#DescribeLoggingOptionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_events.types.logging_options


class DescribeLoggingOptionsResponse(TypedDict, closed=True):
    logging_options: NotRequired[
        "aws_sdk_iot_events.types.logging_options.LoggingOptions"
    ]
    """<p>The current settings of the AWS IoT Events logging options.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeLoggingOptionsResponse) -> dict:
    out: dict = {}
    if "logging_options" in value:
        import aws_sdk_iot_events.types.logging_options

        out["loggingOptions"] = aws_sdk_iot_events.types.logging_options.serialize_json(
            value["logging_options"]
        )
    return out


def deserialize_json(data: dict) -> DescribeLoggingOptionsResponse:
    out: DescribeLoggingOptionsResponse = {}  # type: ignore[typeddict-item]
    if "loggingOptions" in data:
        import aws_sdk_iot_events.types.logging_options

        out["logging_options"] = (
            aws_sdk_iot_events.types.logging_options.deserialize_json(
                data["loggingOptions"]
            )
        )
    return out
