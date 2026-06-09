"""Generated from Smithy shape ``com.amazonaws.iam#RejectDelegationRequestRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iam._protocol.xml import Element
from aws_sdk_iam.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iam.types.delegation_request_id_type
    import aws_sdk_iam.types.notes_type


class RejectDelegationRequestRequest(TypedDict):
    delegation_request_id: (
        "aws_sdk_iam.types.delegation_request_id_type.delegationRequestIdType"
    )
    """<p>The unique identifier of the delegation request to reject.</p>"""
    notes: NotRequired["aws_sdk_iam.types.notes_type.notesType"]
    """<p>Optional notes explaining the reason for rejecting the delegation request.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: RejectDelegationRequestRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.DelegationRequestId", str(value["delegation_request_id"])))
    if "notes" in value:
        pairs.append((f"{prefix}.Notes", str(value["notes"])))


def deserialize_query(el: Element) -> RejectDelegationRequestRequest:
    out: RejectDelegationRequestRequest = {}  # type: ignore[typeddict-item]
    child_delegation_request_id = el.find("DelegationRequestId")
    if child_delegation_request_id is not None:
        out["delegation_request_id"] = str(child_delegation_request_id.text or "")
    else:
        raise DeserializationError(
            "RejectDelegationRequestRequest.delegation_request_id required"
        )
    child_notes = el.find("Notes")
    if child_notes is not None:
        out["notes"] = str(child_notes.text or "")
    return out
