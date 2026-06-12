"""Generated from Smithy shape ``com.amazonaws.pinpointemail#DeliveryOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint_email.types.pool_name
    import aws_sdk_pinpoint_email.types.tls_policy


class DeliveryOptions(TypedDict):
    tls_policy: NotRequired["aws_sdk_pinpoint_email.types.tls_policy.TlsPolicy"]
    """<p>Specifies whether messages that use the configuration set are required to use Transport Layer Security (TLS). If the value is <code>Require</code>, messages are only delivered if a TLS connection can be established. If the value is <code>Optional</code>, messages can be delivered in plain text if a TLS connection can't be established.</p>"""
    sending_pool_name: NotRequired["aws_sdk_pinpoint_email.types.pool_name.PoolName"]
    """<p>The name of the dedicated IP pool that you want to associate with the configuration set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeliveryOptions) -> dict:
    out: dict = {}
    if "tls_policy" in value:
        import aws_sdk_pinpoint_email.types.tls_policy

        out["TlsPolicy"] = aws_sdk_pinpoint_email.types.tls_policy.serialize_json(
            value["tls_policy"]
        )
    if "sending_pool_name" in value:
        out["SendingPoolName"] = value["sending_pool_name"]
    return out


def deserialize_json(data: dict) -> DeliveryOptions:
    out: DeliveryOptions = {}  # type: ignore[typeddict-item]
    if "TlsPolicy" in data:
        import aws_sdk_pinpoint_email.types.tls_policy

        out["tls_policy"] = aws_sdk_pinpoint_email.types.tls_policy.deserialize_json(
            data["TlsPolicy"]
        )
    if "SendingPoolName" in data:
        out["sending_pool_name"] = data["SendingPoolName"]
    return out
