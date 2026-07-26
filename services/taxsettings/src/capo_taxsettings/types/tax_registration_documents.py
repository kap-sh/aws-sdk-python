"""Generated from Smithy shape ``com.amazonaws.taxsettings#TaxRegistrationDocuments``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_taxsettings.types.tax_registration_document

TaxRegistrationDocuments: TypeAlias = list[
    "capo_taxsettings.types.tax_registration_document.TaxRegistrationDocument"
]


# --- restJson1 ser/de ---
def serialize_json(value: TaxRegistrationDocuments) -> list:
    import capo_taxsettings.types.tax_registration_document

    out: list = []
    for item in value:
        out.append(
            capo_taxsettings.types.tax_registration_document.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> TaxRegistrationDocuments:
    import capo_taxsettings.types.tax_registration_document

    out: TaxRegistrationDocuments = []
    for item in data:
        out.append(
            capo_taxsettings.types.tax_registration_document.deserialize_json(item)
        )
    return out
