"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#BatchCreateBillScenarioUsageModificationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bcm_pricing_calculator.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bcm_pricing_calculator.types.batch_create_bill_scenario_usage_modification_entries
    import capo_bcm_pricing_calculator.types.client_token
    import capo_bcm_pricing_calculator.types.resource_id


class BatchCreateBillScenarioUsageModificationRequest(TypedDict, closed=True):
    bill_scenario_id: "capo_bcm_pricing_calculator.types.resource_id.ResourceId"
    """<p> The ID of the Bill Scenario for which you want to create the modeled usage. </p>"""
    usage_modifications: "capo_bcm_pricing_calculator.types.batch_create_bill_scenario_usage_modification_entries.BatchCreateBillScenarioUsageModificationEntries"
    """<p> List of usage that you want to model in the Bill Scenario. </p>"""
    client_token: NotRequired[
        "capo_bcm_pricing_calculator.types.client_token.ClientToken"
    ]
    """<p> A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: BatchCreateBillScenarioUsageModificationRequest,
) -> dict:
    out: dict = {}
    out["billScenarioId"] = value["bill_scenario_id"]
    import capo_bcm_pricing_calculator.types.batch_create_bill_scenario_usage_modification_entries

    out["usageModifications"] = (
        capo_bcm_pricing_calculator.types.batch_create_bill_scenario_usage_modification_entries.serialize_aws_json_1_0(
            value["usage_modifications"]
        )
    )
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> BatchCreateBillScenarioUsageModificationRequest:
    out: BatchCreateBillScenarioUsageModificationRequest = {}  # type: ignore[typeddict-item]
    if "billScenarioId" in data:
        out["bill_scenario_id"] = data["billScenarioId"]
    else:
        raise DeserializationError(
            "BatchCreateBillScenarioUsageModificationRequest.bill_scenario_id required"
        )
    if "usageModifications" in data:
        import capo_bcm_pricing_calculator.types.batch_create_bill_scenario_usage_modification_entries

        out["usage_modifications"] = (
            capo_bcm_pricing_calculator.types.batch_create_bill_scenario_usage_modification_entries.deserialize_aws_json_1_0(
                data["usageModifications"]
            )
        )
    else:
        raise DeserializationError(
            "BatchCreateBillScenarioUsageModificationRequest.usage_modifications required"
        )
    return out
