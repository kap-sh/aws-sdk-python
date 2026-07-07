"""Generated from Smithy shape ``com.amazonaws.taxsettings#PutTaxRegistrationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_taxsettings.types.tax_registration_status


class PutTaxRegistrationResponse(TypedDict, closed=True):
    status: NotRequired[
        "aws_sdk_taxsettings.types.tax_registration_status.TaxRegistrationStatus"
    ]
    """<p>The status of your TRN stored in the system after processing. Based on the validation occurring on the TRN, the status can be <code>Verified</code>, <code>Pending</code> or <code>Rejected</code>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutTaxRegistrationResponse) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_taxsettings.types.tax_registration_status

        out["status"] = (
            aws_sdk_taxsettings.types.tax_registration_status.serialize_json(
                value["status"]
            )
        )
    return out


def deserialize_json(data: dict) -> PutTaxRegistrationResponse:
    out: PutTaxRegistrationResponse = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import aws_sdk_taxsettings.types.tax_registration_status

        out["status"] = (
            aws_sdk_taxsettings.types.tax_registration_status.deserialize_json(
                data["status"]
            )
        )
    return out
