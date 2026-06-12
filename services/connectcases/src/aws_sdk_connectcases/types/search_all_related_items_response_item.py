"""Generated from Smithy shape ``com.amazonaws.connectcases#SearchAllRelatedItemsResponseItem``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_connectcases.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.association_time
    import aws_sdk_connectcases.types.case_id
    import aws_sdk_connectcases.types.related_item_content
    import aws_sdk_connectcases.types.related_item_id
    import aws_sdk_connectcases.types.related_item_type
    import aws_sdk_connectcases.types.tags
    import aws_sdk_connectcases.types.user_union


class SearchAllRelatedItemsResponseItem(TypedDict):
    related_item_id: "aws_sdk_connectcases.types.related_item_id.RelatedItemId"
    """<p>Unique identifier of a related item.</p>"""
    case_id: "aws_sdk_connectcases.types.case_id.CaseId"
    """<p>A unique identifier of the case.</p>"""
    type: "aws_sdk_connectcases.types.related_item_type.RelatedItemType"
    """<p>Type of a related item.</p>"""
    association_time: "aws_sdk_connectcases.types.association_time.AssociationTime"
    """<p>Time at which a related item was associated with a case.</p>"""
    content: "aws_sdk_connectcases.types.related_item_content.RelatedItemContent"
    performed_by: NotRequired["aws_sdk_connectcases.types.user_union.UserUnion"]
    tags: NotRequired["aws_sdk_connectcases.types.tags.Tags"]
    """<p>A map of of key-value pairs that represent tags on a resource. Tags are used to organize, track, or control access for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchAllRelatedItemsResponseItem) -> dict:
    out: dict = {}
    out["relatedItemId"] = value["related_item_id"]
    out["caseId"] = value["case_id"]
    out["type"] = value["type"]
    import aws_sdk_connectcases.types.association_time

    out["associationTime"] = aws_sdk_connectcases.types.association_time.serialize_json(
        value["association_time"]
    )
    import aws_sdk_connectcases.types.related_item_content

    out["content"] = aws_sdk_connectcases.types.related_item_content.serialize_json(
        value["content"]
    )
    if "performed_by" in value:
        import aws_sdk_connectcases.types.user_union

        out["performedBy"] = aws_sdk_connectcases.types.user_union.serialize_json(
            value["performed_by"]
        )
    if "tags" in value:
        import aws_sdk_connectcases.types.tags

        out["tags"] = aws_sdk_connectcases.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> SearchAllRelatedItemsResponseItem:
    out: SearchAllRelatedItemsResponseItem = {}  # type: ignore[typeddict-item]
    if "relatedItemId" in data:
        out["related_item_id"] = data["relatedItemId"]
    else:
        raise DeserializationError(
            "SearchAllRelatedItemsResponseItem.related_item_id required"
        )
    if "caseId" in data:
        out["case_id"] = data["caseId"]
    else:
        raise DeserializationError("SearchAllRelatedItemsResponseItem.case_id required")
    if "type" in data:
        out["type"] = data["type"]
    else:
        raise DeserializationError("SearchAllRelatedItemsResponseItem.type required")
    if "associationTime" in data:
        import aws_sdk_connectcases.types.association_time

        out["association_time"] = (
            aws_sdk_connectcases.types.association_time.deserialize_json(
                data["associationTime"]
            )
        )
    else:
        raise DeserializationError(
            "SearchAllRelatedItemsResponseItem.association_time required"
        )
    if "content" in data:
        import aws_sdk_connectcases.types.related_item_content

        out["content"] = (
            aws_sdk_connectcases.types.related_item_content.deserialize_json(
                data["content"]
            )
        )
    else:
        raise DeserializationError("SearchAllRelatedItemsResponseItem.content required")
    if "performedBy" in data:
        import aws_sdk_connectcases.types.user_union

        out["performed_by"] = aws_sdk_connectcases.types.user_union.deserialize_json(
            data["performedBy"]
        )
    if "tags" in data:
        import aws_sdk_connectcases.types.tags

        out["tags"] = aws_sdk_connectcases.types.tags.deserialize_json(data["tags"])
    return out
