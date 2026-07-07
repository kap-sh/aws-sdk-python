"""Generated from Smithy shape ``com.amazonaws.ec2#CertificateAuthentication``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class CertificateAuthentication(TypedDict, closed=True):
    client_root_certificate_chain: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ARN of the client certificate. </p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CertificateAuthentication, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "client_root_certificate_chain" in value:
        pairs.append(
            (
                f"{prefix}.ClientRootCertificateChain",
                str(value["client_root_certificate_chain"]),
            )
        )


def deserialize_ec2_query(el: Element) -> CertificateAuthentication:
    out: CertificateAuthentication = {}  # type: ignore[typeddict-item]
    child_client_root_certificate_chain = el.find("ClientRootCertificateChain")
    if child_client_root_certificate_chain is not None:
        out["client_root_certificate_chain"] = str(
            child_client_root_certificate_chain.text or ""
        )
    return out
