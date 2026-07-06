"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#CreateSystemRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.client_token
    import aws_sdk_resiliencehubv2.types.entity_description
    import aws_sdk_resiliencehubv2.types.entity_name
    import aws_sdk_resiliencehubv2.types.kms_key_id
    import aws_sdk_resiliencehubv2.types.tag_map


class CreateSystemRequest(TypedDict, closed=True):
    name: "aws_sdk_resiliencehubv2.types.entity_name.EntityName"
    description: NotRequired[
        "aws_sdk_resiliencehubv2.types.entity_description.EntityDescription"
    ]
    sharing_enabled: NotRequired["bool"]
    """<p>Indicates whether cross-account sharing is enabled for the system.</p>"""
    kms_key_id: NotRequired["aws_sdk_resiliencehubv2.types.kms_key_id.KmsKeyId"]
    tags: NotRequired["aws_sdk_resiliencehubv2.types.tag_map.TagMap"]
    client_token: NotRequired["aws_sdk_resiliencehubv2.types.client_token.ClientToken"]


# --- restJson1 ser/de ---
def serialize_json(value: CreateSystemRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "sharing_enabled" in value:
        out["sharingEnabled"] = value["sharing_enabled"]
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    if "tags" in value:
        import aws_sdk_resiliencehubv2.types.tag_map

        out["tags"] = aws_sdk_resiliencehubv2.types.tag_map.serialize_json(
            value["tags"]
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateSystemRequest:
    out: CreateSystemRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateSystemRequest.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "sharingEnabled" in data:
        out["sharing_enabled"] = data["sharingEnabled"]
    if "kmsKeyId" in data:
        out["kms_key_id"] = data["kmsKeyId"]
    if "tags" in data:
        import aws_sdk_resiliencehubv2.types.tag_map

        out["tags"] = aws_sdk_resiliencehubv2.types.tag_map.deserialize_json(
            data["tags"]
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
