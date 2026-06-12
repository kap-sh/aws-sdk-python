"""Generated from Smithy shape ``com.amazonaws.connectcases#DeleteCaseRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.case_id
    import aws_sdk_connectcases.types.domain_id


class DeleteCaseRequest(TypedDict):
    domain_id: "aws_sdk_connectcases.types.domain_id.DomainId"
    """<p>A unique identifier of the Cases domain.</p>"""
    case_id: "aws_sdk_connectcases.types.case_id.CaseId"
    """<p>A unique identifier of the case.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteCaseRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteCaseRequest:
    out: DeleteCaseRequest = {}  # type: ignore[typeddict-item]
    return out
