"""Generated from Smithy shape ``com.amazonaws.sesv2#PutConfigurationSetDeliveryOptionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.configuration_set_name
    import capo_sesv2.types.max_delivery_seconds
    import capo_sesv2.types.sending_pool_name
    import capo_sesv2.types.tls_policy


class PutConfigurationSetDeliveryOptionsRequest(TypedDict, closed=True):
    configuration_set_name: (
        "capo_sesv2.types.configuration_set_name.ConfigurationSetName"
    )
    """<p>The name of the configuration set to associate with a dedicated IP pool.</p>"""
    tls_policy: NotRequired["capo_sesv2.types.tls_policy.TlsPolicy"]
    """<p>Specifies whether messages that use the configuration set are required to use Transport Layer Security (TLS). If the value is <code>Require</code>, messages are only delivered if a TLS connection can be established. If the value is <code>Optional</code>, messages can be delivered in plain text if a TLS connection can't be established.</p>"""
    sending_pool_name: NotRequired["capo_sesv2.types.sending_pool_name.SendingPoolName"]
    """<p>The name of the dedicated IP pool to associate with the configuration set.</p>"""
    max_delivery_seconds: NotRequired[
        "capo_sesv2.types.max_delivery_seconds.MaxDeliverySeconds"
    ]
    """<p>The maximum amount of time, in seconds, that Amazon SES API v2 will attempt delivery of email. If specified, the value must greater than or equal to 300 seconds (5 minutes) and less than or equal to 50400 seconds (840 minutes). </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutConfigurationSetDeliveryOptionsRequest) -> dict:
    out: dict = {}
    if "tls_policy" in value:
        import capo_sesv2.types.tls_policy

        out["TlsPolicy"] = capo_sesv2.types.tls_policy.serialize_json(
            value["tls_policy"]
        )
    if "sending_pool_name" in value:
        out["SendingPoolName"] = value["sending_pool_name"]
    if "max_delivery_seconds" in value:
        out["MaxDeliverySeconds"] = value["max_delivery_seconds"]
    return out


def deserialize_json(data: dict) -> PutConfigurationSetDeliveryOptionsRequest:
    out: PutConfigurationSetDeliveryOptionsRequest = {}  # type: ignore[typeddict-item]
    if "TlsPolicy" in data:
        import capo_sesv2.types.tls_policy

        out["tls_policy"] = capo_sesv2.types.tls_policy.deserialize_json(
            data["TlsPolicy"]
        )
    if "SendingPoolName" in data:
        out["sending_pool_name"] = data["SendingPoolName"]
    if "MaxDeliverySeconds" in data:
        out["max_delivery_seconds"] = data["MaxDeliverySeconds"]
    return out
