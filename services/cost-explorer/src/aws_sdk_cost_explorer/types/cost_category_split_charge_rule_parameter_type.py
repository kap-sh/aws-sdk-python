"""Generated from Smithy shape ``com.amazonaws.costexplorer#CostCategorySplitChargeRuleParameterType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cost_explorer.errors import DeserializationError

CostCategorySplitChargeRuleParameterType: TypeAlias = Literal["ALLOCATION_PERCENTAGES",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("ALLOCATION_PERCENTAGES",))


def serialize_aws_json_1_1(value: CostCategorySplitChargeRuleParameterType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CostCategorySplitChargeRuleParameterType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown CostCategorySplitChargeRuleParameterType value: {data!r}"
        )
    return cast(CostCategorySplitChargeRuleParameterType, data)
