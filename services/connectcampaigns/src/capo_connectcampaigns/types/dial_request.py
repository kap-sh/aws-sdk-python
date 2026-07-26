"""Generated from Smithy shape ``com.amazonaws.connectcampaigns#DialRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_connectcampaigns.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connectcampaigns.types.attributes
    import capo_connectcampaigns.types.client_token
    import capo_connectcampaigns.types.destination_phone_number
    import capo_connectcampaigns.types.time_stamp


class DialRequest(TypedDict, closed=True):
    client_token: "capo_connectcampaigns.types.client_token.ClientToken"
    phone_number: (
        "capo_connectcampaigns.types.destination_phone_number.DestinationPhoneNumber"
    )
    expiration_time: "capo_connectcampaigns.types.time_stamp.TimeStamp"
    attributes: "capo_connectcampaigns.types.attributes.Attributes"


# --- restJson1 ser/de ---
def serialize_json(value: DialRequest) -> dict:
    out: dict = {}
    out["clientToken"] = value["client_token"]
    out["phoneNumber"] = value["phone_number"]
    import capo_connectcampaigns.types.time_stamp

    out["expirationTime"] = capo_connectcampaigns.types.time_stamp.serialize_json(
        value["expiration_time"]
    )
    import capo_connectcampaigns.types.attributes

    out["attributes"] = capo_connectcampaigns.types.attributes.serialize_json(
        value["attributes"]
    )
    return out


def deserialize_json(data: dict) -> DialRequest:
    out: DialRequest = {}  # type: ignore[typeddict-item]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    else:
        raise DeserializationError("DialRequest.client_token required")
    if "phoneNumber" in data:
        out["phone_number"] = data["phoneNumber"]
    else:
        raise DeserializationError("DialRequest.phone_number required")
    if "expirationTime" in data:
        import capo_connectcampaigns.types.time_stamp

        out["expiration_time"] = (
            capo_connectcampaigns.types.time_stamp.deserialize_json(
                data["expirationTime"]
            )
        )
    else:
        raise DeserializationError("DialRequest.expiration_time required")
    if "attributes" in data:
        import capo_connectcampaigns.types.attributes

        out["attributes"] = capo_connectcampaigns.types.attributes.deserialize_json(
            data["attributes"]
        )
    else:
        raise DeserializationError("DialRequest.attributes required")
    return out
