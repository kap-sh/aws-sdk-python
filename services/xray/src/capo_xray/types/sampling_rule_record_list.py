"""Generated from Smithy shape ``com.amazonaws.xray#SamplingRuleRecordList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_xray.types.sampling_rule_record

SamplingRuleRecordList: TypeAlias = list[
    "capo_xray.types.sampling_rule_record.SamplingRuleRecord"
]


# --- restJson1 ser/de ---
def serialize_json(value: SamplingRuleRecordList) -> list:
    import capo_xray.types.sampling_rule_record

    out: list = []
    for item in value:
        out.append(capo_xray.types.sampling_rule_record.serialize_json(item))
    return out


def deserialize_json(data: list) -> SamplingRuleRecordList:
    import capo_xray.types.sampling_rule_record

    out: SamplingRuleRecordList = []
    for item in data:
        out.append(capo_xray.types.sampling_rule_record.deserialize_json(item))
    return out
