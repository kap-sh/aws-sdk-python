"""Generated from Smithy shape ``com.amazonaws.account#GetPrimaryEmailResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_account.types.primary_email_address


class GetPrimaryEmailResponse(TypedDict):
    primary_email: NotRequired[
        "aws_sdk_account.types.primary_email_address.PrimaryEmailAddress"
    ]
    """<p>Retrieves the primary email address associated with the specified account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPrimaryEmailResponse) -> dict:
    out: dict = {}
    if "primary_email" in value:
        out["PrimaryEmail"] = value["primary_email"]
    return out


def deserialize_json(data: dict) -> GetPrimaryEmailResponse:
    out: GetPrimaryEmailResponse = {}  # type: ignore[typeddict-item]
    if "PrimaryEmail" in data:
        out["primary_email"] = data["PrimaryEmail"]
    return out
