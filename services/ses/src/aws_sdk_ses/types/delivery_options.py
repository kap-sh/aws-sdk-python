"""Generated from Smithy shape ``com.amazonaws.ses#DeliveryOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ses._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ses.types.tls_policy


class DeliveryOptions(TypedDict):
    tls_policy: NotRequired["aws_sdk_ses.types.tls_policy.TlsPolicy"]
    """<p>Specifies whether messages that use the configuration set are required to use Transport Layer Security (TLS). If the value is <code>Require</code>, messages are only delivered if a TLS connection can be established. If the value is <code>Optional</code>, messages can be delivered in plain text if a TLS connection can't be established.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeliveryOptions, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "tls_policy" in value:
        import aws_sdk_ses.types.tls_policy

        aws_sdk_ses.types.tls_policy.serialize_query(
            value["tls_policy"], pairs, f"{prefix}.TlsPolicy"
        )


def deserialize_query(el: Element) -> DeliveryOptions:
    out: DeliveryOptions = {}  # type: ignore[typeddict-item]
    child_tls_policy = el.find("TlsPolicy")
    if child_tls_policy is not None:
        import aws_sdk_ses.types.tls_policy

        out["tls_policy"] = aws_sdk_ses.types.tls_policy.deserialize_query(
            child_tls_policy
        )
    return out
