"""Generated from Smithy shape ``com.amazonaws.connectcases#DeleteCaseRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connectcases.types.case_id
    import capo_connectcases.types.domain_id


class DeleteCaseRequest(TypedDict, closed=True):
    domain_id: "capo_connectcases.types.domain_id.DomainId"
    """<p>A unique identifier of the Cases domain.</p>"""
    case_id: "capo_connectcases.types.case_id.CaseId"
    """<p>A unique identifier of the case.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteCaseRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteCaseRequest:
    out: DeleteCaseRequest = {}  # type: ignore[typeddict-item]
    return out
