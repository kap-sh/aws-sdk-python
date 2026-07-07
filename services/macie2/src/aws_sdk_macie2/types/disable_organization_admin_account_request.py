"""Generated from Smithy shape ``com.amazonaws.macie2#DisableOrganizationAdminAccountRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__string


class DisableOrganizationAdminAccountRequest(TypedDict, closed=True):
    admin_account_id: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The Amazon Web Services account ID of the delegated Amazon Macie administrator account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisableOrganizationAdminAccountRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DisableOrganizationAdminAccountRequest:
    out: DisableOrganizationAdminAccountRequest = {}  # type: ignore[typeddict-item]
    return out
