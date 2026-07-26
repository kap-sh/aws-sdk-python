"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#CommunicationLimits``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_connectcampaignsv2.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.communication_limit_list


class _CommunicationLimits_communicationLimitsList(TypedDict, closed=True):
    communicationLimitsList: (
        "capo_connectcampaignsv2.types.communication_limit_list.CommunicationLimitList"
    )


CommunicationLimits: TypeAlias = _CommunicationLimits_communicationLimitsList


# --- restJson1 ser/de ---
def serialize_json(value: CommunicationLimits) -> dict:
    if "communicationLimitsList" in value:
        import capo_connectcampaignsv2.types.communication_limit_list

        return {
            "communicationLimitsList": capo_connectcampaignsv2.types.communication_limit_list.serialize_json(
                value["communicationLimitsList"]
            )
        }
    else:
        raise SerializationError("CommunicationLimits: no variant present")


def deserialize_json(data: dict) -> CommunicationLimits:
    if "communicationLimitsList" in data:
        import capo_connectcampaignsv2.types.communication_limit_list

        return {
            "communicationLimitsList": capo_connectcampaignsv2.types.communication_limit_list.deserialize_json(
                data["communicationLimitsList"]
            )
        }
    else:
        raise DeserializationError("CommunicationLimits: no recognized variant key")
