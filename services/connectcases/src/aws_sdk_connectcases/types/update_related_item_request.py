"""Generated from Smithy shape ``com.amazonaws.connectcases#UpdateRelatedItemRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_connectcases.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.case_id
    import aws_sdk_connectcases.types.domain_id
    import aws_sdk_connectcases.types.related_item_id
    import aws_sdk_connectcases.types.related_item_update_content
    import aws_sdk_connectcases.types.user_union


class UpdateRelatedItemRequest(TypedDict):
    domain_id: "aws_sdk_connectcases.types.domain_id.DomainId"
    """<p>The unique identifier of the Cases domain. </p>"""
    case_id: "aws_sdk_connectcases.types.case_id.CaseId"
    """<p>A unique identifier of the case.</p>"""
    related_item_id: "aws_sdk_connectcases.types.related_item_id.RelatedItemId"
    """<p>Unique identifier of a related item.</p>"""
    content: "aws_sdk_connectcases.types.related_item_update_content.RelatedItemUpdateContent"
    """<p>The content of a related item to be updated.</p>"""
    performed_by: NotRequired["aws_sdk_connectcases.types.user_union.UserUnion"]
    """<p>Represents the user who performed the update of the related item.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRelatedItemRequest) -> dict:
    out: dict = {}
    import aws_sdk_connectcases.types.related_item_update_content

    out["content"] = (
        aws_sdk_connectcases.types.related_item_update_content.serialize_json(
            value["content"]
        )
    )
    if "performed_by" in value:
        import aws_sdk_connectcases.types.user_union

        out["performedBy"] = aws_sdk_connectcases.types.user_union.serialize_json(
            value["performed_by"]
        )
    return out


def deserialize_json(data: dict) -> UpdateRelatedItemRequest:
    out: UpdateRelatedItemRequest = {}  # type: ignore[typeddict-item]
    if "content" in data:
        import aws_sdk_connectcases.types.related_item_update_content

        out["content"] = (
            aws_sdk_connectcases.types.related_item_update_content.deserialize_json(
                data["content"]
            )
        )
    else:
        raise DeserializationError("UpdateRelatedItemRequest.content required")
    if "performedBy" in data:
        import aws_sdk_connectcases.types.user_union

        out["performed_by"] = aws_sdk_connectcases.types.user_union.deserialize_json(
            data["performedBy"]
        )
    return out
