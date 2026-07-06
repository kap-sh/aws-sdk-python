"""Generated from Smithy shape ``com.amazonaws.connectcases#DeleteFieldRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.domain_id
    import aws_sdk_connectcases.types.field_id


class DeleteFieldRequest(TypedDict, closed=True):
    domain_id: "aws_sdk_connectcases.types.domain_id.DomainId"
    """<p>The unique identifier of the Cases domain.</p>"""
    field_id: "aws_sdk_connectcases.types.field_id.FieldId"
    """<p>Unique identifier of the field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteFieldRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteFieldRequest:
    out: DeleteFieldRequest = {}  # type: ignore[typeddict-item]
    return out
