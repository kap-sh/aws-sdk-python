"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DeleteCertificateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.certificate


class DeleteCertificateResponse(TypedDict, closed=True):
    certificate: NotRequired[
        "capo_database_migration_service.types.certificate.Certificate"
    ]
    """<p>The Secure Sockets Layer (SSL) certificate.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteCertificateResponse) -> dict:
    out: dict = {}
    if "certificate" in value:
        import capo_database_migration_service.types.certificate

        out["Certificate"] = (
            capo_database_migration_service.types.certificate.serialize_aws_json_1_1(
                value["certificate"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteCertificateResponse:
    out: DeleteCertificateResponse = {}  # type: ignore[typeddict-item]
    if "Certificate" in data:
        import capo_database_migration_service.types.certificate

        out["certificate"] = (
            capo_database_migration_service.types.certificate.deserialize_aws_json_1_1(
                data["Certificate"]
            )
        )
    return out
