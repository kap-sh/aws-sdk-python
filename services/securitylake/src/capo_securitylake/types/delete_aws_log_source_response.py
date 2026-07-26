"""Generated from Smithy shape ``com.amazonaws.securitylake#DeleteAwsLogSourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securitylake.types.account_list


class DeleteAwsLogSourceResponse(TypedDict, closed=True):
    failed: NotRequired["capo_securitylake.types.account_list.AccountList"]
    """<p>Deletion of the Amazon Web Services sources failed as the account is not a part of the organization.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAwsLogSourceResponse) -> dict:
    out: dict = {}
    if "failed" in value:
        import capo_securitylake.types.account_list

        out["failed"] = capo_securitylake.types.account_list.serialize_json(
            value["failed"]
        )
    return out


def deserialize_json(data: dict) -> DeleteAwsLogSourceResponse:
    out: DeleteAwsLogSourceResponse = {}  # type: ignore[typeddict-item]
    if "failed" in data:
        import capo_securitylake.types.account_list

        out["failed"] = capo_securitylake.types.account_list.deserialize_json(
            data["failed"]
        )
    return out
