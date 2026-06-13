"""Generated from Smithy shape ``com.amazonaws.inspector2#GetDelegatedAdminAccountResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.delegated_admin


class GetDelegatedAdminAccountResponse(TypedDict):
    delegated_admin: NotRequired[
        "aws_sdk_inspector2.types.delegated_admin.DelegatedAdmin"
    ]
    """<p>The Amazon Web Services account ID of the Amazon Inspector delegated administrator.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDelegatedAdminAccountResponse) -> dict:
    out: dict = {}
    if "delegated_admin" in value:
        import aws_sdk_inspector2.types.delegated_admin

        out["delegatedAdmin"] = aws_sdk_inspector2.types.delegated_admin.serialize_json(
            value["delegated_admin"]
        )
    return out


def deserialize_json(data: dict) -> GetDelegatedAdminAccountResponse:
    out: GetDelegatedAdminAccountResponse = {}  # type: ignore[typeddict-item]
    if "delegatedAdmin" in data:
        import aws_sdk_inspector2.types.delegated_admin

        out["delegated_admin"] = (
            aws_sdk_inspector2.types.delegated_admin.deserialize_json(
                data["delegatedAdmin"]
            )
        )
    return out
