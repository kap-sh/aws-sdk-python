"""Generated from Smithy shape ``com.amazonaws.connect#EndpointType``."""

from typing import Literal, TypeAlias, cast

EndpointType: TypeAlias = Literal[
    "TELEPHONE_NUMBER",
    "VOIP",
    "CONTACT_FLOW",
    "CONNECT_PHONENUMBER_ARN",
    "EMAIL_ADDRESS",
]


# --- restJson1 ser/de ---
def serialize_json(value: EndpointType) -> str:
    return value


def deserialize_json(data: str) -> EndpointType:
    return cast(EndpointType, data)
