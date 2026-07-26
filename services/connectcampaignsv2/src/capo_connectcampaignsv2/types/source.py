"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#Source``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_connectcampaignsv2.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.arn
    import capo_connectcampaignsv2.types.event_trigger


class _Source_customerProfilesSegmentArn(TypedDict, closed=True):
    customerProfilesSegmentArn: "capo_connectcampaignsv2.types.arn.Arn"


class _Source_eventTrigger(TypedDict, closed=True):
    eventTrigger: "capo_connectcampaignsv2.types.event_trigger.EventTrigger"


Source: TypeAlias = _Source_customerProfilesSegmentArn | _Source_eventTrigger


# --- restJson1 ser/de ---
def serialize_json(value: Source) -> dict:
    if "customerProfilesSegmentArn" in value:
        return {"customerProfilesSegmentArn": value["customerProfilesSegmentArn"]}
    elif "eventTrigger" in value:
        import capo_connectcampaignsv2.types.event_trigger

        return {
            "eventTrigger": capo_connectcampaignsv2.types.event_trigger.serialize_json(
                value["eventTrigger"]
            )
        }
    else:
        raise SerializationError("Source: no variant present")


def deserialize_json(data: dict) -> Source:
    if "customerProfilesSegmentArn" in data:
        return {"customerProfilesSegmentArn": data["customerProfilesSegmentArn"]}
    elif "eventTrigger" in data:
        import capo_connectcampaignsv2.types.event_trigger

        return {
            "eventTrigger": capo_connectcampaignsv2.types.event_trigger.deserialize_json(
                data["eventTrigger"]
            )
        }
    else:
        raise DeserializationError("Source: no recognized variant key")
