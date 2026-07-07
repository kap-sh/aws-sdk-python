"""Generated from Smithy shape ``com.amazonaws.detective#EnableOrganizationAdminAccountRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_detective.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_detective.types.account_id


class EnableOrganizationAdminAccountRequest(TypedDict, closed=True):
    account_id: "aws_sdk_detective.types.account_id.AccountId"
    """<p>The Amazon Web Services account identifier of the account to designate as the Detective administrator account for the organization.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnableOrganizationAdminAccountRequest) -> dict:
    out: dict = {}
    out["AccountId"] = value["account_id"]
    return out


def deserialize_json(data: dict) -> EnableOrganizationAdminAccountRequest:
    out: EnableOrganizationAdminAccountRequest = {}  # type: ignore[typeddict-item]
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    else:
        raise DeserializationError(
            "EnableOrganizationAdminAccountRequest.account_id required"
        )
    return out
