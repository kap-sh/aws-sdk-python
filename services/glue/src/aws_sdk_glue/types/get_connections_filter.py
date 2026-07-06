"""Generated from Smithy shape ``com.amazonaws.glue#GetConnectionsFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.connection_schema_version
    import aws_sdk_glue.types.connection_type
    import aws_sdk_glue.types.match_criteria


class GetConnectionsFilter(TypedDict, closed=True):
    match_criteria: NotRequired["aws_sdk_glue.types.match_criteria.MatchCriteria"]
    """<p>A criteria string that must match the criteria recorded in the connection definition for that connection definition to be returned.</p>"""
    connection_type: NotRequired["aws_sdk_glue.types.connection_type.ConnectionType"]
    """<p>The type of connections to return. Currently, SFTP is not supported.</p>"""
    connection_schema_version: NotRequired[
        "aws_sdk_glue.types.connection_schema_version.ConnectionSchemaVersion"
    ]
    """<p>Denotes if the connection was created with schema version 1 or 2.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetConnectionsFilter) -> dict:
    out: dict = {}
    if "match_criteria" in value:
        import aws_sdk_glue.types.match_criteria

        out["MatchCriteria"] = aws_sdk_glue.types.match_criteria.serialize_aws_json_1_1(
            value["match_criteria"]
        )
    if "connection_type" in value:
        import aws_sdk_glue.types.connection_type

        out["ConnectionType"] = (
            aws_sdk_glue.types.connection_type.serialize_aws_json_1_1(
                value["connection_type"]
            )
        )
    if "connection_schema_version" in value:
        out["ConnectionSchemaVersion"] = value["connection_schema_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetConnectionsFilter:
    out: GetConnectionsFilter = {}  # type: ignore[typeddict-item]
    if "MatchCriteria" in data:
        import aws_sdk_glue.types.match_criteria

        out["match_criteria"] = (
            aws_sdk_glue.types.match_criteria.deserialize_aws_json_1_1(
                data["MatchCriteria"]
            )
        )
    if "ConnectionType" in data:
        import aws_sdk_glue.types.connection_type

        out["connection_type"] = (
            aws_sdk_glue.types.connection_type.deserialize_aws_json_1_1(
                data["ConnectionType"]
            )
        )
    if "ConnectionSchemaVersion" in data:
        out["connection_schema_version"] = data["ConnectionSchemaVersion"]
    return out
