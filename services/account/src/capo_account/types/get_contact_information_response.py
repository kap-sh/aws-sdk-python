"""Generated from Smithy shape ``com.amazonaws.account#GetContactInformationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_account.types.contact_information


class GetContactInformationResponse(TypedDict, closed=True):
    contact_information: NotRequired[
        "capo_account.types.contact_information.ContactInformation"
    ]
    """<p>Contains the details of the primary contact information associated with an Amazon Web Services account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetContactInformationResponse) -> dict:
    out: dict = {}
    if "contact_information" in value:
        import capo_account.types.contact_information

        out["ContactInformation"] = (
            capo_account.types.contact_information.serialize_json(
                value["contact_information"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetContactInformationResponse:
    out: GetContactInformationResponse = {}  # type: ignore[typeddict-item]
    if "ContactInformation" in data:
        import capo_account.types.contact_information

        out["contact_information"] = (
            capo_account.types.contact_information.deserialize_json(
                data["ContactInformation"]
            )
        )
    return out
