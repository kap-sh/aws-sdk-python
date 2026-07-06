"""Generated from Smithy shape ``com.amazonaws.connectcampaigns#DialRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_connectcampaigns.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcampaigns.types.attributes
    import aws_sdk_connectcampaigns.types.client_token
    import aws_sdk_connectcampaigns.types.destination_phone_number
    import aws_sdk_connectcampaigns.types.time_stamp


class DialRequest(TypedDict, closed=True):
    client_token: "aws_sdk_connectcampaigns.types.client_token.ClientToken"
    phone_number: (
        "aws_sdk_connectcampaigns.types.destination_phone_number.DestinationPhoneNumber"
    )
    expiration_time: "aws_sdk_connectcampaigns.types.time_stamp.TimeStamp"
    attributes: "aws_sdk_connectcampaigns.types.attributes.Attributes"


# --- restJson1 ser/de ---
def serialize_json(value: DialRequest) -> dict:
    out: dict = {}
    out["clientToken"] = value["client_token"]
    out["phoneNumber"] = value["phone_number"]
    import aws_sdk_connectcampaigns.types.time_stamp

    out["expirationTime"] = aws_sdk_connectcampaigns.types.time_stamp.serialize_json(
        value["expiration_time"]
    )
    import aws_sdk_connectcampaigns.types.attributes

    out["attributes"] = aws_sdk_connectcampaigns.types.attributes.serialize_json(
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
        import aws_sdk_connectcampaigns.types.time_stamp

        out["expiration_time"] = (
            aws_sdk_connectcampaigns.types.time_stamp.deserialize_json(
                data["expirationTime"]
            )
        )
    else:
        raise DeserializationError("DialRequest.expiration_time required")
    if "attributes" in data:
        import aws_sdk_connectcampaigns.types.attributes

        out["attributes"] = aws_sdk_connectcampaigns.types.attributes.deserialize_json(
            data["attributes"]
        )
    else:
        raise DeserializationError("DialRequest.attributes required")
    return out
