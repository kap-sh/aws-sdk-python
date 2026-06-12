"""Generated from Smithy shape ``com.amazonaws.lightsail#RelationalDatabaseBlueprint``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.boolean
    import aws_sdk_lightsail.types.relational_database_engine
    import aws_sdk_lightsail.types.string


class RelationalDatabaseBlueprint(TypedDict):
    blueprint_id: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>The ID for the database blueprint.</p>"""
    engine: NotRequired[
        "aws_sdk_lightsail.types.relational_database_engine.RelationalDatabaseEngine"
    ]
    """<p>The database software of the database blueprint (for example, <code>MySQL</code>).</p>"""
    engine_version: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>The database engine version for the database blueprint (for example, <code>5.7.23</code>).</p>"""
    engine_description: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>The description of the database engine for the database blueprint.</p>"""
    engine_version_description: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>The description of the database engine version for the database blueprint.</p>"""
    is_engine_default: NotRequired["aws_sdk_lightsail.types.boolean.boolean"]
    """<p>A Boolean value indicating whether the engine version is the default for the database blueprint.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RelationalDatabaseBlueprint) -> dict:
    out: dict = {}
    if "blueprint_id" in value:
        out["blueprintId"] = value["blueprint_id"]
    if "engine" in value:
        import aws_sdk_lightsail.types.relational_database_engine

        out["engine"] = (
            aws_sdk_lightsail.types.relational_database_engine.serialize_aws_json_1_1(
                value["engine"]
            )
        )
    if "engine_version" in value:
        out["engineVersion"] = value["engine_version"]
    if "engine_description" in value:
        out["engineDescription"] = value["engine_description"]
    if "engine_version_description" in value:
        out["engineVersionDescription"] = value["engine_version_description"]
    if "is_engine_default" in value:
        out["isEngineDefault"] = value["is_engine_default"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RelationalDatabaseBlueprint:
    out: RelationalDatabaseBlueprint = {}  # type: ignore[typeddict-item]
    if "blueprintId" in data:
        out["blueprint_id"] = data["blueprintId"]
    if "engine" in data:
        import aws_sdk_lightsail.types.relational_database_engine

        out["engine"] = (
            aws_sdk_lightsail.types.relational_database_engine.deserialize_aws_json_1_1(
                data["engine"]
            )
        )
    if "engineVersion" in data:
        out["engine_version"] = data["engineVersion"]
    if "engineDescription" in data:
        out["engine_description"] = data["engineDescription"]
    if "engineVersionDescription" in data:
        out["engine_version_description"] = data["engineVersionDescription"]
    if "isEngineDefault" in data:
        out["is_engine_default"] = data["isEngineDefault"]
    return out
