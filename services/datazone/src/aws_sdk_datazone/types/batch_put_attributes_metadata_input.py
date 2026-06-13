"""Generated from Smithy shape ``com.amazonaws.datazone#BatchPutAttributesMetadataInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.attribute_entity_type
    import aws_sdk_datazone.types.attributes
    import aws_sdk_datazone.types.client_token
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.entity_id


class BatchPutAttributesMetadataInput(TypedDict):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The domain ID where you want to write the attribute metadata.</p>"""
    entity_type: "aws_sdk_datazone.types.attribute_entity_type.AttributeEntityType"
    """<p>The entity type for which you want to write the attribute metadata.</p>"""
    entity_identifier: "aws_sdk_datazone.types.entity_id.EntityId"
    """<p>The entity ID for which you want to write the attribute metadata.</p>"""
    client_token: NotRequired["aws_sdk_datazone.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier to ensure idempotency of the request. This field is automatically populated if not provided.</p>"""
    attributes: "aws_sdk_datazone.types.attributes.Attributes"
    """<p>The attributes of the metadata.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchPutAttributesMetadataInput) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    import aws_sdk_datazone.types.attributes

    out["attributes"] = aws_sdk_datazone.types.attributes.serialize_json(
        value["attributes"]
    )
    return out


def deserialize_json(data: dict) -> BatchPutAttributesMetadataInput:
    out: BatchPutAttributesMetadataInput = {}  # type: ignore[typeddict-item]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "attributes" in data:
        import aws_sdk_datazone.types.attributes

        out["attributes"] = aws_sdk_datazone.types.attributes.deserialize_json(
            data["attributes"]
        )
    else:
        raise DeserializationError(
            "BatchPutAttributesMetadataInput.attributes required"
        )
    return out
