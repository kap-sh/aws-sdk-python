"""Generated from Smithy shape ``com.amazonaws.taxsettings#BatchPutTaxRegistrationErrors``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_taxsettings.types.batch_put_tax_registration_error

BatchPutTaxRegistrationErrors: TypeAlias = list["aws_sdk_taxsettings.types.batch_put_tax_registration_error.BatchPutTaxRegistrationError"]


# --- restJson1 ser/de ---
def serialize_json(value: BatchPutTaxRegistrationErrors) -> list:
    import aws_sdk_taxsettings.types.batch_put_tax_registration_error
    out: list = []
    for item in value:
        out.append(aws_sdk_taxsettings.types.batch_put_tax_registration_error.serialize_json(item))
    return out


def deserialize_json(data: list) -> BatchPutTaxRegistrationErrors:
    import aws_sdk_taxsettings.types.batch_put_tax_registration_error
    out: BatchPutTaxRegistrationErrors = []
    for item in data:
        out.append(aws_sdk_taxsettings.types.batch_put_tax_registration_error.deserialize_json(item))
    return out