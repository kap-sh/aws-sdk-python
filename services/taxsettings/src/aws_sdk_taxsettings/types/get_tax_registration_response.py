"""Generated from Smithy shape ``com.amazonaws.taxsettings#GetTaxRegistrationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_taxsettings.types.tax_registration


class GetTaxRegistrationResponse(TypedDict, closed=True):
    tax_registration: NotRequired[
        "aws_sdk_taxsettings.types.tax_registration.TaxRegistration"
    ]
    """<p>TRN information of the account mentioned in the request. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTaxRegistrationResponse) -> dict:
    out: dict = {}
    if "tax_registration" in value:
        import aws_sdk_taxsettings.types.tax_registration

        out["taxRegistration"] = (
            aws_sdk_taxsettings.types.tax_registration.serialize_json(
                value["tax_registration"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetTaxRegistrationResponse:
    out: GetTaxRegistrationResponse = {}  # type: ignore[typeddict-item]
    if "taxRegistration" in data:
        import aws_sdk_taxsettings.types.tax_registration

        out["tax_registration"] = (
            aws_sdk_taxsettings.types.tax_registration.deserialize_json(
                data["taxRegistration"]
            )
        )
    return out
