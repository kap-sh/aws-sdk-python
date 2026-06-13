"""Generated from Smithy shape ``com.amazonaws.cleanrooms#PrivacyBudget``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.access_budget
    import aws_sdk_cleanrooms.types.differential_privacy_privacy_budget


class _PrivacyBudget_differentialPrivacy(TypedDict):
    differentialPrivacy: "aws_sdk_cleanrooms.types.differential_privacy_privacy_budget.DifferentialPrivacyPrivacyBudget"


class _PrivacyBudget_accessBudget(TypedDict):
    accessBudget: "aws_sdk_cleanrooms.types.access_budget.AccessBudget"


PrivacyBudget: TypeAlias = (
    _PrivacyBudget_differentialPrivacy | _PrivacyBudget_accessBudget
)


# --- restJson1 ser/de ---
def serialize_json(value: PrivacyBudget) -> dict:
    if "differentialPrivacy" in value:
        import aws_sdk_cleanrooms.types.differential_privacy_privacy_budget

        return {
            "differentialPrivacy": aws_sdk_cleanrooms.types.differential_privacy_privacy_budget.serialize_json(
                value["differentialPrivacy"]
            )
        }
    elif "accessBudget" in value:
        import aws_sdk_cleanrooms.types.access_budget

        return {
            "accessBudget": aws_sdk_cleanrooms.types.access_budget.serialize_json(
                value["accessBudget"]
            )
        }
    else:
        raise SerializationError("PrivacyBudget: no variant present")


def deserialize_json(data: dict) -> PrivacyBudget:
    if "differentialPrivacy" in data:
        import aws_sdk_cleanrooms.types.differential_privacy_privacy_budget

        return {
            "differentialPrivacy": aws_sdk_cleanrooms.types.differential_privacy_privacy_budget.deserialize_json(
                data["differentialPrivacy"]
            )
        }
    elif "accessBudget" in data:
        import aws_sdk_cleanrooms.types.access_budget

        return {
            "accessBudget": aws_sdk_cleanrooms.types.access_budget.deserialize_json(
                data["accessBudget"]
            )
        }
    else:
        raise DeserializationError("PrivacyBudget: no recognized variant key")
