"""Generated from Smithy shape ``com.amazonaws.ssmsap#GetDatabaseOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm_sap.types.database
    import aws_sdk_ssm_sap.types.tag_map


class GetDatabaseOutput(TypedDict, closed=True):
    database: NotRequired["aws_sdk_ssm_sap.types.database.Database"]
    """<p>The SAP HANA database of an application registered with AWS Systems Manager for SAP.</p>"""
    tags: NotRequired["aws_sdk_ssm_sap.types.tag_map.TagMap"]
    """<p>The tags of a database.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDatabaseOutput) -> dict:
    out: dict = {}
    if "database" in value:
        import aws_sdk_ssm_sap.types.database

        out["Database"] = aws_sdk_ssm_sap.types.database.serialize_json(
            value["database"]
        )
    if "tags" in value:
        import aws_sdk_ssm_sap.types.tag_map

        out["Tags"] = aws_sdk_ssm_sap.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> GetDatabaseOutput:
    out: GetDatabaseOutput = {}  # type: ignore[typeddict-item]
    if "Database" in data:
        import aws_sdk_ssm_sap.types.database

        out["database"] = aws_sdk_ssm_sap.types.database.deserialize_json(
            data["Database"]
        )
    if "Tags" in data:
        import aws_sdk_ssm_sap.types.tag_map

        out["tags"] = aws_sdk_ssm_sap.types.tag_map.deserialize_json(data["Tags"])
    return out
