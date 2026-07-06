"""Generated from Smithy shape ``com.amazonaws.amp#ScraperLoggingDestination``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_amp.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_amp.types.cloud_watch_log_destination


class _ScraperLoggingDestination_cloudWatchLogs(TypedDict, closed=True):
    cloudWatchLogs: (
        "aws_sdk_amp.types.cloud_watch_log_destination.CloudWatchLogDestination"
    )


ScraperLoggingDestination: TypeAlias = _ScraperLoggingDestination_cloudWatchLogs


# --- restJson1 ser/de ---
def serialize_json(value: ScraperLoggingDestination) -> dict:
    if "cloudWatchLogs" in value:
        import aws_sdk_amp.types.cloud_watch_log_destination

        return {
            "cloudWatchLogs": aws_sdk_amp.types.cloud_watch_log_destination.serialize_json(
                value["cloudWatchLogs"]
            )
        }
    else:
        raise SerializationError("ScraperLoggingDestination: no variant present")


def deserialize_json(data: dict) -> ScraperLoggingDestination:
    if "cloudWatchLogs" in data:
        import aws_sdk_amp.types.cloud_watch_log_destination

        return {
            "cloudWatchLogs": aws_sdk_amp.types.cloud_watch_log_destination.deserialize_json(
                data["cloudWatchLogs"]
            )
        }
    else:
        raise DeserializationError(
            "ScraperLoggingDestination: no recognized variant key"
        )
