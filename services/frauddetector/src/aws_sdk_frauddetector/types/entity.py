"""Generated from Smithy shape ``com.amazonaws.frauddetector#Entity``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_frauddetector.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.entity_restricted_string
    import aws_sdk_frauddetector.types.string


class Entity(TypedDict):
    entity_type: "aws_sdk_frauddetector.types.string.string"
    """<p>The entity type.</p>"""
    entity_id: (
        "aws_sdk_frauddetector.types.entity_restricted_string.entityRestrictedString"
    )
    """<p>The entity ID. If you do not know the <code>entityId</code>, you can pass <code>unknown</code>, which is areserved string literal.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Entity) -> dict:
    out: dict = {}
    out["entityType"] = value["entity_type"]
    out["entityId"] = value["entity_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Entity:
    out: Entity = {}  # type: ignore[typeddict-item]
    if "entityType" in data:
        out["entity_type"] = data["entityType"]
    else:
        raise DeserializationError("Entity.entity_type required")
    if "entityId" in data:
        out["entity_id"] = data["entityId"]
    else:
        raise DeserializationError("Entity.entity_id required")
    return out
