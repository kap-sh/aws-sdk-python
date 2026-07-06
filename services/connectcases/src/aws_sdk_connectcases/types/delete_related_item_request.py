"""Generated from Smithy shape ``com.amazonaws.connectcases#DeleteRelatedItemRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.case_id
    import aws_sdk_connectcases.types.domain_id
    import aws_sdk_connectcases.types.related_item_id


class DeleteRelatedItemRequest(TypedDict, closed=True):
    domain_id: "aws_sdk_connectcases.types.domain_id.DomainId"
    """<p>A unique identifier of the Cases domain.</p>"""
    case_id: "aws_sdk_connectcases.types.case_id.CaseId"
    """<p>A unique identifier of the case.</p>"""
    related_item_id: "aws_sdk_connectcases.types.related_item_id.RelatedItemId"
    """<p>A unique identifier of a related item.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteRelatedItemRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteRelatedItemRequest:
    out: DeleteRelatedItemRequest = {}  # type: ignore[typeddict-item]
    return out
