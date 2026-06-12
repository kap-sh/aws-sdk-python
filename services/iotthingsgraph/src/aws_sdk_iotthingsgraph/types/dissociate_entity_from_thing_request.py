"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#DissociateEntityFromThingRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iotthingsgraph.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotthingsgraph.types.entity_type
    import aws_sdk_iotthingsgraph.types.thing_name


class DissociateEntityFromThingRequest(TypedDict):
    thing_name: "aws_sdk_iotthingsgraph.types.thing_name.ThingName"
    """<p>The name of the thing to disassociate.</p>"""
    entity_type: "aws_sdk_iotthingsgraph.types.entity_type.EntityType"
    """<p>The entity type from which to disassociate the thing.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DissociateEntityFromThingRequest) -> dict:
    out: dict = {}
    out["thingName"] = value["thing_name"]
    import aws_sdk_iotthingsgraph.types.entity_type

    out["entityType"] = aws_sdk_iotthingsgraph.types.entity_type.serialize_aws_json_1_1(
        value["entity_type"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DissociateEntityFromThingRequest:
    out: DissociateEntityFromThingRequest = {}  # type: ignore[typeddict-item]
    if "thingName" in data:
        out["thing_name"] = data["thingName"]
    else:
        raise DeserializationError(
            "DissociateEntityFromThingRequest.thing_name required"
        )
    if "entityType" in data:
        import aws_sdk_iotthingsgraph.types.entity_type

        out["entity_type"] = (
            aws_sdk_iotthingsgraph.types.entity_type.deserialize_aws_json_1_1(
                data["entityType"]
            )
        )
    else:
        raise DeserializationError(
            "DissociateEntityFromThingRequest.entity_type required"
        )
    return out
