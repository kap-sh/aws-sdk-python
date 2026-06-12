"""Generated from Smithy shape ``com.amazonaws.pinpointemail#TrackingOptions``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_pinpoint_email.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pinpoint_email.types.custom_redirect_domain


class TrackingOptions(TypedDict):
    custom_redirect_domain: (
        "aws_sdk_pinpoint_email.types.custom_redirect_domain.CustomRedirectDomain"
    )
    """<p>The domain that you want to use for tracking open and click events.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TrackingOptions) -> dict:
    out: dict = {}
    out["CustomRedirectDomain"] = value["custom_redirect_domain"]
    return out


def deserialize_json(data: dict) -> TrackingOptions:
    out: TrackingOptions = {}  # type: ignore[typeddict-item]
    if "CustomRedirectDomain" in data:
        out["custom_redirect_domain"] = data["CustomRedirectDomain"]
    else:
        raise DeserializationError("TrackingOptions.custom_redirect_domain required")
    return out
