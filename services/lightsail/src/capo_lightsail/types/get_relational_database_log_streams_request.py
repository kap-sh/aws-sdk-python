"""Generated from Smithy shape ``com.amazonaws.lightsail#GetRelationalDatabaseLogStreamsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_lightsail.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lightsail.types.resource_name


class GetRelationalDatabaseLogStreamsRequest(TypedDict, closed=True):
    relational_database_name: "capo_lightsail.types.resource_name.ResourceName"
    """<p>The name of your database for which to get log streams.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetRelationalDatabaseLogStreamsRequest) -> dict:
    out: dict = {}
    out["relationalDatabaseName"] = value["relational_database_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetRelationalDatabaseLogStreamsRequest:
    out: GetRelationalDatabaseLogStreamsRequest = {}  # type: ignore[typeddict-item]
    if "relationalDatabaseName" in data:
        out["relational_database_name"] = data["relationalDatabaseName"]
    else:
        raise DeserializationError(
            "GetRelationalDatabaseLogStreamsRequest.relational_database_name required"
        )
    return out
