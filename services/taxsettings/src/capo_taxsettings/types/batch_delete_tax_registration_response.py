"""Generated from Smithy shape ``com.amazonaws.taxsettings#BatchDeleteTaxRegistrationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_taxsettings.errors import DeserializationError

if TYPE_CHECKING:
    import capo_taxsettings.types.batch_delete_tax_registration_errors


class BatchDeleteTaxRegistrationResponse(TypedDict, closed=True):
    errors: "capo_taxsettings.types.batch_delete_tax_registration_errors.BatchDeleteTaxRegistrationErrors"
    """<p>The list of errors for the accounts the TRN information could not be deleted for. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteTaxRegistrationResponse) -> dict:
    out: dict = {}
    import capo_taxsettings.types.batch_delete_tax_registration_errors

    out["errors"] = (
        capo_taxsettings.types.batch_delete_tax_registration_errors.serialize_json(
            value["errors"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchDeleteTaxRegistrationResponse:
    out: BatchDeleteTaxRegistrationResponse = {}  # type: ignore[typeddict-item]
    if "errors" in data:
        import capo_taxsettings.types.batch_delete_tax_registration_errors

        out["errors"] = (
            capo_taxsettings.types.batch_delete_tax_registration_errors.deserialize_json(
                data["errors"]
            )
        )
    else:
        raise DeserializationError("BatchDeleteTaxRegistrationResponse.errors required")
    return out
