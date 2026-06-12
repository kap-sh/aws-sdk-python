"""Generated from Smithy shape ``com.amazonaws.taxsettings#ListSupplementalTaxRegistrationsResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_taxsettings.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_taxsettings.types.pagination_token_string
    import aws_sdk_taxsettings.types.supplemental_tax_registration_list

class ListSupplementalTaxRegistrationsResponse(TypedDict):
    tax_registrations: "aws_sdk_taxsettings.types.supplemental_tax_registration_list.SupplementalTaxRegistrationList"
    """<p> The list of supplemental tax registrations. </p>"""
    next_token: NotRequired["aws_sdk_taxsettings.types.pagination_token_string.PaginationTokenString"]
    """<p> The token to retrieve the next set of results. </p>"""

# --- restJson1 ser/de ---
def serialize_json(value: ListSupplementalTaxRegistrationsResponse) -> dict:
    out: dict = {}
    import aws_sdk_taxsettings.types.supplemental_tax_registration_list
    out["taxRegistrations"] = aws_sdk_taxsettings.types.supplemental_tax_registration_list.serialize_json(value["tax_registrations"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSupplementalTaxRegistrationsResponse:
    out: ListSupplementalTaxRegistrationsResponse = {}  # type: ignore[typeddict-item]
    if "taxRegistrations" in data:
        import aws_sdk_taxsettings.types.supplemental_tax_registration_list
        out["tax_registrations"] = aws_sdk_taxsettings.types.supplemental_tax_registration_list.deserialize_json(data["taxRegistrations"])
    else:
        raise DeserializationError("ListSupplementalTaxRegistrationsResponse.tax_registrations required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out