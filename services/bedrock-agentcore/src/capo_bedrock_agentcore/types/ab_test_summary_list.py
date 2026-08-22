"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ABTestSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.ab_test_summary

ABTestSummaryList: TypeAlias = list[
    "capo_bedrock_agentcore.types.ab_test_summary.ABTestSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ABTestSummaryList) -> list:
    import capo_bedrock_agentcore.types.ab_test_summary

    out: list = []
    for item in value:
        out.append(capo_bedrock_agentcore.types.ab_test_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ABTestSummaryList:
    import capo_bedrock_agentcore.types.ab_test_summary

    out: ABTestSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_bedrock_agentcore.types.ab_test_summary.deserialize_json(item))
    return out
