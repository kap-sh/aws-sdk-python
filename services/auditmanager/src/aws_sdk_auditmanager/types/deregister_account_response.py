"""Generated from Smithy shape ``com.amazonaws.auditmanager#DeregisterAccountResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.account_status


class DeregisterAccountResponse(TypedDict, closed=True):
    status: NotRequired["aws_sdk_auditmanager.types.account_status.AccountStatus"]
    """<p> The registration status of the account. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeregisterAccountResponse) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_auditmanager.types.account_status

        out["status"] = aws_sdk_auditmanager.types.account_status.serialize_json(
            value["status"]
        )
    return out


def deserialize_json(data: dict) -> DeregisterAccountResponse:
    out: DeregisterAccountResponse = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import aws_sdk_auditmanager.types.account_status

        out["status"] = aws_sdk_auditmanager.types.account_status.deserialize_json(
            data["status"]
        )
    return out
