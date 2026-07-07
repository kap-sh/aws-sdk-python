"""Generated from Smithy shape ``com.amazonaws.xray#GetSamplingRulesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_xray.types.sampling_rule_record_list
    import aws_sdk_xray.types.string


class GetSamplingRulesResult(TypedDict, closed=True):
    sampling_rule_records: NotRequired[
        "aws_sdk_xray.types.sampling_rule_record_list.SamplingRuleRecordList"
    ]
    """<p>Rule definitions and metadata.</p>"""
    next_token: NotRequired["aws_sdk_xray.types.string.String"]
    """<p>Pagination token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSamplingRulesResult) -> dict:
    out: dict = {}
    if "sampling_rule_records" in value:
        import aws_sdk_xray.types.sampling_rule_record_list

        out["SamplingRuleRecords"] = (
            aws_sdk_xray.types.sampling_rule_record_list.serialize_json(
                value["sampling_rule_records"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetSamplingRulesResult:
    out: GetSamplingRulesResult = {}  # type: ignore[typeddict-item]
    if "SamplingRuleRecords" in data:
        import aws_sdk_xray.types.sampling_rule_record_list

        out["sampling_rule_records"] = (
            aws_sdk_xray.types.sampling_rule_record_list.deserialize_json(
                data["SamplingRuleRecords"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
