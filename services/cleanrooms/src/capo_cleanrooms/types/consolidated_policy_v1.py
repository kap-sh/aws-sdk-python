"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ConsolidatedPolicyV1``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_cleanrooms.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_cleanrooms.types.consolidated_policy_aggregation
    import capo_cleanrooms.types.consolidated_policy_custom
    import capo_cleanrooms.types.consolidated_policy_list


class _ConsolidatedPolicyV1_list(TypedDict, closed=True):
    list: "capo_cleanrooms.types.consolidated_policy_list.ConsolidatedPolicyList"


class _ConsolidatedPolicyV1_aggregation(TypedDict, closed=True):
    aggregation: "capo_cleanrooms.types.consolidated_policy_aggregation.ConsolidatedPolicyAggregation"


class _ConsolidatedPolicyV1_custom(TypedDict, closed=True):
    custom: "capo_cleanrooms.types.consolidated_policy_custom.ConsolidatedPolicyCustom"


ConsolidatedPolicyV1: TypeAlias = (
    _ConsolidatedPolicyV1_list
    | _ConsolidatedPolicyV1_aggregation
    | _ConsolidatedPolicyV1_custom
)


# --- restJson1 ser/de ---
def serialize_json(value: ConsolidatedPolicyV1) -> dict:
    if "list" in value:
        import capo_cleanrooms.types.consolidated_policy_list

        return {
            "list": capo_cleanrooms.types.consolidated_policy_list.serialize_json(
                value["list"]
            )
        }
    elif "aggregation" in value:
        import capo_cleanrooms.types.consolidated_policy_aggregation

        return {
            "aggregation": capo_cleanrooms.types.consolidated_policy_aggregation.serialize_json(
                value["aggregation"]
            )
        }
    elif "custom" in value:
        import capo_cleanrooms.types.consolidated_policy_custom

        return {
            "custom": capo_cleanrooms.types.consolidated_policy_custom.serialize_json(
                value["custom"]
            )
        }
    else:
        raise SerializationError("ConsolidatedPolicyV1: no variant present")


def deserialize_json(data: dict) -> ConsolidatedPolicyV1:
    if "list" in data:
        import capo_cleanrooms.types.consolidated_policy_list

        return {
            "list": capo_cleanrooms.types.consolidated_policy_list.deserialize_json(
                data["list"]
            )
        }
    elif "aggregation" in data:
        import capo_cleanrooms.types.consolidated_policy_aggregation

        return {
            "aggregation": capo_cleanrooms.types.consolidated_policy_aggregation.deserialize_json(
                data["aggregation"]
            )
        }
    elif "custom" in data:
        import capo_cleanrooms.types.consolidated_policy_custom

        return {
            "custom": capo_cleanrooms.types.consolidated_policy_custom.deserialize_json(
                data["custom"]
            )
        }
    else:
        raise DeserializationError("ConsolidatedPolicyV1: no recognized variant key")
