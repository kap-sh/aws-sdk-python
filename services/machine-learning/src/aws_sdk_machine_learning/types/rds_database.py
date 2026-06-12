"""Generated from Smithy shape ``com.amazonaws.machinelearning#RDSDatabase``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_machine_learning.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_machine_learning.types.rds_database_name
    import aws_sdk_machine_learning.types.rds_instance_identifier


class RDSDatabase(TypedDict):
    instance_identifier: (
        "aws_sdk_machine_learning.types.rds_instance_identifier.RDSInstanceIdentifier"
    )
    """<p>The ID of an RDS DB instance.</p>"""
    database_name: "aws_sdk_machine_learning.types.rds_database_name.RDSDatabaseName"


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RDSDatabase) -> dict:
    out: dict = {}
    out["InstanceIdentifier"] = value["instance_identifier"]
    out["DatabaseName"] = value["database_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RDSDatabase:
    out: RDSDatabase = {}  # type: ignore[typeddict-item]
    if "InstanceIdentifier" in data:
        out["instance_identifier"] = data["InstanceIdentifier"]
    else:
        raise DeserializationError("RDSDatabase.instance_identifier required")
    if "DatabaseName" in data:
        out["database_name"] = data["DatabaseName"]
    else:
        raise DeserializationError("RDSDatabase.database_name required")
    return out
