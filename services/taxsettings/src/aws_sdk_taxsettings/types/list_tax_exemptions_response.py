"""Generated from Smithy shape ``com.amazonaws.taxsettings#ListTaxExemptionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_taxsettings.types.pagination_token_string
    import aws_sdk_taxsettings.types.tax_exemption_details_map


class ListTaxExemptionsResponse(TypedDict, closed=True):
    next_token: NotRequired[
        "aws_sdk_taxsettings.types.pagination_token_string.PaginationTokenString"
    ]
    """<p>The token to retrieve the next set of results. </p>"""
    tax_exemption_details_map: NotRequired[
        "aws_sdk_taxsettings.types.tax_exemption_details_map.TaxExemptionDetailsMap"
    ]
    """<p>The tax exemption details map of <code>accountId</code> and tax exemption details. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTaxExemptionsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "tax_exemption_details_map" in value:
        import aws_sdk_taxsettings.types.tax_exemption_details_map

        out["taxExemptionDetailsMap"] = (
            aws_sdk_taxsettings.types.tax_exemption_details_map.serialize_json(
                value["tax_exemption_details_map"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListTaxExemptionsResponse:
    out: ListTaxExemptionsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "taxExemptionDetailsMap" in data:
        import aws_sdk_taxsettings.types.tax_exemption_details_map

        out["tax_exemption_details_map"] = (
            aws_sdk_taxsettings.types.tax_exemption_details_map.deserialize_json(
                data["taxExemptionDetailsMap"]
            )
        )
    return out
