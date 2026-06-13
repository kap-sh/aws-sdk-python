"""Generated from Smithy shape ``com.amazonaws.securitylake#DataLakeConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_securitylake.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_securitylake.types.data_lake_encryption_configuration
    import aws_sdk_securitylake.types.data_lake_lifecycle_configuration
    import aws_sdk_securitylake.types.data_lake_replication_configuration
    import aws_sdk_securitylake.types.region


class DataLakeConfiguration(TypedDict):
    region: "aws_sdk_securitylake.types.region.Region"
    """<p>The Amazon Web Services Regions where Security Lake is automatically enabled.</p>"""
    encryption_configuration: NotRequired[
        "aws_sdk_securitylake.types.data_lake_encryption_configuration.DataLakeEncryptionConfiguration"
    ]
    """<p>Provides encryption details of Amazon Security Lake object.</p>"""
    lifecycle_configuration: NotRequired[
        "aws_sdk_securitylake.types.data_lake_lifecycle_configuration.DataLakeLifecycleConfiguration"
    ]
    """<p>Provides lifecycle details of Amazon Security Lake object.</p>"""
    replication_configuration: NotRequired[
        "aws_sdk_securitylake.types.data_lake_replication_configuration.DataLakeReplicationConfiguration"
    ]
    """<p>Provides replication details of Amazon Security Lake object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataLakeConfiguration) -> dict:
    out: dict = {}
    out["region"] = value["region"]
    if "encryption_configuration" in value:
        import aws_sdk_securitylake.types.data_lake_encryption_configuration

        out["encryptionConfiguration"] = (
            aws_sdk_securitylake.types.data_lake_encryption_configuration.serialize_json(
                value["encryption_configuration"]
            )
        )
    if "lifecycle_configuration" in value:
        import aws_sdk_securitylake.types.data_lake_lifecycle_configuration

        out["lifecycleConfiguration"] = (
            aws_sdk_securitylake.types.data_lake_lifecycle_configuration.serialize_json(
                value["lifecycle_configuration"]
            )
        )
    if "replication_configuration" in value:
        import aws_sdk_securitylake.types.data_lake_replication_configuration

        out["replicationConfiguration"] = (
            aws_sdk_securitylake.types.data_lake_replication_configuration.serialize_json(
                value["replication_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> DataLakeConfiguration:
    out: DataLakeConfiguration = {}  # type: ignore[typeddict-item]
    if "region" in data:
        out["region"] = data["region"]
    else:
        raise DeserializationError("DataLakeConfiguration.region required")
    if "encryptionConfiguration" in data:
        import aws_sdk_securitylake.types.data_lake_encryption_configuration

        out["encryption_configuration"] = (
            aws_sdk_securitylake.types.data_lake_encryption_configuration.deserialize_json(
                data["encryptionConfiguration"]
            )
        )
    if "lifecycleConfiguration" in data:
        import aws_sdk_securitylake.types.data_lake_lifecycle_configuration

        out["lifecycle_configuration"] = (
            aws_sdk_securitylake.types.data_lake_lifecycle_configuration.deserialize_json(
                data["lifecycleConfiguration"]
            )
        )
    if "replicationConfiguration" in data:
        import aws_sdk_securitylake.types.data_lake_replication_configuration

        out["replication_configuration"] = (
            aws_sdk_securitylake.types.data_lake_replication_configuration.deserialize_json(
                data["replicationConfiguration"]
            )
        )
    return out
