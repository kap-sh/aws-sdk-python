"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#PrivacyBudgets``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_cleanroomsml.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.access_budgets


class _PrivacyBudgets_accessBudgets(TypedDict, closed=True):
    accessBudgets: "aws_sdk_cleanroomsml.types.access_budgets.AccessBudgets"


PrivacyBudgets: TypeAlias = _PrivacyBudgets_accessBudgets


# --- restJson1 ser/de ---
def serialize_json(value: PrivacyBudgets) -> dict:
    if "accessBudgets" in value:
        import aws_sdk_cleanroomsml.types.access_budgets

        return {
            "accessBudgets": aws_sdk_cleanroomsml.types.access_budgets.serialize_json(
                value["accessBudgets"]
            )
        }
    else:
        raise SerializationError("PrivacyBudgets: no variant present")


def deserialize_json(data: dict) -> PrivacyBudgets:
    if "accessBudgets" in data:
        import aws_sdk_cleanroomsml.types.access_budgets

        return {
            "accessBudgets": aws_sdk_cleanroomsml.types.access_budgets.deserialize_json(
                data["accessBudgets"]
            )
        }
    else:
        raise DeserializationError("PrivacyBudgets: no recognized variant key")
