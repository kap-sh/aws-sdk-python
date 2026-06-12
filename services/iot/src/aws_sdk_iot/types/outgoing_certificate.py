"""Generated from Smithy shape ``com.amazonaws.iot#OutgoingCertificate``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.aws_account_id
    import aws_sdk_iot.types.certificate_arn
    import aws_sdk_iot.types.certificate_id
    import aws_sdk_iot.types.date_type
    import aws_sdk_iot.types.message


class OutgoingCertificate(TypedDict):
    certificate_arn: NotRequired["aws_sdk_iot.types.certificate_arn.CertificateArn"]
    """<p>The certificate ARN.</p>"""
    certificate_id: NotRequired["aws_sdk_iot.types.certificate_id.CertificateId"]
    """<p>The certificate ID.</p>"""
    transferred_to: NotRequired["aws_sdk_iot.types.aws_account_id.AwsAccountId"]
    """<p>The Amazon Web Services account to which the transfer was made.</p>"""
    transfer_date: NotRequired["aws_sdk_iot.types.date_type.DateType"]
    """<p>The date the transfer was initiated.</p>"""
    transfer_message: NotRequired["aws_sdk_iot.types.message.Message"]
    """<p>The transfer message.</p>"""
    creation_date: NotRequired["aws_sdk_iot.types.date_type.DateType"]
    """<p>The certificate creation date.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OutgoingCertificate) -> dict:
    out: dict = {}
    if "certificate_arn" in value:
        out["certificateArn"] = value["certificate_arn"]
    if "certificate_id" in value:
        out["certificateId"] = value["certificate_id"]
    if "transferred_to" in value:
        out["transferredTo"] = value["transferred_to"]
    if "transfer_date" in value:
        import aws_sdk_iot.types.date_type

        out["transferDate"] = aws_sdk_iot.types.date_type.serialize_json(
            value["transfer_date"]
        )
    if "transfer_message" in value:
        out["transferMessage"] = value["transfer_message"]
    if "creation_date" in value:
        import aws_sdk_iot.types.date_type

        out["creationDate"] = aws_sdk_iot.types.date_type.serialize_json(
            value["creation_date"]
        )
    return out


def deserialize_json(data: dict) -> OutgoingCertificate:
    out: OutgoingCertificate = {}  # type: ignore[typeddict-item]
    if "certificateArn" in data:
        out["certificate_arn"] = data["certificateArn"]
    if "certificateId" in data:
        out["certificate_id"] = data["certificateId"]
    if "transferredTo" in data:
        out["transferred_to"] = data["transferredTo"]
    if "transferDate" in data:
        import aws_sdk_iot.types.date_type

        out["transfer_date"] = aws_sdk_iot.types.date_type.deserialize_json(
            data["transferDate"]
        )
    if "transferMessage" in data:
        out["transfer_message"] = data["transferMessage"]
    if "creationDate" in data:
        import aws_sdk_iot.types.date_type

        out["creation_date"] = aws_sdk_iot.types.date_type.deserialize_json(
            data["creationDate"]
        )
    return out
