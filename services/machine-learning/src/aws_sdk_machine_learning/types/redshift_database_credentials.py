"""Generated from Smithy shape ``com.amazonaws.machinelearning#RedshiftDatabaseCredentials``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_machine_learning.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_machine_learning.types.redshift_database_password
    import aws_sdk_machine_learning.types.redshift_database_username


class RedshiftDatabaseCredentials(TypedDict, closed=True):
    username: "aws_sdk_machine_learning.types.redshift_database_username.RedshiftDatabaseUsername"
    password: "aws_sdk_machine_learning.types.redshift_database_password.RedshiftDatabasePassword"


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RedshiftDatabaseCredentials) -> dict:
    out: dict = {}
    out["Username"] = value["username"]
    out["Password"] = value["password"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RedshiftDatabaseCredentials:
    out: RedshiftDatabaseCredentials = {}  # type: ignore[typeddict-item]
    if "Username" in data:
        out["username"] = data["Username"]
    else:
        raise DeserializationError("RedshiftDatabaseCredentials.username required")
    if "Password" in data:
        out["password"] = data["Password"]
    else:
        raise DeserializationError("RedshiftDatabaseCredentials.password required")
    return out
