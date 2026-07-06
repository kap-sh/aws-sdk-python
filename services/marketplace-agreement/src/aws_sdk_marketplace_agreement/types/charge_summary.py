"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#ChargeSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_marketplace_agreement.types.bounded_string
    import aws_sdk_marketplace_agreement.types.currency_code
    import aws_sdk_marketplace_agreement.types.estimated_taxes
    import aws_sdk_marketplace_agreement.types.expected_charge_list
    import aws_sdk_marketplace_agreement.types.invoicing_entity
    import aws_sdk_marketplace_agreement.types.itemized_charge_list


class ChargeSummary(TypedDict, closed=True):
    currency_code: NotRequired[
        "aws_sdk_marketplace_agreement.types.currency_code.CurrencyCode"
    ]
    """<p>The three-letter currency code for all charges (e.g., USD).</p>"""
    new_agreement_value: NotRequired[
        "aws_sdk_marketplace_agreement.types.bounded_string.BoundedString"
    ]
    """<p>The total value of the agreement, which includes any amendments.</p>"""
    new_agreement_value_after_tax: NotRequired[
        "aws_sdk_marketplace_agreement.types.bounded_string.BoundedString"
    ]
    """<p>Expected new agreement value after estimated taxes are applied.</p>"""
    expected_charges: NotRequired[
        "aws_sdk_marketplace_agreement.types.expected_charge_list.ExpectedChargeList"
    ]
    """<p>A list of expected charges for the agreement request.</p>"""
    estimated_taxes: NotRequired[
        "aws_sdk_marketplace_agreement.types.estimated_taxes.EstimatedTaxes"
    ]
    """<p>Provides an aggregated view of estimated tax information for the agreement.</p>"""
    itemized_charges: NotRequired[
        "aws_sdk_marketplace_agreement.types.itemized_charge_list.ItemizedChargeList"
    ]
    """<p>An itemized list of charges for the agreement request.</p>"""
    invoicing_entity: NotRequired[
        "aws_sdk_marketplace_agreement.types.invoicing_entity.InvoicingEntity"
    ]
    """<p>The entity responsible for issuing the invoice.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ChargeSummary) -> dict:
    out: dict = {}
    if "currency_code" in value:
        out["currencyCode"] = value["currency_code"]
    if "new_agreement_value" in value:
        out["newAgreementValue"] = value["new_agreement_value"]
    if "new_agreement_value_after_tax" in value:
        out["newAgreementValueAfterTax"] = value["new_agreement_value_after_tax"]
    if "expected_charges" in value:
        import aws_sdk_marketplace_agreement.types.expected_charge_list

        out["expectedCharges"] = (
            aws_sdk_marketplace_agreement.types.expected_charge_list.serialize_aws_json_1_0(
                value["expected_charges"]
            )
        )
    if "estimated_taxes" in value:
        import aws_sdk_marketplace_agreement.types.estimated_taxes

        out["estimatedTaxes"] = (
            aws_sdk_marketplace_agreement.types.estimated_taxes.serialize_aws_json_1_0(
                value["estimated_taxes"]
            )
        )
    if "itemized_charges" in value:
        import aws_sdk_marketplace_agreement.types.itemized_charge_list

        out["itemizedCharges"] = (
            aws_sdk_marketplace_agreement.types.itemized_charge_list.serialize_aws_json_1_0(
                value["itemized_charges"]
            )
        )
    if "invoicing_entity" in value:
        import aws_sdk_marketplace_agreement.types.invoicing_entity

        out["invoicingEntity"] = (
            aws_sdk_marketplace_agreement.types.invoicing_entity.serialize_aws_json_1_0(
                value["invoicing_entity"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ChargeSummary:
    out: ChargeSummary = {}  # type: ignore[typeddict-item]
    if "currencyCode" in data:
        out["currency_code"] = data["currencyCode"]
    if "newAgreementValue" in data:
        out["new_agreement_value"] = data["newAgreementValue"]
    if "newAgreementValueAfterTax" in data:
        out["new_agreement_value_after_tax"] = data["newAgreementValueAfterTax"]
    if "expectedCharges" in data:
        import aws_sdk_marketplace_agreement.types.expected_charge_list

        out["expected_charges"] = (
            aws_sdk_marketplace_agreement.types.expected_charge_list.deserialize_aws_json_1_0(
                data["expectedCharges"]
            )
        )
    if "estimatedTaxes" in data:
        import aws_sdk_marketplace_agreement.types.estimated_taxes

        out["estimated_taxes"] = (
            aws_sdk_marketplace_agreement.types.estimated_taxes.deserialize_aws_json_1_0(
                data["estimatedTaxes"]
            )
        )
    if "itemizedCharges" in data:
        import aws_sdk_marketplace_agreement.types.itemized_charge_list

        out["itemized_charges"] = (
            aws_sdk_marketplace_agreement.types.itemized_charge_list.deserialize_aws_json_1_0(
                data["itemizedCharges"]
            )
        )
    if "invoicingEntity" in data:
        import aws_sdk_marketplace_agreement.types.invoicing_entity

        out["invoicing_entity"] = (
            aws_sdk_marketplace_agreement.types.invoicing_entity.deserialize_aws_json_1_0(
                data["invoicingEntity"]
            )
        )
    return out
