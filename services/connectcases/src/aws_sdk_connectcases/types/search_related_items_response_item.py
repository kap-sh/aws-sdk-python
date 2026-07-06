"""Generated from Smithy shape ``com.amazonaws.connectcases#SearchRelatedItemsResponseItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_connectcases.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.association_time
    import aws_sdk_connectcases.types.related_item_content
    import aws_sdk_connectcases.types.related_item_id
    import aws_sdk_connectcases.types.related_item_type
    import aws_sdk_connectcases.types.tags
    import aws_sdk_connectcases.types.user_union


class SearchRelatedItemsResponseItem(TypedDict, closed=True):
    related_item_id: "aws_sdk_connectcases.types.related_item_id.RelatedItemId"
    """<p>Unique identifier of a related item.</p>"""
    type: "aws_sdk_connectcases.types.related_item_type.RelatedItemType"
    """<p>Type of a related item.</p>"""
    association_time: "aws_sdk_connectcases.types.association_time.AssociationTime"
    """<p>Time at which a related item was associated with a case.</p>"""
    content: "aws_sdk_connectcases.types.related_item_content.RelatedItemContent"
    """<p>Represents the content of a particular type of related item.</p>"""
    tags: NotRequired["aws_sdk_connectcases.types.tags.Tags"]
    """<p>A map of of key-value pairs that represent tags on a resource. Tags are used to organize, track, or control access for this resource.</p>"""
    performed_by: NotRequired["aws_sdk_connectcases.types.user_union.UserUnion"]
    """<p>Represents the creator of the related item.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchRelatedItemsResponseItem) -> dict:
    out: dict = {}
    out["relatedItemId"] = value["related_item_id"]
    out["type"] = value["type"]
    import aws_sdk_connectcases.types.association_time

    out["associationTime"] = aws_sdk_connectcases.types.association_time.serialize_json(
        value["association_time"]
    )
    import aws_sdk_connectcases.types.related_item_content

    out["content"] = aws_sdk_connectcases.types.related_item_content.serialize_json(
        value["content"]
    )
    if "tags" in value:
        import aws_sdk_connectcases.types.tags

        out["tags"] = aws_sdk_connectcases.types.tags.serialize_json(value["tags"])
    if "performed_by" in value:
        import aws_sdk_connectcases.types.user_union

        out["performedBy"] = aws_sdk_connectcases.types.user_union.serialize_json(
            value["performed_by"]
        )
    return out


def deserialize_json(data: dict) -> SearchRelatedItemsResponseItem:
    out: SearchRelatedItemsResponseItem = {}  # type: ignore[typeddict-item]
    if "relatedItemId" in data:
        out["related_item_id"] = data["relatedItemId"]
    else:
        raise DeserializationError(
            "SearchRelatedItemsResponseItem.related_item_id required"
        )
    if "type" in data:
        out["type"] = data["type"]
    else:
        raise DeserializationError("SearchRelatedItemsResponseItem.type required")
    if "associationTime" in data:
        import aws_sdk_connectcases.types.association_time

        out["association_time"] = (
            aws_sdk_connectcases.types.association_time.deserialize_json(
                data["associationTime"]
            )
        )
    else:
        raise DeserializationError(
            "SearchRelatedItemsResponseItem.association_time required"
        )
    if "content" in data:
        import aws_sdk_connectcases.types.related_item_content

        out["content"] = (
            aws_sdk_connectcases.types.related_item_content.deserialize_json(
                data["content"]
            )
        )
    else:
        raise DeserializationError("SearchRelatedItemsResponseItem.content required")
    if "tags" in data:
        import aws_sdk_connectcases.types.tags

        out["tags"] = aws_sdk_connectcases.types.tags.deserialize_json(data["tags"])
    if "performedBy" in data:
        import aws_sdk_connectcases.types.user_union

        out["performed_by"] = aws_sdk_connectcases.types.user_union.deserialize_json(
            data["performedBy"]
        )
    return out
