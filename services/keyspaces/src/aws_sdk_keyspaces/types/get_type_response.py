"""Generated from Smithy shape ``com.amazonaws.keyspaces#GetTypeResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_keyspaces.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_keyspaces.types.arn
    import aws_sdk_keyspaces.types.depth
    import aws_sdk_keyspaces.types.field_list
    import aws_sdk_keyspaces.types.keyspace_name
    import aws_sdk_keyspaces.types.table_name_list
    import aws_sdk_keyspaces.types.timestamp
    import aws_sdk_keyspaces.types.type_name
    import aws_sdk_keyspaces.types.type_name_list
    import aws_sdk_keyspaces.types.type_status


class GetTypeResponse(TypedDict):
    keyspace_name: "aws_sdk_keyspaces.types.keyspace_name.KeyspaceName"
    """<p> The name of the keyspace that contains this type. </p>"""
    type_name: "aws_sdk_keyspaces.types.type_name.TypeName"
    """<p> The name of the type. </p>"""
    field_definitions: NotRequired["aws_sdk_keyspaces.types.field_list.FieldList"]
    """<p> The names and types that define this type. </p>"""
    last_modified_timestamp: NotRequired["aws_sdk_keyspaces.types.timestamp.Timestamp"]
    """<p> The timestamp that shows when this type was last modified. </p>"""
    status: NotRequired["aws_sdk_keyspaces.types.type_status.TypeStatus"]
    """<p> The status of this type. </p>"""
    direct_referring_tables: NotRequired[
        "aws_sdk_keyspaces.types.table_name_list.TableNameList"
    ]
    """<p> The tables that use this type. </p>"""
    direct_parent_types: NotRequired[
        "aws_sdk_keyspaces.types.type_name_list.TypeNameList"
    ]
    """<p> The types that use this type. </p>"""
    max_nesting_depth: "aws_sdk_keyspaces.types.depth.Depth"
    """<p> The level of nesting implemented for this type. </p>"""
    keyspace_arn: "aws_sdk_keyspaces.types.arn.ARN"
    """<p> The unique identifier of the keyspace that contains this type in the format of an Amazon Resource Name (ARN). </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetTypeResponse) -> dict:
    out: dict = {}
    out["keyspaceName"] = value["keyspace_name"]
    out["typeName"] = value["type_name"]
    if "field_definitions" in value:
        import aws_sdk_keyspaces.types.field_list

        out["fieldDefinitions"] = (
            aws_sdk_keyspaces.types.field_list.serialize_aws_json_1_0(
                value["field_definitions"]
            )
        )
    if "last_modified_timestamp" in value:
        import aws_sdk_keyspaces.types.timestamp

        out["lastModifiedTimestamp"] = (
            aws_sdk_keyspaces.types.timestamp.serialize_aws_json_1_0(
                value["last_modified_timestamp"]
            )
        )
    if "status" in value:
        out["status"] = value["status"]
    if "direct_referring_tables" in value:
        import aws_sdk_keyspaces.types.table_name_list

        out["directReferringTables"] = (
            aws_sdk_keyspaces.types.table_name_list.serialize_aws_json_1_0(
                value["direct_referring_tables"]
            )
        )
    if "direct_parent_types" in value:
        import aws_sdk_keyspaces.types.type_name_list

        out["directParentTypes"] = (
            aws_sdk_keyspaces.types.type_name_list.serialize_aws_json_1_0(
                value["direct_parent_types"]
            )
        )
    out["maxNestingDepth"] = value.get("max_nesting_depth", 0)
    out["keyspaceArn"] = value["keyspace_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetTypeResponse:
    out: GetTypeResponse = {}  # type: ignore[typeddict-item]
    if "keyspaceName" in data:
        out["keyspace_name"] = data["keyspaceName"]
    else:
        raise DeserializationError("GetTypeResponse.keyspace_name required")
    if "typeName" in data:
        out["type_name"] = data["typeName"]
    else:
        raise DeserializationError("GetTypeResponse.type_name required")
    if "fieldDefinitions" in data:
        import aws_sdk_keyspaces.types.field_list

        out["field_definitions"] = (
            aws_sdk_keyspaces.types.field_list.deserialize_aws_json_1_0(
                data["fieldDefinitions"]
            )
        )
    if "lastModifiedTimestamp" in data:
        import aws_sdk_keyspaces.types.timestamp

        out["last_modified_timestamp"] = (
            aws_sdk_keyspaces.types.timestamp.deserialize_aws_json_1_0(
                data["lastModifiedTimestamp"]
            )
        )
    if "status" in data:
        out["status"] = data["status"]
    if "directReferringTables" in data:
        import aws_sdk_keyspaces.types.table_name_list

        out["direct_referring_tables"] = (
            aws_sdk_keyspaces.types.table_name_list.deserialize_aws_json_1_0(
                data["directReferringTables"]
            )
        )
    if "directParentTypes" in data:
        import aws_sdk_keyspaces.types.type_name_list

        out["direct_parent_types"] = (
            aws_sdk_keyspaces.types.type_name_list.deserialize_aws_json_1_0(
                data["directParentTypes"]
            )
        )
    if "maxNestingDepth" in data:
        out["max_nesting_depth"] = data["maxNestingDepth"]
    else:
        out["max_nesting_depth"] = 0
    if "keyspaceArn" in data:
        out["keyspace_arn"] = data["keyspaceArn"]
    else:
        raise DeserializationError("GetTypeResponse.keyspace_arn required")
    return out
