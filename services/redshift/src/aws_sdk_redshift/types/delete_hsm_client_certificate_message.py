"""Generated from Smithy shape ``com.amazonaws.redshift#DeleteHsmClientCertificateMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.string


class DeleteHsmClientCertificateMessage(TypedDict):
    hsm_client_certificate_identifier: NotRequired[
        "aws_sdk_redshift.types.string.String"
    ]
    """<p>The identifier of the HSM client certificate to be deleted.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteHsmClientCertificateMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "hsm_client_certificate_identifier" in value:
        pairs.append(
            (
                f"{prefix}.HsmClientCertificateIdentifier",
                str(value["hsm_client_certificate_identifier"]),
            )
        )


def deserialize_query(el: Element) -> DeleteHsmClientCertificateMessage:
    out: DeleteHsmClientCertificateMessage = {}  # type: ignore[typeddict-item]
    child_hsm_client_certificate_identifier = el.find("HsmClientCertificateIdentifier")
    if child_hsm_client_certificate_identifier is not None:
        out["hsm_client_certificate_identifier"] = str(
            child_hsm_client_certificate_identifier.text or ""
        )
    return out
