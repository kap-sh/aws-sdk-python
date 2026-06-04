"""Generated from Smithy shape ``com.amazonaws.iam#DeleteServerCertificateRequest``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_iam.errors import DeserializationError
from aws_sdk_iam._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_iam.types.server_certificate_name_type


class DeleteServerCertificateRequest(TypedDict):
    server_certificate_name: (
        "aws_sdk_iam.types.server_certificate_name_type.serverCertificateNameType"
    )
    """<p>The name of the server certificate you want to delete.</p> <p>This parameter allows (through its <a href=\"http://wikipedia.org/wiki/regex\">regex pattern</a>) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteServerCertificateRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append(
        (f"{prefix}.ServerCertificateName", str(value["server_certificate_name"]))
    )


def deserialize_query(el: Element) -> DeleteServerCertificateRequest:
    out: DeleteServerCertificateRequest = {}  # type: ignore[typeddict-item]
    child_server_certificate_name = el.find("ServerCertificateName")
    if child_server_certificate_name is not None:
        out["server_certificate_name"] = str(child_server_certificate_name.text or "")
    else:
        raise DeserializationError(
            "DeleteServerCertificateRequest.server_certificate_name required"
        )
    return out
