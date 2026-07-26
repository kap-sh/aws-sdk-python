"""Generated from Smithy shape ``com.amazonaws.connectcases#GetFieldResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connectcases.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connectcases.types.created_time
    import capo_connectcases.types.deleted
    import capo_connectcases.types.field_arn
    import capo_connectcases.types.field_attributes
    import capo_connectcases.types.field_description
    import capo_connectcases.types.field_id
    import capo_connectcases.types.field_name
    import capo_connectcases.types.field_namespace
    import capo_connectcases.types.field_type
    import capo_connectcases.types.last_modified_time
    import capo_connectcases.types.tags


class GetFieldResponse(TypedDict, closed=True):
    field_id: "capo_connectcases.types.field_id.FieldId"
    """<p>Unique identifier of the field.</p>"""
    name: "capo_connectcases.types.field_name.FieldName"
    """<p>Name of the field.</p>"""
    field_arn: "capo_connectcases.types.field_arn.FieldArn"
    """<p>The Amazon Resource Name (ARN) of the field.</p>"""
    description: NotRequired[
        "capo_connectcases.types.field_description.FieldDescription"
    ]
    """<p>Description of the field.</p>"""
    type: "capo_connectcases.types.field_type.FieldType"
    """<p>Type of the field.</p>"""
    namespace: "capo_connectcases.types.field_namespace.FieldNamespace"
    """<p>Namespace of the field.</p>"""
    tags: NotRequired["capo_connectcases.types.tags.Tags"]
    """<p>A map of of key-value pairs that represent tags on a resource. Tags are used to organize, track, or control access for this resource.</p>"""
    deleted: "capo_connectcases.types.deleted.Deleted"
    """<p>Denotes whether or not the resource has been deleted.</p>"""
    created_time: NotRequired["capo_connectcases.types.created_time.CreatedTime"]
    """<p>Timestamp at which the resource was created.</p>"""
    last_modified_time: NotRequired[
        "capo_connectcases.types.last_modified_time.LastModifiedTime"
    ]
    """<p>Timestamp at which the resource was created or last modified.</p>"""
    attributes: NotRequired["capo_connectcases.types.field_attributes.FieldAttributes"]
    """<p>Union of field attributes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFieldResponse) -> dict:
    out: dict = {}
    out["fieldId"] = value["field_id"]
    out["name"] = value["name"]
    out["fieldArn"] = value["field_arn"]
    if "description" in value:
        out["description"] = value["description"]
    out["type"] = value["type"]
    out["namespace"] = value["namespace"]
    if "tags" in value:
        import capo_connectcases.types.tags

        out["tags"] = capo_connectcases.types.tags.serialize_json(value["tags"])
    out["deleted"] = value.get("deleted", False)
    if "created_time" in value:
        import capo_connectcases.types.created_time

        out["createdTime"] = capo_connectcases.types.created_time.serialize_json(
            value["created_time"]
        )
    if "last_modified_time" in value:
        import capo_connectcases.types.last_modified_time

        out["lastModifiedTime"] = (
            capo_connectcases.types.last_modified_time.serialize_json(
                value["last_modified_time"]
            )
        )
    if "attributes" in value:
        import capo_connectcases.types.field_attributes

        out["attributes"] = capo_connectcases.types.field_attributes.serialize_json(
            value["attributes"]
        )
    return out


def deserialize_json(data: dict) -> GetFieldResponse:
    out: GetFieldResponse = {}  # type: ignore[typeddict-item]
    if "fieldId" in data:
        out["field_id"] = data["fieldId"]
    else:
        raise DeserializationError("GetFieldResponse.field_id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GetFieldResponse.name required")
    if "fieldArn" in data:
        out["field_arn"] = data["fieldArn"]
    else:
        raise DeserializationError("GetFieldResponse.field_arn required")
    if "description" in data:
        out["description"] = data["description"]
    if "type" in data:
        out["type"] = data["type"]
    else:
        raise DeserializationError("GetFieldResponse.type required")
    if "namespace" in data:
        out["namespace"] = data["namespace"]
    else:
        raise DeserializationError("GetFieldResponse.namespace required")
    if "tags" in data:
        import capo_connectcases.types.tags

        out["tags"] = capo_connectcases.types.tags.deserialize_json(data["tags"])
    if "deleted" in data:
        out["deleted"] = data["deleted"]
    else:
        out["deleted"] = False
    if "createdTime" in data:
        import capo_connectcases.types.created_time

        out["created_time"] = capo_connectcases.types.created_time.deserialize_json(
            data["createdTime"]
        )
    if "lastModifiedTime" in data:
        import capo_connectcases.types.last_modified_time

        out["last_modified_time"] = (
            capo_connectcases.types.last_modified_time.deserialize_json(
                data["lastModifiedTime"]
            )
        )
    if "attributes" in data:
        import capo_connectcases.types.field_attributes

        out["attributes"] = capo_connectcases.types.field_attributes.deserialize_json(
            data["attributes"]
        )
    return out
