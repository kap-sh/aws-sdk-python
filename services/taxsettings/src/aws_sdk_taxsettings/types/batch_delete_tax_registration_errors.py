"""Generated from Smithy shape ``com.amazonaws.taxsettings#BatchDeleteTaxRegistrationErrors``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_taxsettings.types.batch_delete_tax_registration_error

BatchDeleteTaxRegistrationErrors: TypeAlias = list["aws_sdk_taxsettings.types.batch_delete_tax_registration_error.BatchDeleteTaxRegistrationError"]


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteTaxRegistrationErrors) -> list:
    import aws_sdk_taxsettings.types.batch_delete_tax_registration_error
    out: list = []
    for item in value:
        out.append(aws_sdk_taxsettings.types.batch_delete_tax_registration_error.serialize_json(item))
    return out


def deserialize_json(data: list) -> BatchDeleteTaxRegistrationErrors:
    import aws_sdk_taxsettings.types.batch_delete_tax_registration_error
    out: BatchDeleteTaxRegistrationErrors = []
    for item in data:
        out.append(aws_sdk_taxsettings.types.batch_delete_tax_registration_error.deserialize_json(item))
    return out