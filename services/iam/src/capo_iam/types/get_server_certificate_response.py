"""Generated from Smithy shape ``com.amazonaws.iam#GetServerCertificateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iam._protocol.xml import Element
from capo_iam.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iam.types.server_certificate


class GetServerCertificateResponse(TypedDict, closed=True):
    server_certificate: "capo_iam.types.server_certificate.ServerCertificate"
    """<p>A structure containing details about the server certificate.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetServerCertificateResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    import capo_iam.types.server_certificate

    capo_iam.types.server_certificate.serialize_query(
        value["server_certificate"], pairs, f"{key_prefix}ServerCertificate"
    )


def deserialize_query(el: Element) -> GetServerCertificateResponse:
    out: GetServerCertificateResponse = {}  # type: ignore[typeddict-item]
    child_server_certificate = el.find("ServerCertificate")
    if child_server_certificate is not None:
        import capo_iam.types.server_certificate

        out["server_certificate"] = capo_iam.types.server_certificate.deserialize_query(
            child_server_certificate
        )
    else:
        raise DeserializationError(
            "GetServerCertificateResponse.server_certificate required"
        )
    return out
