"""Generated from Smithy shape ``com.amazonaws.connectcases#CreateRelatedItemRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_connectcases.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.case_id
    import aws_sdk_connectcases.types.domain_id
    import aws_sdk_connectcases.types.related_item_input_content
    import aws_sdk_connectcases.types.related_item_type
    import aws_sdk_connectcases.types.user_union


class CreateRelatedItemRequest(TypedDict):
    domain_id: "aws_sdk_connectcases.types.domain_id.DomainId"
    """<p>The unique identifier of the Cases domain. </p>"""
    case_id: "aws_sdk_connectcases.types.case_id.CaseId"
    """<p>A unique identifier of the case.</p>"""
    type: "aws_sdk_connectcases.types.related_item_type.RelatedItemType"
    """<p>The type of a related item.</p>"""
    content: (
        "aws_sdk_connectcases.types.related_item_input_content.RelatedItemInputContent"
    )
    """<p>The content of a related item to be created.</p>"""
    performed_by: NotRequired["aws_sdk_connectcases.types.user_union.UserUnion"]
    """<p>Represents the creator of the related item.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRelatedItemRequest) -> dict:
    out: dict = {}
    out["type"] = value["type"]
    import aws_sdk_connectcases.types.related_item_input_content

    out["content"] = (
        aws_sdk_connectcases.types.related_item_input_content.serialize_json(
            value["content"]
        )
    )
    if "performed_by" in value:
        import aws_sdk_connectcases.types.user_union

        out["performedBy"] = aws_sdk_connectcases.types.user_union.serialize_json(
            value["performed_by"]
        )
    return out


def deserialize_json(data: dict) -> CreateRelatedItemRequest:
    out: CreateRelatedItemRequest = {}  # type: ignore[typeddict-item]
    if "type" in data:
        out["type"] = data["type"]
    else:
        raise DeserializationError("CreateRelatedItemRequest.type required")
    if "content" in data:
        import aws_sdk_connectcases.types.related_item_input_content

        out["content"] = (
            aws_sdk_connectcases.types.related_item_input_content.deserialize_json(
                data["content"]
            )
        )
    else:
        raise DeserializationError("CreateRelatedItemRequest.content required")
    if "performedBy" in data:
        import aws_sdk_connectcases.types.user_union

        out["performed_by"] = aws_sdk_connectcases.types.user_union.deserialize_json(
            data["performedBy"]
        )
    return out
