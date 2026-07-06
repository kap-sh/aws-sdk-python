"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#Heterogeneous``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_migrationhubstrategy.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_migrationhubstrategy.types.heterogeneous_target_database_engines


class Heterogeneous(TypedDict, closed=True):
    target_database_engine: "aws_sdk_migrationhubstrategy.types.heterogeneous_target_database_engines.HeterogeneousTargetDatabaseEngines"
    """<p> The target database engine for heterogeneous database migration preference. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Heterogeneous) -> dict:
    out: dict = {}
    import aws_sdk_migrationhubstrategy.types.heterogeneous_target_database_engines

    out["targetDatabaseEngine"] = (
        aws_sdk_migrationhubstrategy.types.heterogeneous_target_database_engines.serialize_json(
            value["target_database_engine"]
        )
    )
    return out


def deserialize_json(data: dict) -> Heterogeneous:
    out: Heterogeneous = {}  # type: ignore[typeddict-item]
    if "targetDatabaseEngine" in data:
        import aws_sdk_migrationhubstrategy.types.heterogeneous_target_database_engines

        out["target_database_engine"] = (
            aws_sdk_migrationhubstrategy.types.heterogeneous_target_database_engines.deserialize_json(
                data["targetDatabaseEngine"]
            )
        )
    else:
        raise DeserializationError("Heterogeneous.target_database_engine required")
    return out
