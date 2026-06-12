"""Generated from Smithy shape ``com.amazonaws.machinelearning#RedshiftDatabase``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_machine_learning.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_machine_learning.types.redshift_cluster_identifier
    import aws_sdk_machine_learning.types.redshift_database_name


class RedshiftDatabase(TypedDict):
    database_name: (
        "aws_sdk_machine_learning.types.redshift_database_name.RedshiftDatabaseName"
    )
    cluster_identifier: "aws_sdk_machine_learning.types.redshift_cluster_identifier.RedshiftClusterIdentifier"


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RedshiftDatabase) -> dict:
    out: dict = {}
    out["DatabaseName"] = value["database_name"]
    out["ClusterIdentifier"] = value["cluster_identifier"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RedshiftDatabase:
    out: RedshiftDatabase = {}  # type: ignore[typeddict-item]
    if "DatabaseName" in data:
        out["database_name"] = data["DatabaseName"]
    else:
        raise DeserializationError("RedshiftDatabase.database_name required")
    if "ClusterIdentifier" in data:
        out["cluster_identifier"] = data["ClusterIdentifier"]
    else:
        raise DeserializationError("RedshiftDatabase.cluster_identifier required")
    return out
