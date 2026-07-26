"""Generated from Smithy shape ``com.amazonaws.entityresolution#ListSchemaMappingsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_entityresolution.types.next_token
    import capo_entityresolution.types.schema_mapping_list


class ListSchemaMappingsOutput(TypedDict, closed=True):
    schema_list: NotRequired[
        "capo_entityresolution.types.schema_mapping_list.SchemaMappingList"
    ]
    """<p>A list of <code>SchemaMappingSummary</code> objects, each of which contain the fields <code>SchemaName</code>, <code>SchemaArn</code>, <code>CreatedAt</code>, <code>UpdatedAt</code>.</p>"""
    next_token: NotRequired["capo_entityresolution.types.next_token.NextToken"]
    """<p>The pagination token from the previous API call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSchemaMappingsOutput) -> dict:
    out: dict = {}
    if "schema_list" in value:
        import capo_entityresolution.types.schema_mapping_list

        out["schemaList"] = (
            capo_entityresolution.types.schema_mapping_list.serialize_json(
                value["schema_list"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSchemaMappingsOutput:
    out: ListSchemaMappingsOutput = {}  # type: ignore[typeddict-item]
    if "schemaList" in data:
        import capo_entityresolution.types.schema_mapping_list

        out["schema_list"] = (
            capo_entityresolution.types.schema_mapping_list.deserialize_json(
                data["schemaList"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
