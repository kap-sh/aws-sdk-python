"""Generated from Smithy shape ``com.amazonaws.iam#SigningCertificate``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iam._protocol.xml import Element
from aws_sdk_iam.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iam.types.certificate_body_type
    import aws_sdk_iam.types.certificate_id_type
    import aws_sdk_iam.types.date_type
    import aws_sdk_iam.types.status_type
    import aws_sdk_iam.types.user_name_type


class SigningCertificate(TypedDict):
    user_name: "aws_sdk_iam.types.user_name_type.userNameType"
    """<p>The name of the user the signing certificate is associated with.</p>"""
    certificate_id: "aws_sdk_iam.types.certificate_id_type.certificateIdType"
    """<p>The ID for the signing certificate.</p>"""
    certificate_body: "aws_sdk_iam.types.certificate_body_type.certificateBodyType"
    """<p>The contents of the signing certificate.</p>"""
    status: "aws_sdk_iam.types.status_type.statusType"
    """<p>The status of the signing certificate. <code>Active</code> means that the key is valid for API calls, while <code>Inactive</code> means it is not.</p>"""
    upload_date: NotRequired["aws_sdk_iam.types.date_type.dateType"]
    """<p>The date when the signing certificate was uploaded.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: SigningCertificate, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.UserName", str(value["user_name"])))
    pairs.append((f"{prefix}.CertificateId", str(value["certificate_id"])))
    pairs.append((f"{prefix}.CertificateBody", str(value["certificate_body"])))
    import aws_sdk_iam.types.status_type

    aws_sdk_iam.types.status_type.serialize_query(
        value["status"], pairs, f"{prefix}.Status"
    )
    if "upload_date" in value:
        import aws_sdk_iam.types.date_type

        aws_sdk_iam.types.date_type.serialize_query(
            value["upload_date"], pairs, f"{prefix}.UploadDate"
        )


def deserialize_query(el: Element) -> SigningCertificate:
    out: SigningCertificate = {}  # type: ignore[typeddict-item]
    child_user_name = el.find("UserName")
    if child_user_name is not None:
        out["user_name"] = str(child_user_name.text or "")
    else:
        raise DeserializationError("SigningCertificate.user_name required")
    child_certificate_id = el.find("CertificateId")
    if child_certificate_id is not None:
        out["certificate_id"] = str(child_certificate_id.text or "")
    else:
        raise DeserializationError("SigningCertificate.certificate_id required")
    child_certificate_body = el.find("CertificateBody")
    if child_certificate_body is not None:
        out["certificate_body"] = str(child_certificate_body.text or "")
    else:
        raise DeserializationError("SigningCertificate.certificate_body required")
    child_status = el.find("Status")
    if child_status is not None:
        import aws_sdk_iam.types.status_type

        out["status"] = aws_sdk_iam.types.status_type.deserialize_query(child_status)
    else:
        raise DeserializationError("SigningCertificate.status required")
    child_upload_date = el.find("UploadDate")
    if child_upload_date is not None:
        import aws_sdk_iam.types.date_type

        out["upload_date"] = aws_sdk_iam.types.date_type.deserialize_query(
            child_upload_date
        )
    return out
