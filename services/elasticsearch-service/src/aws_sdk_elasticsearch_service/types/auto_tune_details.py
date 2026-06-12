"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#AutoTuneDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.scheduled_auto_tune_details


class AutoTuneDetails(TypedDict):
    scheduled_auto_tune_details: NotRequired[
        "aws_sdk_elasticsearch_service.types.scheduled_auto_tune_details.ScheduledAutoTuneDetails"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: AutoTuneDetails) -> dict:
    out: dict = {}
    if "scheduled_auto_tune_details" in value:
        import aws_sdk_elasticsearch_service.types.scheduled_auto_tune_details

        out["ScheduledAutoTuneDetails"] = (
            aws_sdk_elasticsearch_service.types.scheduled_auto_tune_details.serialize_json(
                value["scheduled_auto_tune_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> AutoTuneDetails:
    out: AutoTuneDetails = {}  # type: ignore[typeddict-item]
    if "ScheduledAutoTuneDetails" in data:
        import aws_sdk_elasticsearch_service.types.scheduled_auto_tune_details

        out["scheduled_auto_tune_details"] = (
            aws_sdk_elasticsearch_service.types.scheduled_auto_tune_details.deserialize_json(
                data["ScheduledAutoTuneDetails"]
            )
        )
    return out
