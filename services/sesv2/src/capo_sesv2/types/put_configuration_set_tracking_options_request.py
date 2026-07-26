"""Generated from Smithy shape ``com.amazonaws.sesv2#PutConfigurationSetTrackingOptionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.configuration_set_name
    import capo_sesv2.types.custom_redirect_domain
    import capo_sesv2.types.https_policy


class PutConfigurationSetTrackingOptionsRequest(TypedDict, closed=True):
    configuration_set_name: (
        "capo_sesv2.types.configuration_set_name.ConfigurationSetName"
    )
    """<p>The name of the configuration set.</p>"""
    custom_redirect_domain: NotRequired[
        "capo_sesv2.types.custom_redirect_domain.CustomRedirectDomain"
    ]
    """<p>The domain to use to track open and click events.</p>"""
    https_policy: NotRequired["capo_sesv2.types.https_policy.HttpsPolicy"]


# --- restJson1 ser/de ---
def serialize_json(value: PutConfigurationSetTrackingOptionsRequest) -> dict:
    out: dict = {}
    if "custom_redirect_domain" in value:
        out["CustomRedirectDomain"] = value["custom_redirect_domain"]
    if "https_policy" in value:
        import capo_sesv2.types.https_policy

        out["HttpsPolicy"] = capo_sesv2.types.https_policy.serialize_json(
            value["https_policy"]
        )
    return out


def deserialize_json(data: dict) -> PutConfigurationSetTrackingOptionsRequest:
    out: PutConfigurationSetTrackingOptionsRequest = {}  # type: ignore[typeddict-item]
    if "CustomRedirectDomain" in data:
        out["custom_redirect_domain"] = data["CustomRedirectDomain"]
    if "HttpsPolicy" in data:
        import capo_sesv2.types.https_policy

        out["https_policy"] = capo_sesv2.types.https_policy.deserialize_json(
            data["HttpsPolicy"]
        )
    return out
