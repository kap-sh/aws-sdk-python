"""Generated from Smithy shape ``com.amazonaws.datazone#DeleteAccountPoolInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.account_pool_id
    import capo_datazone.types.domain_id


class DeleteAccountPoolInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The ID of the domain where the account pool is deleted.</p>"""
    identifier: "capo_datazone.types.account_pool_id.AccountPoolId"
    """<p>The ID of the account pool to be deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAccountPoolInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteAccountPoolInput:
    out: DeleteAccountPoolInput = {}  # type: ignore[typeddict-item]
    return out
