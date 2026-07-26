"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#Homogeneous``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migrationhubstrategy.types.homogeneous_target_database_engines


class Homogeneous(TypedDict, closed=True):
    target_database_engine: NotRequired[
        "capo_migrationhubstrategy.types.homogeneous_target_database_engines.HomogeneousTargetDatabaseEngines"
    ]
    """<p> The target database engine for homogeneous database migration preferences. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Homogeneous) -> dict:
    out: dict = {}
    if "target_database_engine" in value:
        import capo_migrationhubstrategy.types.homogeneous_target_database_engines

        out["targetDatabaseEngine"] = (
            capo_migrationhubstrategy.types.homogeneous_target_database_engines.serialize_json(
                value["target_database_engine"]
            )
        )
    return out


def deserialize_json(data: dict) -> Homogeneous:
    out: Homogeneous = {}  # type: ignore[typeddict-item]
    if "targetDatabaseEngine" in data:
        import capo_migrationhubstrategy.types.homogeneous_target_database_engines

        out["target_database_engine"] = (
            capo_migrationhubstrategy.types.homogeneous_target_database_engines.deserialize_json(
                data["targetDatabaseEngine"]
            )
        )
    return out
