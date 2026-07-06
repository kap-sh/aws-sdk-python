"""Generated from Smithy shape ``com.amazonaws.datazone#RemoveEntityOwnerInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.client_token
    import aws_sdk_datazone.types.data_zone_entity_type
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.owner_properties


class RemoveEntityOwnerInput(TypedDict, closed=True):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the domain where you want to remove an owner from an entity.</p>"""
    entity_type: "aws_sdk_datazone.types.data_zone_entity_type.DataZoneEntityType"
    """<p>The type of the entity from which you want to remove an owner.</p>"""
    entity_identifier: "str"
    """<p>The ID of the entity from which you want to remove an owner.</p>"""
    owner: "aws_sdk_datazone.types.owner_properties.OwnerProperties"
    """<p>The owner that you want to remove from an entity.</p>"""
    client_token: NotRequired["aws_sdk_datazone.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RemoveEntityOwnerInput) -> dict:
    out: dict = {}
    import aws_sdk_datazone.types.owner_properties

    out["owner"] = aws_sdk_datazone.types.owner_properties.serialize_json(
        value["owner"]
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> RemoveEntityOwnerInput:
    out: RemoveEntityOwnerInput = {}  # type: ignore[typeddict-item]
    if "owner" in data:
        import aws_sdk_datazone.types.owner_properties

        out["owner"] = aws_sdk_datazone.types.owner_properties.deserialize_json(
            data["owner"]
        )
    else:
        raise DeserializationError("RemoveEntityOwnerInput.owner required")
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
