"""Generated from Smithy shape ``com.amazonaws.kendra#EntityConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kendra.types.entity_id
    import aws_sdk_kendra.types.entity_type


class EntityConfiguration(TypedDict):
    entity_id: "aws_sdk_kendra.types.entity_id.EntityId"
    """<p>The identifier of a user or group in your IAM Identity Center identity source. For example, a user ID could be an email.</p>"""
    entity_type: "aws_sdk_kendra.types.entity_type.EntityType"
    """<p>Specifies whether you are configuring a <code>User</code> or a <code>Group</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EntityConfiguration) -> dict:
    out: dict = {}
    out["EntityId"] = value["entity_id"]
    import aws_sdk_kendra.types.entity_type

    out["EntityType"] = aws_sdk_kendra.types.entity_type.serialize_aws_json_1_1(
        value["entity_type"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> EntityConfiguration:
    out: EntityConfiguration = {}  # type: ignore[typeddict-item]
    if "EntityId" in data:
        out["entity_id"] = data["EntityId"]
    else:
        raise DeserializationError("EntityConfiguration.entity_id required")
    if "EntityType" in data:
        import aws_sdk_kendra.types.entity_type

        out["entity_type"] = aws_sdk_kendra.types.entity_type.deserialize_aws_json_1_1(
            data["EntityType"]
        )
    else:
        raise DeserializationError("EntityConfiguration.entity_type required")
    return out
