"""Generated from Smithy shape ``com.amazonaws.datazone#RelationPattern``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.relation_direction
    import aws_sdk_datazone.types.relation_type


class RelationPattern(TypedDict):
    relation_type: "aws_sdk_datazone.types.relation_type.RelationType"
    """<p>The type of relation to query.</p>"""
    relation_direction: "aws_sdk_datazone.types.relation_direction.RelationDirection"
    """<p>The direction to query.</p>"""
    max_path_length: NotRequired["int"]
    """<p>The number of hops to query.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RelationPattern) -> dict:
    out: dict = {}
    import aws_sdk_datazone.types.relation_type

    out["relationType"] = aws_sdk_datazone.types.relation_type.serialize_json(
        value["relation_type"]
    )
    import aws_sdk_datazone.types.relation_direction

    out["relationDirection"] = aws_sdk_datazone.types.relation_direction.serialize_json(
        value["relation_direction"]
    )
    if "max_path_length" in value:
        out["maxPathLength"] = value["max_path_length"]
    return out


def deserialize_json(data: dict) -> RelationPattern:
    out: RelationPattern = {}  # type: ignore[typeddict-item]
    if "relationType" in data:
        import aws_sdk_datazone.types.relation_type

        out["relation_type"] = aws_sdk_datazone.types.relation_type.deserialize_json(
            data["relationType"]
        )
    else:
        raise DeserializationError("RelationPattern.relation_type required")
    if "relationDirection" in data:
        import aws_sdk_datazone.types.relation_direction

        out["relation_direction"] = (
            aws_sdk_datazone.types.relation_direction.deserialize_json(
                data["relationDirection"]
            )
        )
    else:
        raise DeserializationError("RelationPattern.relation_direction required")
    if "maxPathLength" in data:
        out["max_path_length"] = data["maxPathLength"]
    return out
