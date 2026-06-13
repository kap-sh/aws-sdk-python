"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#DashAvailabilityStartTimeConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_mediapackagev2.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import datetime


class _DashAvailabilityStartTimeConfiguration_FixedAvailabilityStartTime(TypedDict):
    FixedAvailabilityStartTime: "datetime.datetime"


DashAvailabilityStartTimeConfiguration: TypeAlias = (
    _DashAvailabilityStartTimeConfiguration_FixedAvailabilityStartTime
)


# --- restJson1 ser/de ---
def serialize_json(value: DashAvailabilityStartTimeConfiguration) -> dict:
    if "FixedAvailabilityStartTime" in value:
        import aws_sdk_mediapackagev2.types._prelude.timestamp

        return {
            "FixedAvailabilityStartTime": aws_sdk_mediapackagev2.types._prelude.timestamp.serialize_json(
                value["FixedAvailabilityStartTime"]
            )
        }
    else:
        raise SerializationError(
            "DashAvailabilityStartTimeConfiguration: no variant present"
        )


def deserialize_json(data: dict) -> DashAvailabilityStartTimeConfiguration:
    if "FixedAvailabilityStartTime" in data:
        import aws_sdk_mediapackagev2.types._prelude.timestamp

        return {
            "FixedAvailabilityStartTime": aws_sdk_mediapackagev2.types._prelude.timestamp.deserialize_json(
                data["FixedAvailabilityStartTime"]
            )
        }
    else:
        raise DeserializationError(
            "DashAvailabilityStartTimeConfiguration: no recognized variant key"
        )
