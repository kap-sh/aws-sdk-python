"""Generated from Smithy shape ``com.amazonaws.connectcases#UpdateRelatedItemResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_connectcases.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.association_time
    import aws_sdk_connectcases.types.related_item_arn
    import aws_sdk_connectcases.types.related_item_content
    import aws_sdk_connectcases.types.related_item_id
    import aws_sdk_connectcases.types.related_item_type
    import aws_sdk_connectcases.types.tags
    import aws_sdk_connectcases.types.user_union


class UpdateRelatedItemResponse(TypedDict, closed=True):
    related_item_id: "aws_sdk_connectcases.types.related_item_id.RelatedItemId"
    """<p>The unique identifier of the updated related item.</p>"""
    related_item_arn: "aws_sdk_connectcases.types.related_item_arn.RelatedItemArn"
    """<p>The Amazon Resource Name (ARN) of the updated related item.</p>"""
    type: "aws_sdk_connectcases.types.related_item_type.RelatedItemType"
    """<p>Type of the updated related item.</p>"""
    content: "aws_sdk_connectcases.types.related_item_content.RelatedItemContent"
    """<p>Represents the content of the updated related item.</p>"""
    association_time: "aws_sdk_connectcases.types.association_time.AssociationTime"
    """<p>Time at which the related item was associated with the case.</p>"""
    tags: NotRequired["aws_sdk_connectcases.types.tags.Tags"]
    """<p>A map of of key-value pairs that represent tags on a resource. Tags are used to organize, track, or control access for this resource.</p>"""
    last_updated_user: NotRequired["aws_sdk_connectcases.types.user_union.UserUnion"]
    """<p>Represents the last user that updated the related item.</p>"""
    created_by: NotRequired["aws_sdk_connectcases.types.user_union.UserUnion"]
    """<p>Represents the creator of the related item.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRelatedItemResponse) -> dict:
    out: dict = {}
    out["relatedItemId"] = value["related_item_id"]
    out["relatedItemArn"] = value["related_item_arn"]
    out["type"] = value["type"]
    import aws_sdk_connectcases.types.related_item_content

    out["content"] = aws_sdk_connectcases.types.related_item_content.serialize_json(
        value["content"]
    )
    import aws_sdk_connectcases.types.association_time

    out["associationTime"] = aws_sdk_connectcases.types.association_time.serialize_json(
        value["association_time"]
    )
    if "tags" in value:
        import aws_sdk_connectcases.types.tags

        out["tags"] = aws_sdk_connectcases.types.tags.serialize_json(value["tags"])
    if "last_updated_user" in value:
        import aws_sdk_connectcases.types.user_union

        out["lastUpdatedUser"] = aws_sdk_connectcases.types.user_union.serialize_json(
            value["last_updated_user"]
        )
    if "created_by" in value:
        import aws_sdk_connectcases.types.user_union

        out["createdBy"] = aws_sdk_connectcases.types.user_union.serialize_json(
            value["created_by"]
        )
    return out


def deserialize_json(data: dict) -> UpdateRelatedItemResponse:
    out: UpdateRelatedItemResponse = {}  # type: ignore[typeddict-item]
    if "relatedItemId" in data:
        out["related_item_id"] = data["relatedItemId"]
    else:
        raise DeserializationError("UpdateRelatedItemResponse.related_item_id required")
    if "relatedItemArn" in data:
        out["related_item_arn"] = data["relatedItemArn"]
    else:
        raise DeserializationError(
            "UpdateRelatedItemResponse.related_item_arn required"
        )
    if "type" in data:
        out["type"] = data["type"]
    else:
        raise DeserializationError("UpdateRelatedItemResponse.type required")
    if "content" in data:
        import aws_sdk_connectcases.types.related_item_content

        out["content"] = (
            aws_sdk_connectcases.types.related_item_content.deserialize_json(
                data["content"]
            )
        )
    else:
        raise DeserializationError("UpdateRelatedItemResponse.content required")
    if "associationTime" in data:
        import aws_sdk_connectcases.types.association_time

        out["association_time"] = (
            aws_sdk_connectcases.types.association_time.deserialize_json(
                data["associationTime"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateRelatedItemResponse.association_time required"
        )
    if "tags" in data:
        import aws_sdk_connectcases.types.tags

        out["tags"] = aws_sdk_connectcases.types.tags.deserialize_json(data["tags"])
    if "lastUpdatedUser" in data:
        import aws_sdk_connectcases.types.user_union

        out["last_updated_user"] = (
            aws_sdk_connectcases.types.user_union.deserialize_json(
                data["lastUpdatedUser"]
            )
        )
    if "createdBy" in data:
        import aws_sdk_connectcases.types.user_union

        out["created_by"] = aws_sdk_connectcases.types.user_union.deserialize_json(
            data["createdBy"]
        )
    return out
