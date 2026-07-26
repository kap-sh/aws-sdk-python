"""Generated from Smithy shape ``com.amazonaws.iam#AssociateDelegationRequestRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iam._protocol.xml import Element
from capo_iam.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iam.types.delegation_request_id_type


class AssociateDelegationRequestRequest(TypedDict, closed=True):
    delegation_request_id: (
        "capo_iam.types.delegation_request_id_type.delegationRequestIdType"
    )
    """<p>The unique identifier of the delegation request to associate.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: AssociateDelegationRequestRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.DelegationRequestId", str(value["delegation_request_id"])))


def deserialize_query(el: Element) -> AssociateDelegationRequestRequest:
    out: AssociateDelegationRequestRequest = {}  # type: ignore[typeddict-item]
    child_delegation_request_id = el.find("DelegationRequestId")
    if child_delegation_request_id is not None:
        out["delegation_request_id"] = str(child_delegation_request_id.text or "")
    else:
        raise DeserializationError(
            "AssociateDelegationRequestRequest.delegation_request_id required"
        )
    return out
