"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DatabaseInstanceSoftwareDetailsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.integer_optional
    import capo_database_migration_service.types.string


class DatabaseInstanceSoftwareDetailsResponse(TypedDict, closed=True):
    engine: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The database engine of a database in a Fleet Advisor collector inventory, for example <code>Microsoft SQL Server</code>.</p>"""
    engine_version: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The database engine version of a database in a Fleet Advisor collector inventory, for example <code>2019</code>.</p>"""
    engine_edition: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The database engine edition of a database in a Fleet Advisor collector inventory, for example <code>Express</code>.</p>"""
    service_pack: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The service pack level of the database.</p>"""
    support_level: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The support level of the database, for example <code>Mainstream support</code>.</p>"""
    os_architecture: NotRequired[
        "capo_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p>The operating system architecture of the database.</p>"""
    tooltip: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>Information about the database engine software, for example <code>Mainstream support ends on November 14th, 2024</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DatabaseInstanceSoftwareDetailsResponse) -> dict:
    out: dict = {}
    if "engine" in value:
        out["Engine"] = value["engine"]
    if "engine_version" in value:
        out["EngineVersion"] = value["engine_version"]
    if "engine_edition" in value:
        out["EngineEdition"] = value["engine_edition"]
    if "service_pack" in value:
        out["ServicePack"] = value["service_pack"]
    if "support_level" in value:
        out["SupportLevel"] = value["support_level"]
    if "os_architecture" in value:
        out["OsArchitecture"] = value["os_architecture"]
    if "tooltip" in value:
        out["Tooltip"] = value["tooltip"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DatabaseInstanceSoftwareDetailsResponse:
    out: DatabaseInstanceSoftwareDetailsResponse = {}  # type: ignore[typeddict-item]
    if "Engine" in data:
        out["engine"] = data["Engine"]
    if "EngineVersion" in data:
        out["engine_version"] = data["EngineVersion"]
    if "EngineEdition" in data:
        out["engine_edition"] = data["EngineEdition"]
    if "ServicePack" in data:
        out["service_pack"] = data["ServicePack"]
    if "SupportLevel" in data:
        out["support_level"] = data["SupportLevel"]
    if "OsArchitecture" in data:
        out["os_architecture"] = data["OsArchitecture"]
    if "Tooltip" in data:
        out["tooltip"] = data["Tooltip"]
    return out
