"""Generated from Smithy shape ``com.amazonaws.iam#DeleteSigningCertificateRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iam._protocol.xml import Element
from aws_sdk_iam.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iam.types.certificate_id_type
    import aws_sdk_iam.types.existing_user_name_type


class DeleteSigningCertificateRequest(TypedDict):
    user_name: NotRequired[
        "aws_sdk_iam.types.existing_user_name_type.existingUserNameType"
    ]
    """<p>The name of the user the signing certificate belongs to.</p> <p>This parameter allows (through its <a href=\"http://wikipedia.org/wiki/regex\">regex pattern</a>) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-</p>"""
    certificate_id: "aws_sdk_iam.types.certificate_id_type.certificateIdType"
    """<p>The ID of the signing certificate to delete.</p> <p>The format of this parameter, as described by its <a href=\"http://wikipedia.org/wiki/regex\">regex</a> pattern, is a string of characters that can be upper- or lower-cased letters or digits.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteSigningCertificateRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "user_name" in value:
        pairs.append((f"{prefix}.UserName", str(value["user_name"])))
    pairs.append((f"{prefix}.CertificateId", str(value["certificate_id"])))


def deserialize_query(el: Element) -> DeleteSigningCertificateRequest:
    out: DeleteSigningCertificateRequest = {}  # type: ignore[typeddict-item]
    child_user_name = el.find("UserName")
    if child_user_name is not None:
        out["user_name"] = str(child_user_name.text or "")
    child_certificate_id = el.find("CertificateId")
    if child_certificate_id is not None:
        out["certificate_id"] = str(child_certificate_id.text or "")
    else:
        raise DeserializationError(
            "DeleteSigningCertificateRequest.certificate_id required"
        )
    return out
