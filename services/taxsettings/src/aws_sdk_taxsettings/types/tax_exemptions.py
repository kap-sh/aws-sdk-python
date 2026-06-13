"""Generated from Smithy shape ``com.amazonaws.taxsettings#TaxExemptions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_taxsettings.types.tax_exemption

TaxExemptions: TypeAlias = list["aws_sdk_taxsettings.types.tax_exemption.TaxExemption"]


# --- restJson1 ser/de ---
def serialize_json(value: TaxExemptions) -> list:
    import aws_sdk_taxsettings.types.tax_exemption

    out: list = []
    for item in value:
        out.append(aws_sdk_taxsettings.types.tax_exemption.serialize_json(item))
    return out


def deserialize_json(data: list) -> TaxExemptions:
    import aws_sdk_taxsettings.types.tax_exemption

    out: TaxExemptions = []
    for item in data:
        out.append(aws_sdk_taxsettings.types.tax_exemption.deserialize_json(item))
    return out
