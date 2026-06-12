"""Generated from Smithy shape ``com.amazonaws.pinpointemail#PutConfigurationSetTrackingOptionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint_email.types.configuration_set_name
    import aws_sdk_pinpoint_email.types.custom_redirect_domain


class PutConfigurationSetTrackingOptionsRequest(TypedDict):
    configuration_set_name: (
        "aws_sdk_pinpoint_email.types.configuration_set_name.ConfigurationSetName"
    )
    """<p>The name of the configuration set that you want to add a custom tracking domain to.</p>"""
    custom_redirect_domain: NotRequired[
        "aws_sdk_pinpoint_email.types.custom_redirect_domain.CustomRedirectDomain"
    ]
    """<p>The domain that you want to use to track open and click events.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutConfigurationSetTrackingOptionsRequest) -> dict:
    out: dict = {}
    if "custom_redirect_domain" in value:
        out["CustomRedirectDomain"] = value["custom_redirect_domain"]
    return out


def deserialize_json(data: dict) -> PutConfigurationSetTrackingOptionsRequest:
    out: PutConfigurationSetTrackingOptionsRequest = {}  # type: ignore[typeddict-item]
    if "CustomRedirectDomain" in data:
        out["custom_redirect_domain"] = data["CustomRedirectDomain"]
    return out
