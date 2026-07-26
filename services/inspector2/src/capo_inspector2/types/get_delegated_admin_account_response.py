"""Generated from Smithy shape ``com.amazonaws.inspector2#GetDelegatedAdminAccountResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.delegated_admin


class GetDelegatedAdminAccountResponse(TypedDict, closed=True):
    delegated_admin: NotRequired["capo_inspector2.types.delegated_admin.DelegatedAdmin"]
    """<p>The Amazon Web Services account ID of the Amazon Inspector delegated administrator.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDelegatedAdminAccountResponse) -> dict:
    out: dict = {}
    if "delegated_admin" in value:
        import capo_inspector2.types.delegated_admin

        out["delegatedAdmin"] = capo_inspector2.types.delegated_admin.serialize_json(
            value["delegated_admin"]
        )
    return out


def deserialize_json(data: dict) -> GetDelegatedAdminAccountResponse:
    out: GetDelegatedAdminAccountResponse = {}  # type: ignore[typeddict-item]
    if "delegatedAdmin" in data:
        import capo_inspector2.types.delegated_admin

        out["delegated_admin"] = capo_inspector2.types.delegated_admin.deserialize_json(
            data["delegatedAdmin"]
        )
    return out
