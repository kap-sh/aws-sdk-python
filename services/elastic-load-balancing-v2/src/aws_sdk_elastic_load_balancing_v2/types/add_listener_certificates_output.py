"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#AddListenerCertificatesOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing_v2.types.certificate_list


class AddListenerCertificatesOutput(TypedDict):
    certificates: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.certificate_list.CertificateList"
    ]
    """<p>Information about the certificates in the certificate list.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: AddListenerCertificatesOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "certificates" in value:
        import aws_sdk_elastic_load_balancing_v2.types.certificate_list

        aws_sdk_elastic_load_balancing_v2.types.certificate_list.serialize_query(
            value["certificates"], pairs, f"{prefix}.Certificates"
        )


def deserialize_query(el: Element) -> AddListenerCertificatesOutput:
    out: AddListenerCertificatesOutput = {}  # type: ignore[typeddict-item]
    child_certificates = el.find("Certificates")
    if child_certificates is not None:
        import aws_sdk_elastic_load_balancing_v2.types.certificate_list

        out["certificates"] = (
            aws_sdk_elastic_load_balancing_v2.types.certificate_list.deserialize_query(
                child_certificates
            )
        )
    return out
