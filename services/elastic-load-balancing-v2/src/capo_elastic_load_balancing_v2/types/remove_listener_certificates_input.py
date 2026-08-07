"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#RemoveListenerCertificatesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing_v2.types.certificate_list
    import capo_elastic_load_balancing_v2.types.listener_arn


class RemoveListenerCertificatesInput(TypedDict, closed=True):
    listener_arn: NotRequired[
        "capo_elastic_load_balancing_v2.types.listener_arn.ListenerArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the listener.</p>"""
    certificates: NotRequired[
        "capo_elastic_load_balancing_v2.types.certificate_list.CertificateList"
    ]
    """<p>The certificate to remove. You can specify one certificate per call. Set <code>CertificateArn</code> to the certificate ARN but do not set <code>IsDefault</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: RemoveListenerCertificatesInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "listener_arn" in value:
        pairs.append((f"{key_prefix}ListenerArn", str(value["listener_arn"])))
    if "certificates" in value:
        import capo_elastic_load_balancing_v2.types.certificate_list

        capo_elastic_load_balancing_v2.types.certificate_list.serialize_query(
            value["certificates"], pairs, f"{key_prefix}Certificates"
        )


def deserialize_query(el: Element) -> RemoveListenerCertificatesInput:
    out: RemoveListenerCertificatesInput = {}  # type: ignore[typeddict-item]
    child_listener_arn = el.find("ListenerArn")
    if child_listener_arn is not None:
        out["listener_arn"] = str(child_listener_arn.text or "")
    child_certificates = el.find("Certificates")
    if child_certificates is not None:
        import capo_elastic_load_balancing_v2.types.certificate_list

        out["certificates"] = (
            capo_elastic_load_balancing_v2.types.certificate_list.deserialize_query(
                child_certificates
            )
        )
    return out
