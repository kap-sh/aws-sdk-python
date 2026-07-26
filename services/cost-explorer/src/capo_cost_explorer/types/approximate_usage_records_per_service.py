"""Generated from Smithy shape ``com.amazonaws.costexplorer#ApproximateUsageRecordsPerService``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cost_explorer.types.generic_string
    import capo_cost_explorer.types.non_negative_long

ApproximateUsageRecordsPerService: TypeAlias = dict[
    "capo_cost_explorer.types.generic_string.GenericString",
    "capo_cost_explorer.types.non_negative_long.NonNegativeLong",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    input_to_serialize: ApproximateUsageRecordsPerService,
) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> ApproximateUsageRecordsPerService:
    out: ApproximateUsageRecordsPerService = {}
    for key, value in data.items():
        out[key] = value
    return out
