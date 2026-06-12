"""Generated from Smithy shape ``com.amazonaws.deadline#BudgetSchedule``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_deadline.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.fixed_budget_schedule


class _BudgetSchedule_fixed(TypedDict):
    fixed: "aws_sdk_deadline.types.fixed_budget_schedule.FixedBudgetSchedule"


BudgetSchedule: TypeAlias = _BudgetSchedule_fixed


# --- restJson1 ser/de ---
def serialize_json(value: BudgetSchedule) -> dict:
    if "fixed" in value:
        import aws_sdk_deadline.types.fixed_budget_schedule

        return {
            "fixed": aws_sdk_deadline.types.fixed_budget_schedule.serialize_json(
                value["fixed"]
            )
        }
    else:
        raise SerializationError("BudgetSchedule: no variant present")


def deserialize_json(data: dict) -> BudgetSchedule:
    if "fixed" in data:
        import aws_sdk_deadline.types.fixed_budget_schedule

        return {
            "fixed": aws_sdk_deadline.types.fixed_budget_schedule.deserialize_json(
                data["fixed"]
            )
        }
    else:
        raise DeserializationError("BudgetSchedule: no recognized variant key")
