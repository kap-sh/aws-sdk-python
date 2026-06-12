"""Generated from Smithy shape ``com.amazonaws.servicecatalogappregistry#AttributeGroup``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_service_catalog_appregistry.types.attribute_group_arn
    import aws_sdk_service_catalog_appregistry.types.attribute_group_id
    import aws_sdk_service_catalog_appregistry.types.description
    import aws_sdk_service_catalog_appregistry.types.name
    import aws_sdk_service_catalog_appregistry.types.tags
    import aws_sdk_service_catalog_appregistry.types.timestamp


class AttributeGroup(TypedDict):
    id: NotRequired[
        "aws_sdk_service_catalog_appregistry.types.attribute_group_id.AttributeGroupId"
    ]
    """<p>The globally unique attribute group identifier of the attribute group.</p>"""
    arn: NotRequired[
        "aws_sdk_service_catalog_appregistry.types.attribute_group_arn.AttributeGroupArn"
    ]
    """<p>The Amazon resource name (ARN) that specifies the attribute group across services.</p>"""
    name: NotRequired["aws_sdk_service_catalog_appregistry.types.name.Name"]
    """<p>The name of the attribute group.</p>"""
    description: NotRequired[
        "aws_sdk_service_catalog_appregistry.types.description.Description"
    ]
    """<p>The description of the attribute group that the user provides.</p>"""
    creation_time: NotRequired[
        "aws_sdk_service_catalog_appregistry.types.timestamp.Timestamp"
    ]
    """<p>The ISO-8601 formatted timestamp of the moment the attribute group was created.</p>"""
    last_update_time: NotRequired[
        "aws_sdk_service_catalog_appregistry.types.timestamp.Timestamp"
    ]
    """<p>The ISO-8601 formatted timestamp of the moment the attribute group was last updated. This time is the same as the creationTime for a newly created attribute group.</p>"""
    tags: NotRequired["aws_sdk_service_catalog_appregistry.types.tags.Tags"]
    """<p>Key-value pairs you can use to associate with the attribute group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AttributeGroup) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "creation_time" in value:
        import aws_sdk_service_catalog_appregistry.types.timestamp

        out["creationTime"] = (
            aws_sdk_service_catalog_appregistry.types.timestamp.serialize_json(
                value["creation_time"]
            )
        )
    if "last_update_time" in value:
        import aws_sdk_service_catalog_appregistry.types.timestamp

        out["lastUpdateTime"] = (
            aws_sdk_service_catalog_appregistry.types.timestamp.serialize_json(
                value["last_update_time"]
            )
        )
    if "tags" in value:
        import aws_sdk_service_catalog_appregistry.types.tags

        out["tags"] = aws_sdk_service_catalog_appregistry.types.tags.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> AttributeGroup:
    out: AttributeGroup = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "creationTime" in data:
        import aws_sdk_service_catalog_appregistry.types.timestamp

        out["creation_time"] = (
            aws_sdk_service_catalog_appregistry.types.timestamp.deserialize_json(
                data["creationTime"]
            )
        )
    if "lastUpdateTime" in data:
        import aws_sdk_service_catalog_appregistry.types.timestamp

        out["last_update_time"] = (
            aws_sdk_service_catalog_appregistry.types.timestamp.deserialize_json(
                data["lastUpdateTime"]
            )
        )
    if "tags" in data:
        import aws_sdk_service_catalog_appregistry.types.tags

        out["tags"] = aws_sdk_service_catalog_appregistry.types.tags.deserialize_json(
            data["tags"]
        )
    return out
