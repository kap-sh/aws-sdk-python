"""Generated from Smithy shape ``com.amazonaws.lightsail#GetRelationalDatabaseRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_lightsail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.resource_name


class GetRelationalDatabaseRequest(TypedDict, closed=True):
    relational_database_name: "aws_sdk_lightsail.types.resource_name.ResourceName"
    """<p>The name of the database that you are looking up.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetRelationalDatabaseRequest) -> dict:
    out: dict = {}
    out["relationalDatabaseName"] = value["relational_database_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetRelationalDatabaseRequest:
    out: GetRelationalDatabaseRequest = {}  # type: ignore[typeddict-item]
    if "relationalDatabaseName" in data:
        out["relational_database_name"] = data["relationalDatabaseName"]
    else:
        raise DeserializationError(
            "GetRelationalDatabaseRequest.relational_database_name required"
        )
    return out
