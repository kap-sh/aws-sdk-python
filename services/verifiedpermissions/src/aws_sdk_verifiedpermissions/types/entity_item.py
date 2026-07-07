"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#EntityItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_verifiedpermissions.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_verifiedpermissions.types.entity_attributes
    import aws_sdk_verifiedpermissions.types.entity_cedar_tags
    import aws_sdk_verifiedpermissions.types.entity_identifier
    import aws_sdk_verifiedpermissions.types.parent_list


class EntityItem(TypedDict, closed=True):
    identifier: "aws_sdk_verifiedpermissions.types.entity_identifier.EntityIdentifier"
    """<p>The identifier of the entity.</p>"""
    attributes: NotRequired[
        "aws_sdk_verifiedpermissions.types.entity_attributes.EntityAttributes"
    ]
    """<p>A list of attributes for the entity.</p>"""
    parents: NotRequired["aws_sdk_verifiedpermissions.types.parent_list.ParentList"]
    """<p>The parent entities in the hierarchy that contains the entity. A principal or resource entity can be defined with at most 99 <i>transitive parents</i> per authorization request. </p> <p>A transitive parent is an entity in the hierarchy of entities including all direct parents, and parents of parents. For example, a user can be a member of 91 groups if one of those groups is a member of eight groups, for a total of 100: one entity, 91 entity parents, and eight parents of parents. </p>"""
    tags: NotRequired[
        "aws_sdk_verifiedpermissions.types.entity_cedar_tags.EntityCedarTags"
    ]
    """<p>A list of cedar tags for the entity.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EntityItem) -> dict:
    out: dict = {}
    import aws_sdk_verifiedpermissions.types.entity_identifier

    out["identifier"] = (
        aws_sdk_verifiedpermissions.types.entity_identifier.serialize_aws_json_1_0(
            value["identifier"]
        )
    )
    if "attributes" in value:
        import aws_sdk_verifiedpermissions.types.entity_attributes

        out["attributes"] = (
            aws_sdk_verifiedpermissions.types.entity_attributes.serialize_aws_json_1_0(
                value["attributes"]
            )
        )
    if "parents" in value:
        import aws_sdk_verifiedpermissions.types.parent_list

        out["parents"] = (
            aws_sdk_verifiedpermissions.types.parent_list.serialize_aws_json_1_0(
                value["parents"]
            )
        )
    if "tags" in value:
        import aws_sdk_verifiedpermissions.types.entity_cedar_tags

        out["tags"] = (
            aws_sdk_verifiedpermissions.types.entity_cedar_tags.serialize_aws_json_1_0(
                value["tags"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> EntityItem:
    out: EntityItem = {}  # type: ignore[typeddict-item]
    if "identifier" in data:
        import aws_sdk_verifiedpermissions.types.entity_identifier

        out["identifier"] = (
            aws_sdk_verifiedpermissions.types.entity_identifier.deserialize_aws_json_1_0(
                data["identifier"]
            )
        )
    else:
        raise DeserializationError("EntityItem.identifier required")
    if "attributes" in data:
        import aws_sdk_verifiedpermissions.types.entity_attributes

        out["attributes"] = (
            aws_sdk_verifiedpermissions.types.entity_attributes.deserialize_aws_json_1_0(
                data["attributes"]
            )
        )
    if "parents" in data:
        import aws_sdk_verifiedpermissions.types.parent_list

        out["parents"] = (
            aws_sdk_verifiedpermissions.types.parent_list.deserialize_aws_json_1_0(
                data["parents"]
            )
        )
    if "tags" in data:
        import aws_sdk_verifiedpermissions.types.entity_cedar_tags

        out["tags"] = (
            aws_sdk_verifiedpermissions.types.entity_cedar_tags.deserialize_aws_json_1_0(
                data["tags"]
            )
        )
    return out
