"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#BatchUpdateBillScenarioUsageModificationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bcm_pricing_calculator.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bcm_pricing_calculator.types.batch_update_bill_scenario_usage_modification_entries
    import aws_sdk_bcm_pricing_calculator.types.resource_id


class BatchUpdateBillScenarioUsageModificationRequest(TypedDict):
    bill_scenario_id: "aws_sdk_bcm_pricing_calculator.types.resource_id.ResourceId"
    """<p> The ID of the Bill Scenario for which you want to modify the usage lines. </p>"""
    usage_modifications: "aws_sdk_bcm_pricing_calculator.types.batch_update_bill_scenario_usage_modification_entries.BatchUpdateBillScenarioUsageModificationEntries"
    """<p> List of usage lines that you want to update in a Bill Scenario identified by the usage ID. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: BatchUpdateBillScenarioUsageModificationRequest,
) -> dict:
    out: dict = {}
    out["billScenarioId"] = value["bill_scenario_id"]
    import aws_sdk_bcm_pricing_calculator.types.batch_update_bill_scenario_usage_modification_entries

    out["usageModifications"] = (
        aws_sdk_bcm_pricing_calculator.types.batch_update_bill_scenario_usage_modification_entries.serialize_aws_json_1_0(
            value["usage_modifications"]
        )
    )
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> BatchUpdateBillScenarioUsageModificationRequest:
    out: BatchUpdateBillScenarioUsageModificationRequest = {}  # type: ignore[typeddict-item]
    if "billScenarioId" in data:
        out["bill_scenario_id"] = data["billScenarioId"]
    else:
        raise DeserializationError(
            "BatchUpdateBillScenarioUsageModificationRequest.bill_scenario_id required"
        )
    if "usageModifications" in data:
        import aws_sdk_bcm_pricing_calculator.types.batch_update_bill_scenario_usage_modification_entries

        out["usage_modifications"] = (
            aws_sdk_bcm_pricing_calculator.types.batch_update_bill_scenario_usage_modification_entries.deserialize_aws_json_1_0(
                data["usageModifications"]
            )
        )
    else:
        raise DeserializationError(
            "BatchUpdateBillScenarioUsageModificationRequest.usage_modifications required"
        )
    return out
