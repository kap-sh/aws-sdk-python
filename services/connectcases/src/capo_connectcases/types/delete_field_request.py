"""Generated from Smithy shape ``com.amazonaws.connectcases#DeleteFieldRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connectcases.types.domain_id
    import capo_connectcases.types.field_id


class DeleteFieldRequest(TypedDict, closed=True):
    domain_id: "capo_connectcases.types.domain_id.DomainId"
    """<p>The unique identifier of the Cases domain.</p>"""
    field_id: "capo_connectcases.types.field_id.FieldId"
    """<p>Unique identifier of the field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteFieldRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteFieldRequest:
    out: DeleteFieldRequest = {}  # type: ignore[typeddict-item]
    return out
