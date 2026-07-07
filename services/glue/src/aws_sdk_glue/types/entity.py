"""Generated from Smithy shape ``com.amazonaws.glue#Entity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.category
    import aws_sdk_glue.types.custom_properties
    import aws_sdk_glue.types.entity_description
    import aws_sdk_glue.types.entity_label
    import aws_sdk_glue.types.entity_name
    import aws_sdk_glue.types.is_parent_entity


class Entity(TypedDict, closed=True):
    entity_name: NotRequired["aws_sdk_glue.types.entity_name.EntityName"]
    """<p>The name of the entity.</p>"""
    label: NotRequired["aws_sdk_glue.types.entity_label.EntityLabel"]
    """<p>Label used for the entity.</p>"""
    is_parent_entity: NotRequired["aws_sdk_glue.types.is_parent_entity.IsParentEntity"]
    """<p>A Boolean value which helps to determine whether there are sub objects that can be listed.</p>"""
    description: NotRequired["aws_sdk_glue.types.entity_description.EntityDescription"]
    """<p>A description of the entity.</p>"""
    category: NotRequired["aws_sdk_glue.types.category.Category"]
    """<p>The type of entities that are present in the response. This value depends on the source connection. For example this is <code>SObjects</code> for Salesforce and <code>databases</code> or <code>schemas</code> or <code>tables</code> for sources like Amazon Redshift.</p>"""
    custom_properties: NotRequired[
        "aws_sdk_glue.types.custom_properties.CustomProperties"
    ]
    """<p>An optional map of keys which may be returned for an entity by a connector.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Entity) -> dict:
    out: dict = {}
    if "entity_name" in value:
        out["EntityName"] = value["entity_name"]
    if "label" in value:
        out["Label"] = value["label"]
    if "is_parent_entity" in value:
        out["IsParentEntity"] = value["is_parent_entity"]
    if "description" in value:
        out["Description"] = value["description"]
    if "category" in value:
        out["Category"] = value["category"]
    if "custom_properties" in value:
        import aws_sdk_glue.types.custom_properties

        out["CustomProperties"] = (
            aws_sdk_glue.types.custom_properties.serialize_aws_json_1_1(
                value["custom_properties"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Entity:
    out: Entity = {}  # type: ignore[typeddict-item]
    if "EntityName" in data:
        out["entity_name"] = data["EntityName"]
    if "Label" in data:
        out["label"] = data["Label"]
    if "IsParentEntity" in data:
        out["is_parent_entity"] = data["IsParentEntity"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Category" in data:
        out["category"] = data["Category"]
    if "CustomProperties" in data:
        import aws_sdk_glue.types.custom_properties

        out["custom_properties"] = (
            aws_sdk_glue.types.custom_properties.deserialize_aws_json_1_1(
                data["CustomProperties"]
            )
        )
    return out
