"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#BillScenarioCommitmentModificationAction``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_bcm_pricing_calculator.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import aws_sdk_bcm_pricing_calculator.types.add_reserved_instance_action
    import aws_sdk_bcm_pricing_calculator.types.add_savings_plan_action
    import aws_sdk_bcm_pricing_calculator.types.negate_reserved_instance_action
    import aws_sdk_bcm_pricing_calculator.types.negate_savings_plan_action


class _BillScenarioCommitmentModificationAction_addReservedInstanceAction(
    TypedDict, closed=True
):
    addReservedInstanceAction: "aws_sdk_bcm_pricing_calculator.types.add_reserved_instance_action.AddReservedInstanceAction"


class _BillScenarioCommitmentModificationAction_addSavingsPlanAction(
    TypedDict, closed=True
):
    addSavingsPlanAction: "aws_sdk_bcm_pricing_calculator.types.add_savings_plan_action.AddSavingsPlanAction"


class _BillScenarioCommitmentModificationAction_negateReservedInstanceAction(
    TypedDict, closed=True
):
    negateReservedInstanceAction: "aws_sdk_bcm_pricing_calculator.types.negate_reserved_instance_action.NegateReservedInstanceAction"


class _BillScenarioCommitmentModificationAction_negateSavingsPlanAction(
    TypedDict, closed=True
):
    negateSavingsPlanAction: "aws_sdk_bcm_pricing_calculator.types.negate_savings_plan_action.NegateSavingsPlanAction"


BillScenarioCommitmentModificationAction: TypeAlias = (
    _BillScenarioCommitmentModificationAction_addReservedInstanceAction
    | _BillScenarioCommitmentModificationAction_addSavingsPlanAction
    | _BillScenarioCommitmentModificationAction_negateReservedInstanceAction
    | _BillScenarioCommitmentModificationAction_negateSavingsPlanAction
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BillScenarioCommitmentModificationAction) -> dict:
    if "addReservedInstanceAction" in value:
        import aws_sdk_bcm_pricing_calculator.types.add_reserved_instance_action

        return {
            "addReservedInstanceAction": aws_sdk_bcm_pricing_calculator.types.add_reserved_instance_action.serialize_aws_json_1_0(
                value["addReservedInstanceAction"]
            )
        }
    elif "addSavingsPlanAction" in value:
        import aws_sdk_bcm_pricing_calculator.types.add_savings_plan_action

        return {
            "addSavingsPlanAction": aws_sdk_bcm_pricing_calculator.types.add_savings_plan_action.serialize_aws_json_1_0(
                value["addSavingsPlanAction"]
            )
        }
    elif "negateReservedInstanceAction" in value:
        import aws_sdk_bcm_pricing_calculator.types.negate_reserved_instance_action

        return {
            "negateReservedInstanceAction": aws_sdk_bcm_pricing_calculator.types.negate_reserved_instance_action.serialize_aws_json_1_0(
                value["negateReservedInstanceAction"]
            )
        }
    elif "negateSavingsPlanAction" in value:
        import aws_sdk_bcm_pricing_calculator.types.negate_savings_plan_action

        return {
            "negateSavingsPlanAction": aws_sdk_bcm_pricing_calculator.types.negate_savings_plan_action.serialize_aws_json_1_0(
                value["negateSavingsPlanAction"]
            )
        }
    else:
        raise SerializationError(
            "BillScenarioCommitmentModificationAction: no variant present"
        )


def deserialize_aws_json_1_0(data: dict) -> BillScenarioCommitmentModificationAction:
    if "addReservedInstanceAction" in data:
        import aws_sdk_bcm_pricing_calculator.types.add_reserved_instance_action

        return {
            "addReservedInstanceAction": aws_sdk_bcm_pricing_calculator.types.add_reserved_instance_action.deserialize_aws_json_1_0(
                data["addReservedInstanceAction"]
            )
        }
    elif "addSavingsPlanAction" in data:
        import aws_sdk_bcm_pricing_calculator.types.add_savings_plan_action

        return {
            "addSavingsPlanAction": aws_sdk_bcm_pricing_calculator.types.add_savings_plan_action.deserialize_aws_json_1_0(
                data["addSavingsPlanAction"]
            )
        }
    elif "negateReservedInstanceAction" in data:
        import aws_sdk_bcm_pricing_calculator.types.negate_reserved_instance_action

        return {
            "negateReservedInstanceAction": aws_sdk_bcm_pricing_calculator.types.negate_reserved_instance_action.deserialize_aws_json_1_0(
                data["negateReservedInstanceAction"]
            )
        }
    elif "negateSavingsPlanAction" in data:
        import aws_sdk_bcm_pricing_calculator.types.negate_savings_plan_action

        return {
            "negateSavingsPlanAction": aws_sdk_bcm_pricing_calculator.types.negate_savings_plan_action.deserialize_aws_json_1_0(
                data["negateSavingsPlanAction"]
            )
        }
    else:
        raise DeserializationError(
            "BillScenarioCommitmentModificationAction: no recognized variant key"
        )
