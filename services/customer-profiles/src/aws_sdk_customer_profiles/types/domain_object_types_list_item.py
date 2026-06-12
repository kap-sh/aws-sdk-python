"""Generated from Smithy shape ``com.amazonaws.customerprofiles#DomainObjectTypesListItem``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.sensitive_string1_to10000
    import aws_sdk_customer_profiles.types.tag_map
    import aws_sdk_customer_profiles.types.timestamp
    import aws_sdk_customer_profiles.types.type_name


class DomainObjectTypesListItem(TypedDict):
    object_type_name: "aws_sdk_customer_profiles.types.type_name.typeName"
    """<p>The name that identifies the object type within the domain.</p>"""
    description: NotRequired[
        "aws_sdk_customer_profiles.types.sensitive_string1_to10000.sensitiveString1To10000"
    ]
    """<p>A description explaining the purpose and characteristics of this object type.</p>"""
    created_at: NotRequired["aws_sdk_customer_profiles.types.timestamp.timestamp"]
    """<p>The timestamp of when the domain object type was created.</p>"""
    last_updated_at: NotRequired["aws_sdk_customer_profiles.types.timestamp.timestamp"]
    """<p>The timestamp of when the domain object type was most recently edited.</p>"""
    tags: NotRequired["aws_sdk_customer_profiles.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DomainObjectTypesListItem) -> dict:
    out: dict = {}
    out["ObjectTypeName"] = value["object_type_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "created_at" in value:
        import aws_sdk_customer_profiles.types.timestamp

        out["CreatedAt"] = aws_sdk_customer_profiles.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "last_updated_at" in value:
        import aws_sdk_customer_profiles.types.timestamp

        out["LastUpdatedAt"] = aws_sdk_customer_profiles.types.timestamp.serialize_json(
            value["last_updated_at"]
        )
    if "tags" in value:
        import aws_sdk_customer_profiles.types.tag_map

        out["Tags"] = aws_sdk_customer_profiles.types.tag_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> DomainObjectTypesListItem:
    out: DomainObjectTypesListItem = {}  # type: ignore[typeddict-item]
    if "ObjectTypeName" in data:
        out["object_type_name"] = data["ObjectTypeName"]
    else:
        raise DeserializationError(
            "DomainObjectTypesListItem.object_type_name required"
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "CreatedAt" in data:
        import aws_sdk_customer_profiles.types.timestamp

        out["created_at"] = aws_sdk_customer_profiles.types.timestamp.deserialize_json(
            data["CreatedAt"]
        )
    if "LastUpdatedAt" in data:
        import aws_sdk_customer_profiles.types.timestamp

        out["last_updated_at"] = (
            aws_sdk_customer_profiles.types.timestamp.deserialize_json(
                data["LastUpdatedAt"]
            )
        )
    if "Tags" in data:
        import aws_sdk_customer_profiles.types.tag_map

        out["tags"] = aws_sdk_customer_profiles.types.tag_map.deserialize_json(
            data["Tags"]
        )
    return out
