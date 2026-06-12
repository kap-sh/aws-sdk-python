"""Generated from Smithy shape ``com.amazonaws.sesv2#GetEmailAddressInsightsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_sesv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.email_address


class GetEmailAddressInsightsRequest(TypedDict):
    email_address: "aws_sdk_sesv2.types.email_address.EmailAddress"
    """<p>The email address to analyze for validation insights.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEmailAddressInsightsRequest) -> dict:
    out: dict = {}
    out["EmailAddress"] = value["email_address"]
    return out


def deserialize_json(data: dict) -> GetEmailAddressInsightsRequest:
    out: GetEmailAddressInsightsRequest = {}  # type: ignore[typeddict-item]
    if "EmailAddress" in data:
        out["email_address"] = data["EmailAddress"]
    else:
        raise DeserializationError(
            "GetEmailAddressInsightsRequest.email_address required"
        )
    return out
