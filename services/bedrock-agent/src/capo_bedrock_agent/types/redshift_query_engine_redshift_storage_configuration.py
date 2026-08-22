"""Generated from Smithy shape ``com.amazonaws.bedrockagent#RedshiftQueryEngineRedshiftStorageConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.redshift_database


class RedshiftQueryEngineRedshiftStorageConfiguration(TypedDict, closed=True):
    database_name: "capo_bedrock_agent.types.redshift_database.RedshiftDatabase"
    """<p>The name of the Amazon Redshift database.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RedshiftQueryEngineRedshiftStorageConfiguration) -> dict:
    out: dict = {}
    out["databaseName"] = value["database_name"]
    return out


def deserialize_json(data: dict) -> RedshiftQueryEngineRedshiftStorageConfiguration:
    out: RedshiftQueryEngineRedshiftStorageConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("databaseName") is not None:
        out["database_name"] = data["databaseName"]
    else:
        raise DeserializationError(
            "RedshiftQueryEngineRedshiftStorageConfiguration.database_name required"
        )
    return out
