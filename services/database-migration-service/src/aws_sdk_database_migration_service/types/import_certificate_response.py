"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#ImportCertificateResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.certificate


class ImportCertificateResponse(TypedDict):
    certificate: NotRequired[
        "aws_sdk_database_migration_service.types.certificate.Certificate"
    ]
    """<p>The certificate to be uploaded.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImportCertificateResponse) -> dict:
    out: dict = {}
    if "certificate" in value:
        import aws_sdk_database_migration_service.types.certificate

        out["Certificate"] = (
            aws_sdk_database_migration_service.types.certificate.serialize_aws_json_1_1(
                value["certificate"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ImportCertificateResponse:
    out: ImportCertificateResponse = {}  # type: ignore[typeddict-item]
    if "Certificate" in data:
        import aws_sdk_database_migration_service.types.certificate

        out["certificate"] = (
            aws_sdk_database_migration_service.types.certificate.deserialize_aws_json_1_1(
                data["Certificate"]
            )
        )
    return out
