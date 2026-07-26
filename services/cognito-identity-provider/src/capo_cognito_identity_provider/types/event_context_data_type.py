"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#EventContextDataType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.string_type


class EventContextDataType(TypedDict, closed=True):
    ip_address: NotRequired[
        "capo_cognito_identity_provider.types.string_type.StringType"
    ]
    """<p>The source IP address of your user's device.</p>"""
    device_name: NotRequired[
        "capo_cognito_identity_provider.types.string_type.StringType"
    ]
    """<p>The user's device name.</p>"""
    timezone: NotRequired["capo_cognito_identity_provider.types.string_type.StringType"]
    """<p>The user's time zone.</p>"""
    city: NotRequired["capo_cognito_identity_provider.types.string_type.StringType"]
    """<p>The user's city.</p>"""
    country: NotRequired["capo_cognito_identity_provider.types.string_type.StringType"]
    """<p>The user's country.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventContextDataType) -> dict:
    out: dict = {}
    if "ip_address" in value:
        out["IpAddress"] = value["ip_address"]
    if "device_name" in value:
        out["DeviceName"] = value["device_name"]
    if "timezone" in value:
        out["Timezone"] = value["timezone"]
    if "city" in value:
        out["City"] = value["city"]
    if "country" in value:
        out["Country"] = value["country"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EventContextDataType:
    out: EventContextDataType = {}  # type: ignore[typeddict-item]
    if "IpAddress" in data:
        out["ip_address"] = data["IpAddress"]
    if "DeviceName" in data:
        out["device_name"] = data["DeviceName"]
    if "Timezone" in data:
        out["timezone"] = data["Timezone"]
    if "City" in data:
        out["city"] = data["City"]
    if "Country" in data:
        out["country"] = data["Country"]
    return out
