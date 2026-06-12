"""Generated from Smithy shape ``com.amazonaws.auditmanager#GetAccountStatusResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.account_status


class GetAccountStatusResponse(TypedDict):
    status: NotRequired["aws_sdk_auditmanager.types.account_status.AccountStatus"]
    """<p> The status of the Amazon Web Services account. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAccountStatusResponse) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_auditmanager.types.account_status

        out["status"] = aws_sdk_auditmanager.types.account_status.serialize_json(
            value["status"]
        )
    return out


def deserialize_json(data: dict) -> GetAccountStatusResponse:
    out: GetAccountStatusResponse = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import aws_sdk_auditmanager.types.account_status

        out["status"] = aws_sdk_auditmanager.types.account_status.deserialize_json(
            data["status"]
        )
    return out
