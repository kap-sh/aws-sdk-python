"""Generated from Smithy shape ``com.amazonaws.taxsettings#PutSupplementalTaxRegistrationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_taxsettings.errors import DeserializationError

if TYPE_CHECKING:
    import capo_taxsettings.types.generic_string
    import capo_taxsettings.types.tax_registration_status


class PutSupplementalTaxRegistrationResponse(TypedDict, closed=True):
    authority_id: "capo_taxsettings.types.generic_string.GenericString"
    """<p> Unique authority ID for the supplemental TRN information that was stored. </p>"""
    status: "capo_taxsettings.types.tax_registration_status.TaxRegistrationStatus"
    """<p> The status of the supplemental TRN stored in the system after processing. Based on the validation occurring on the TRN, the status can be <code>Verified</code>, <code>Pending</code>, <code>Rejected</code>, or <code>Deleted</code>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutSupplementalTaxRegistrationResponse) -> dict:
    out: dict = {}
    out["authorityId"] = value["authority_id"]
    import capo_taxsettings.types.tax_registration_status

    out["status"] = capo_taxsettings.types.tax_registration_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> PutSupplementalTaxRegistrationResponse:
    out: PutSupplementalTaxRegistrationResponse = {}  # type: ignore[typeddict-item]
    if "authorityId" in data:
        out["authority_id"] = data["authorityId"]
    else:
        raise DeserializationError(
            "PutSupplementalTaxRegistrationResponse.authority_id required"
        )
    if "status" in data:
        import capo_taxsettings.types.tax_registration_status

        out["status"] = capo_taxsettings.types.tax_registration_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError(
            "PutSupplementalTaxRegistrationResponse.status required"
        )
    return out
