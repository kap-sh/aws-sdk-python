"""Generated from Smithy shape ``com.amazonaws.entityresolution#ListSchemaMappingsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_entityresolution.types.next_token
    import aws_sdk_entityresolution.types.schema_mapping_list


class ListSchemaMappingsOutput(TypedDict):
    schema_list: NotRequired[
        "aws_sdk_entityresolution.types.schema_mapping_list.SchemaMappingList"
    ]
    """<p>A list of <code>SchemaMappingSummary</code> objects, each of which contain the fields <code>SchemaName</code>, <code>SchemaArn</code>, <code>CreatedAt</code>, <code>UpdatedAt</code>.</p>"""
    next_token: NotRequired["aws_sdk_entityresolution.types.next_token.NextToken"]
    """<p>The pagination token from the previous API call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSchemaMappingsOutput) -> dict:
    out: dict = {}
    if "schema_list" in value:
        import aws_sdk_entityresolution.types.schema_mapping_list

        out["schemaList"] = (
            aws_sdk_entityresolution.types.schema_mapping_list.serialize_json(
                value["schema_list"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSchemaMappingsOutput:
    out: ListSchemaMappingsOutput = {}  # type: ignore[typeddict-item]
    if "schemaList" in data:
        import aws_sdk_entityresolution.types.schema_mapping_list

        out["schema_list"] = (
            aws_sdk_entityresolution.types.schema_mapping_list.deserialize_json(
                data["schemaList"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
