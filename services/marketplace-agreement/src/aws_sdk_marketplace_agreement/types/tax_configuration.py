"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#TaxConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_marketplace_agreement.types.tax_estimation


class TaxConfiguration(TypedDict, closed=True):
    tax_estimation: "aws_sdk_marketplace_agreement.types.tax_estimation.TaxEstimation"
    """<p>Toggle to estimate tax as part of the response. Values include <code>ENABLED</code> and <code>DISABLED</code>. Default is <code>DISABLED</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TaxConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_marketplace_agreement.types.tax_estimation

    out["taxEstimation"] = (
        aws_sdk_marketplace_agreement.types.tax_estimation.serialize_aws_json_1_0(
            value.get("tax_estimation", "DISABLED")
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> TaxConfiguration:
    out: TaxConfiguration = {}  # type: ignore[typeddict-item]
    if "taxEstimation" in data:
        import aws_sdk_marketplace_agreement.types.tax_estimation

        out["tax_estimation"] = (
            aws_sdk_marketplace_agreement.types.tax_estimation.deserialize_aws_json_1_0(
                data["taxEstimation"]
            )
        )
    else:
        out["tax_estimation"] = "DISABLED"
    return out
