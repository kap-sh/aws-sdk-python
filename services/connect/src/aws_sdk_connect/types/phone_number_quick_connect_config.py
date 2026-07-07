"""Generated from Smithy shape ``com.amazonaws.connect#PhoneNumberQuickConnectConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.phone_number


class PhoneNumberQuickConnectConfig(TypedDict, closed=True):
    phone_number: "aws_sdk_connect.types.phone_number.PhoneNumber"
    """<p>The phone number in E.164 format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PhoneNumberQuickConnectConfig) -> dict:
    out: dict = {}
    out["PhoneNumber"] = value["phone_number"]
    return out


def deserialize_json(data: dict) -> PhoneNumberQuickConnectConfig:
    out: PhoneNumberQuickConnectConfig = {}  # type: ignore[typeddict-item]
    if "PhoneNumber" in data:
        out["phone_number"] = data["PhoneNumber"]
    else:
        raise DeserializationError(
            "PhoneNumberQuickConnectConfig.phone_number required"
        )
    return out
