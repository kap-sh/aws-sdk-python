"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DescribeCertificatesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.certificate_list
    import aws_sdk_database_migration_service.types.string


class DescribeCertificatesResponse(TypedDict):
    marker: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p>The pagination token.</p>"""
    certificates: NotRequired[
        "aws_sdk_database_migration_service.types.certificate_list.CertificateList"
    ]
    """<p>The Secure Sockets Layer (SSL) certificates associated with the replication instance.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeCertificatesResponse) -> dict:
    out: dict = {}
    if "marker" in value:
        out["Marker"] = value["marker"]
    if "certificates" in value:
        import aws_sdk_database_migration_service.types.certificate_list

        out["Certificates"] = (
            aws_sdk_database_migration_service.types.certificate_list.serialize_aws_json_1_1(
                value["certificates"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeCertificatesResponse:
    out: DescribeCertificatesResponse = {}  # type: ignore[typeddict-item]
    if "Marker" in data:
        out["marker"] = data["Marker"]
    if "Certificates" in data:
        import aws_sdk_database_migration_service.types.certificate_list

        out["certificates"] = (
            aws_sdk_database_migration_service.types.certificate_list.deserialize_aws_json_1_1(
                data["Certificates"]
            )
        )
    return out
