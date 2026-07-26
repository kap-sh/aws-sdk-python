"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DeleteCertificateMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_database_migration_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_database_migration_service.types.string


class DeleteCertificateMessage(TypedDict, closed=True):
    certificate_arn: "capo_database_migration_service.types.string.String"
    """<p>The Amazon Resource Name (ARN) of the certificate.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteCertificateMessage) -> dict:
    out: dict = {}
    out["CertificateArn"] = value["certificate_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteCertificateMessage:
    out: DeleteCertificateMessage = {}  # type: ignore[typeddict-item]
    if "CertificateArn" in data:
        out["certificate_arn"] = data["CertificateArn"]
    else:
        raise DeserializationError("DeleteCertificateMessage.certificate_arn required")
    return out
