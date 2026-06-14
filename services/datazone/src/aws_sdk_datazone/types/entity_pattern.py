"""Generated from Smithy shape ``com.amazonaws.datazone#EntityPattern``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.filter_clause
    import aws_sdk_datazone.types.graph_entity_type


class EntityPattern(TypedDict):
    entity_type: "aws_sdk_datazone.types.graph_entity_type.GraphEntityType"
    """<p>The type of entity to be matched during the graph query.</p>"""
    identifier: "str"
    """<p>The identifier of the root entity to start traversal from during the graph query.</p>"""
    filters: NotRequired["aws_sdk_datazone.types.filter_clause.FilterClause"]


# --- restJson1 ser/de ---
def serialize_json(value: EntityPattern) -> dict:
    out: dict = {}
    import aws_sdk_datazone.types.graph_entity_type

    out["entityType"] = aws_sdk_datazone.types.graph_entity_type.serialize_json(
        value["entity_type"]
    )
    out["identifier"] = value["identifier"]
    if "filters" in value:
        import aws_sdk_datazone.types.filter_clause

        out["filters"] = aws_sdk_datazone.types.filter_clause.serialize_json(
            value["filters"]
        )
    return out


def deserialize_json(data: dict) -> EntityPattern:
    out: EntityPattern = {}  # type: ignore[typeddict-item]
    if "entityType" in data:
        import aws_sdk_datazone.types.graph_entity_type

        out["entity_type"] = aws_sdk_datazone.types.graph_entity_type.deserialize_json(
            data["entityType"]
        )
    else:
        raise DeserializationError("EntityPattern.entity_type required")
    if "identifier" in data:
        out["identifier"] = data["identifier"]
    else:
        raise DeserializationError("EntityPattern.identifier required")
    if "filters" in data:
        import aws_sdk_datazone.types.filter_clause

        out["filters"] = aws_sdk_datazone.types.filter_clause.deserialize_json(
            data["filters"]
        )
    return out
