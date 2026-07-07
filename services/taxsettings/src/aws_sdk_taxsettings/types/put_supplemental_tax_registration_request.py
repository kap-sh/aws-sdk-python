"""Generated from Smithy shape ``com.amazonaws.taxsettings#PutSupplementalTaxRegistrationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_taxsettings.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_taxsettings.types.supplemental_tax_registration_entry


class PutSupplementalTaxRegistrationRequest(TypedDict, closed=True):
    tax_registration_entry: "aws_sdk_taxsettings.types.supplemental_tax_registration_entry.SupplementalTaxRegistrationEntry"
    """<p> The supplemental TRN information that will be stored for the caller account ID. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutSupplementalTaxRegistrationRequest) -> dict:
    out: dict = {}
    import aws_sdk_taxsettings.types.supplemental_tax_registration_entry

    out["taxRegistrationEntry"] = (
        aws_sdk_taxsettings.types.supplemental_tax_registration_entry.serialize_json(
            value["tax_registration_entry"]
        )
    )
    return out


def deserialize_json(data: dict) -> PutSupplementalTaxRegistrationRequest:
    out: PutSupplementalTaxRegistrationRequest = {}  # type: ignore[typeddict-item]
    if "taxRegistrationEntry" in data:
        import aws_sdk_taxsettings.types.supplemental_tax_registration_entry

        out["tax_registration_entry"] = (
            aws_sdk_taxsettings.types.supplemental_tax_registration_entry.deserialize_json(
                data["taxRegistrationEntry"]
            )
        )
    else:
        raise DeserializationError(
            "PutSupplementalTaxRegistrationRequest.tax_registration_entry required"
        )
    return out
