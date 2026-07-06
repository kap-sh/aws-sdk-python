"""Generated from Smithy shape ``com.amazonaws.odb#AutonomousDatabaseConnectionStrings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_odb.types.database_connection_string_map
    import aws_sdk_odb.types.database_connection_string_profile_list


class AutonomousDatabaseConnectionStrings(TypedDict, closed=True):
    all_connection_strings: NotRequired[
        "aws_sdk_odb.types.database_connection_string_map.DatabaseConnectionStringMap"
    ]
    """<p>The list of all connection strings that you can use to connect to the Autonomous Database.</p>"""
    dedicated: NotRequired["str"]
    """<p>The connection string for connecting to the Autonomous Database with a dedicated service.</p>"""
    high: NotRequired["str"]
    """<p>The connection string for the high-priority database service.</p>"""
    medium: NotRequired["str"]
    """<p>The connection string for the medium-priority database service.</p>"""
    low: NotRequired["str"]
    """<p>The connection string for the low-priority database service.</p>"""
    profiles: NotRequired[
        "aws_sdk_odb.types.database_connection_string_profile_list.DatabaseConnectionStringProfileList"
    ]
    """<p>The list of connection string profiles for the Autonomous Database.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AutonomousDatabaseConnectionStrings) -> dict:
    out: dict = {}
    if "all_connection_strings" in value:
        import aws_sdk_odb.types.database_connection_string_map

        out["allConnectionStrings"] = (
            aws_sdk_odb.types.database_connection_string_map.serialize_aws_json_1_0(
                value["all_connection_strings"]
            )
        )
    if "dedicated" in value:
        out["dedicated"] = value["dedicated"]
    if "high" in value:
        out["high"] = value["high"]
    if "medium" in value:
        out["medium"] = value["medium"]
    if "low" in value:
        out["low"] = value["low"]
    if "profiles" in value:
        import aws_sdk_odb.types.database_connection_string_profile_list

        out["profiles"] = (
            aws_sdk_odb.types.database_connection_string_profile_list.serialize_aws_json_1_0(
                value["profiles"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> AutonomousDatabaseConnectionStrings:
    out: AutonomousDatabaseConnectionStrings = {}  # type: ignore[typeddict-item]
    if "allConnectionStrings" in data:
        import aws_sdk_odb.types.database_connection_string_map

        out["all_connection_strings"] = (
            aws_sdk_odb.types.database_connection_string_map.deserialize_aws_json_1_0(
                data["allConnectionStrings"]
            )
        )
    if "dedicated" in data:
        out["dedicated"] = data["dedicated"]
    if "high" in data:
        out["high"] = data["high"]
    if "medium" in data:
        out["medium"] = data["medium"]
    if "low" in data:
        out["low"] = data["low"]
    if "profiles" in data:
        import aws_sdk_odb.types.database_connection_string_profile_list

        out["profiles"] = (
            aws_sdk_odb.types.database_connection_string_profile_list.deserialize_aws_json_1_0(
                data["profiles"]
            )
        )
    return out
