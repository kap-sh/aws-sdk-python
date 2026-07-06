"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#EntityDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iotthingsgraph.types.arn
    import aws_sdk_iotthingsgraph.types.definition_document
    import aws_sdk_iotthingsgraph.types.entity_type
    import aws_sdk_iotthingsgraph.types.timestamp
    import aws_sdk_iotthingsgraph.types.urn


class EntityDescription(TypedDict, closed=True):
    id: NotRequired["aws_sdk_iotthingsgraph.types.urn.Urn"]
    """<p>The entity ID.</p>"""
    arn: NotRequired["aws_sdk_iotthingsgraph.types.arn.Arn"]
    """<p>The entity ARN.</p>"""
    type: NotRequired["aws_sdk_iotthingsgraph.types.entity_type.EntityType"]
    """<p>The entity type.</p>"""
    created_at: NotRequired["aws_sdk_iotthingsgraph.types.timestamp.Timestamp"]
    """<p>The time at which the entity was created.</p>"""
    definition: NotRequired[
        "aws_sdk_iotthingsgraph.types.definition_document.DefinitionDocument"
    ]
    """<p>The definition document of the entity.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EntityDescription) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "type" in value:
        import aws_sdk_iotthingsgraph.types.entity_type

        out["type"] = aws_sdk_iotthingsgraph.types.entity_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "created_at" in value:
        import aws_sdk_iotthingsgraph.types.timestamp

        out["createdAt"] = (
            aws_sdk_iotthingsgraph.types.timestamp.serialize_aws_json_1_1(
                value["created_at"]
            )
        )
    if "definition" in value:
        import aws_sdk_iotthingsgraph.types.definition_document

        out["definition"] = (
            aws_sdk_iotthingsgraph.types.definition_document.serialize_aws_json_1_1(
                value["definition"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EntityDescription:
    out: EntityDescription = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "type" in data:
        import aws_sdk_iotthingsgraph.types.entity_type

        out["type"] = aws_sdk_iotthingsgraph.types.entity_type.deserialize_aws_json_1_1(
            data["type"]
        )
    if "createdAt" in data:
        import aws_sdk_iotthingsgraph.types.timestamp

        out["created_at"] = (
            aws_sdk_iotthingsgraph.types.timestamp.deserialize_aws_json_1_1(
                data["createdAt"]
            )
        )
    if "definition" in data:
        import aws_sdk_iotthingsgraph.types.definition_document

        out["definition"] = (
            aws_sdk_iotthingsgraph.types.definition_document.deserialize_aws_json_1_1(
                data["definition"]
            )
        )
    return out
