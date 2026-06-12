"""Generated from Smithy shape ``com.amazonaws.account#GetContactInformationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_account.types.contact_information


class GetContactInformationResponse(TypedDict):
    contact_information: NotRequired[
        "aws_sdk_account.types.contact_information.ContactInformation"
    ]
    """<p>Contains the details of the primary contact information associated with an Amazon Web Services account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetContactInformationResponse) -> dict:
    out: dict = {}
    if "contact_information" in value:
        import aws_sdk_account.types.contact_information

        out["ContactInformation"] = (
            aws_sdk_account.types.contact_information.serialize_json(
                value["contact_information"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetContactInformationResponse:
    out: GetContactInformationResponse = {}  # type: ignore[typeddict-item]
    if "ContactInformation" in data:
        import aws_sdk_account.types.contact_information

        out["contact_information"] = (
            aws_sdk_account.types.contact_information.deserialize_json(
                data["ContactInformation"]
            )
        )
    return out
