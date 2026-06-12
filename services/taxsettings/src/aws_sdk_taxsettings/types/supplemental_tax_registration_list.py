"""Generated from Smithy shape ``com.amazonaws.taxsettings#SupplementalTaxRegistrationList``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_taxsettings.types.supplemental_tax_registration

SupplementalTaxRegistrationList: TypeAlias = list["aws_sdk_taxsettings.types.supplemental_tax_registration.SupplementalTaxRegistration"]


# --- restJson1 ser/de ---
def serialize_json(value: SupplementalTaxRegistrationList) -> list:
    import aws_sdk_taxsettings.types.supplemental_tax_registration
    out: list = []
    for item in value:
        out.append(aws_sdk_taxsettings.types.supplemental_tax_registration.serialize_json(item))
    return out


def deserialize_json(data: list) -> SupplementalTaxRegistrationList:
    import aws_sdk_taxsettings.types.supplemental_tax_registration
    out: SupplementalTaxRegistrationList = []
    for item in data:
        out.append(aws_sdk_taxsettings.types.supplemental_tax_registration.deserialize_json(item))
    return out