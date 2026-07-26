"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#CertificateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_database_migration_service.types.certificate

CertificateList: TypeAlias = list[
    "capo_database_migration_service.types.certificate.Certificate"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CertificateList) -> list:
    import capo_database_migration_service.types.certificate

    out: list = []
    for item in value:
        out.append(
            capo_database_migration_service.types.certificate.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> CertificateList:
    import capo_database_migration_service.types.certificate

    out: CertificateList = []
    for item in data:
        out.append(
            capo_database_migration_service.types.certificate.deserialize_aws_json_1_1(
                item
            )
        )
    return out
