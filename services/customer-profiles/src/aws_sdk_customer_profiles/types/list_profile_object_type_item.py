"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ListProfileObjectTypeItem``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.min_size0
    import aws_sdk_customer_profiles.types.min_size1
    import aws_sdk_customer_profiles.types.tag_map
    import aws_sdk_customer_profiles.types.text
    import aws_sdk_customer_profiles.types.timestamp
    import aws_sdk_customer_profiles.types.type_name


class ListProfileObjectTypeItem(TypedDict):
    object_type_name: "aws_sdk_customer_profiles.types.type_name.typeName"
    """<p>The name of the profile object type.</p>"""
    description: "aws_sdk_customer_profiles.types.text.text"
    """<p>Description of the profile object type.</p>"""
    created_at: NotRequired["aws_sdk_customer_profiles.types.timestamp.timestamp"]
    """<p>The timestamp of when the domain was created.</p>"""
    last_updated_at: NotRequired["aws_sdk_customer_profiles.types.timestamp.timestamp"]
    """<p>The timestamp of when the profile object type was most recently edited.</p>"""
    max_profile_object_count: NotRequired[
        "aws_sdk_customer_profiles.types.min_size1.minSize1"
    ]
    """<p>The amount of profile object max count assigned to the object type.</p>"""
    max_available_profile_object_count: NotRequired[
        "aws_sdk_customer_profiles.types.min_size0.minSize0"
    ]
    """<p>The amount of provisioned profile object max count available.</p>"""
    source_priority: NotRequired["aws_sdk_customer_profiles.types.min_size1.minSize1"]
    """<p>An integer that determines the priority of this object type when data from multiple sources is ingested. Lower values take priority. Object types without a specified source priority default to the lowest priority.</p>"""
    tags: NotRequired["aws_sdk_customer_profiles.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListProfileObjectTypeItem) -> dict:
    out: dict = {}
    out["ObjectTypeName"] = value["object_type_name"]
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
    if "max_profile_object_count" in value:
        out["MaxProfileObjectCount"] = value["max_profile_object_count"]
    if "max_available_profile_object_count" in value:
        out["MaxAvailableProfileObjectCount"] = value[
            "max_available_profile_object_count"
        ]
    if "source_priority" in value:
        out["SourcePriority"] = value["source_priority"]
    if "tags" in value:
        import aws_sdk_customer_profiles.types.tag_map

        out["Tags"] = aws_sdk_customer_profiles.types.tag_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> ListProfileObjectTypeItem:
    out: ListProfileObjectTypeItem = {}  # type: ignore[typeddict-item]
    if "ObjectTypeName" in data:
        out["object_type_name"] = data["ObjectTypeName"]
    else:
        raise DeserializationError(
            "ListProfileObjectTypeItem.object_type_name required"
        )
    if "Description" in data:
        out["description"] = data["Description"]
    else:
        raise DeserializationError("ListProfileObjectTypeItem.description required")
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
    if "MaxProfileObjectCount" in data:
        out["max_profile_object_count"] = data["MaxProfileObjectCount"]
    if "MaxAvailableProfileObjectCount" in data:
        out["max_available_profile_object_count"] = data[
            "MaxAvailableProfileObjectCount"
        ]
    if "SourcePriority" in data:
        out["source_priority"] = data["SourcePriority"]
    if "Tags" in data:
        import aws_sdk_customer_profiles.types.tag_map

        out["tags"] = aws_sdk_customer_profiles.types.tag_map.deserialize_json(
            data["Tags"]
        )
    return out
