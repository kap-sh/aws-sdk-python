"""Generated from Smithy shape ``com.amazonaws.ec2#CertificateAuthenticationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string


class CertificateAuthenticationRequest(TypedDict, closed=True):
    client_root_certificate_chain_arn: NotRequired["capo_ec2.types.string.String"]
    """<p>The ARN of the client certificate. The certificate must be signed by a certificate authority (CA) and it must be provisioned in Certificate Manager (ACM).</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CertificateAuthenticationRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "client_root_certificate_chain_arn" in value:
        pairs.append(
            (
                f"{prefix}.ClientRootCertificateChainArn",
                str(value["client_root_certificate_chain_arn"]),
            )
        )


def deserialize_ec2_query(el: Element) -> CertificateAuthenticationRequest:
    out: CertificateAuthenticationRequest = {}  # type: ignore[typeddict-item]
    child_client_root_certificate_chain_arn = el.find("ClientRootCertificateChainArn")
    if child_client_root_certificate_chain_arn is not None:
        out["client_root_certificate_chain_arn"] = str(
            child_client_root_certificate_chain_arn.text or ""
        )
    return out
