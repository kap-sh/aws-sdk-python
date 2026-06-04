"""Generated from Smithy shape ``com.amazonaws.iam#UpdateDelegationRequestRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_iam.errors import DeserializationError
from aws_sdk_iam._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_iam.types.delegation_request_id_type
    import aws_sdk_iam.types.notes_type


class UpdateDelegationRequestRequest(TypedDict):
    delegation_request_id: (
        "aws_sdk_iam.types.delegation_request_id_type.delegationRequestIdType"
    )
    """<p>The unique identifier of the delegation request to update.</p>"""
    notes: NotRequired["aws_sdk_iam.types.notes_type.notesType"]
    """<p>Additional notes or comments to add to the delegation request.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: UpdateDelegationRequestRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.DelegationRequestId", str(value["delegation_request_id"])))
    if "notes" in value:
        pairs.append((f"{prefix}.Notes", str(value["notes"])))


def deserialize_query(el: Element) -> UpdateDelegationRequestRequest:
    out: UpdateDelegationRequestRequest = {}  # type: ignore[typeddict-item]
    child_delegation_request_id = el.find("DelegationRequestId")
    if child_delegation_request_id is not None:
        out["delegation_request_id"] = str(child_delegation_request_id.text or "")
    else:
        raise DeserializationError(
            "UpdateDelegationRequestRequest.delegation_request_id required"
        )
    child_notes = el.find("Notes")
    if child_notes is not None:
        out["notes"] = str(child_notes.text or "")
    return out
