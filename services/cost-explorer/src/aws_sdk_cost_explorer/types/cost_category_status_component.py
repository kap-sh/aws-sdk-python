"""Generated from Smithy shape ``com.amazonaws.costexplorer#CostCategoryStatusComponent``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cost_explorer.errors import DeserializationError

CostCategoryStatusComponent: TypeAlias = Literal["COST_EXPLORER",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("COST_EXPLORER",))


def serialize_aws_json_1_1(value: CostCategoryStatusComponent) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CostCategoryStatusComponent:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown CostCategoryStatusComponent value: {data!r}"
        )
    return cast(CostCategoryStatusComponent, data)
