"""Generated from Smithy shape ``com.amazonaws.securityhub#DeclineInvitationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.account_id_list


class DeclineInvitationsRequest(TypedDict, closed=True):
    account_ids: NotRequired["aws_sdk_securityhub.types.account_id_list.AccountIdList"]
    """<p>The list of prospective member account IDs for which to decline an invitation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeclineInvitationsRequest) -> dict:
    out: dict = {}
    if "account_ids" in value:
        import aws_sdk_securityhub.types.account_id_list

        out["AccountIds"] = aws_sdk_securityhub.types.account_id_list.serialize_json(
            value["account_ids"]
        )
    return out


def deserialize_json(data: dict) -> DeclineInvitationsRequest:
    out: DeclineInvitationsRequest = {}  # type: ignore[typeddict-item]
    if "AccountIds" in data:
        import aws_sdk_securityhub.types.account_id_list

        out["account_ids"] = aws_sdk_securityhub.types.account_id_list.deserialize_json(
            data["AccountIds"]
        )
    return out
