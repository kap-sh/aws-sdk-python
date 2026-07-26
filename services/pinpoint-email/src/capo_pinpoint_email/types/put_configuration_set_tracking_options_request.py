"""Generated from Smithy shape ``com.amazonaws.pinpointemail#PutConfigurationSetTrackingOptionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_email.types.configuration_set_name
    import capo_pinpoint_email.types.custom_redirect_domain


class PutConfigurationSetTrackingOptionsRequest(TypedDict, closed=True):
    configuration_set_name: (
        "capo_pinpoint_email.types.configuration_set_name.ConfigurationSetName"
    )
    """<p>The name of the configuration set that you want to add a custom tracking domain to.</p>"""
    custom_redirect_domain: NotRequired[
        "capo_pinpoint_email.types.custom_redirect_domain.CustomRedirectDomain"
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
