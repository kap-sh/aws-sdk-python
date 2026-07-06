"""Generated from Smithy shape ``com.amazonaws.machinelearning#RDSDatabaseCredentials``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_machine_learning.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_machine_learning.types.rds_database_password
    import aws_sdk_machine_learning.types.rds_database_username


class RDSDatabaseCredentials(TypedDict, closed=True):
    username: "aws_sdk_machine_learning.types.rds_database_username.RDSDatabaseUsername"
    password: "aws_sdk_machine_learning.types.rds_database_password.RDSDatabasePassword"


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RDSDatabaseCredentials) -> dict:
    out: dict = {}
    out["Username"] = value["username"]
    out["Password"] = value["password"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RDSDatabaseCredentials:
    out: RDSDatabaseCredentials = {}  # type: ignore[typeddict-item]
    if "Username" in data:
        out["username"] = data["Username"]
    else:
        raise DeserializationError("RDSDatabaseCredentials.username required")
    if "Password" in data:
        out["password"] = data["Password"]
    else:
        raise DeserializationError("RDSDatabaseCredentials.password required")
    return out
