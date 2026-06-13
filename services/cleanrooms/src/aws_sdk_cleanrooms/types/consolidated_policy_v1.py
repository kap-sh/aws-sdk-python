"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ConsolidatedPolicyV1``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.consolidated_policy_aggregation
    import aws_sdk_cleanrooms.types.consolidated_policy_custom
    import aws_sdk_cleanrooms.types.consolidated_policy_list


class _ConsolidatedPolicyV1_list(TypedDict):
    list: "aws_sdk_cleanrooms.types.consolidated_policy_list.ConsolidatedPolicyList"


class _ConsolidatedPolicyV1_aggregation(TypedDict):
    aggregation: "aws_sdk_cleanrooms.types.consolidated_policy_aggregation.ConsolidatedPolicyAggregation"


class _ConsolidatedPolicyV1_custom(TypedDict):
    custom: (
        "aws_sdk_cleanrooms.types.consolidated_policy_custom.ConsolidatedPolicyCustom"
    )


ConsolidatedPolicyV1: TypeAlias = (
    _ConsolidatedPolicyV1_list
    | _ConsolidatedPolicyV1_aggregation
    | _ConsolidatedPolicyV1_custom
)


# --- restJson1 ser/de ---
def serialize_json(value: ConsolidatedPolicyV1) -> dict:
    if "list" in value:
        import aws_sdk_cleanrooms.types.consolidated_policy_list

        return {
            "list": aws_sdk_cleanrooms.types.consolidated_policy_list.serialize_json(
                value["list"]
            )
        }
    elif "aggregation" in value:
        import aws_sdk_cleanrooms.types.consolidated_policy_aggregation

        return {
            "aggregation": aws_sdk_cleanrooms.types.consolidated_policy_aggregation.serialize_json(
                value["aggregation"]
            )
        }
    elif "custom" in value:
        import aws_sdk_cleanrooms.types.consolidated_policy_custom

        return {
            "custom": aws_sdk_cleanrooms.types.consolidated_policy_custom.serialize_json(
                value["custom"]
            )
        }
    else:
        raise SerializationError("ConsolidatedPolicyV1: no variant present")


def deserialize_json(data: dict) -> ConsolidatedPolicyV1:
    if "list" in data:
        import aws_sdk_cleanrooms.types.consolidated_policy_list

        return {
            "list": aws_sdk_cleanrooms.types.consolidated_policy_list.deserialize_json(
                data["list"]
            )
        }
    elif "aggregation" in data:
        import aws_sdk_cleanrooms.types.consolidated_policy_aggregation

        return {
            "aggregation": aws_sdk_cleanrooms.types.consolidated_policy_aggregation.deserialize_json(
                data["aggregation"]
            )
        }
    elif "custom" in data:
        import aws_sdk_cleanrooms.types.consolidated_policy_custom

        return {
            "custom": aws_sdk_cleanrooms.types.consolidated_policy_custom.deserialize_json(
                data["custom"]
            )
        }
    else:
        raise DeserializationError("ConsolidatedPolicyV1: no recognized variant key")
