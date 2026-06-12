"""Generated from Smithy shape ``com.amazonaws.xray#DeleteSamplingRuleResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_xray.types.sampling_rule_record


class DeleteSamplingRuleResult(TypedDict):
    sampling_rule_record: NotRequired[
        "aws_sdk_xray.types.sampling_rule_record.SamplingRuleRecord"
    ]
    """<p>The deleted rule definition and metadata.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteSamplingRuleResult) -> dict:
    out: dict = {}
    if "sampling_rule_record" in value:
        import aws_sdk_xray.types.sampling_rule_record

        out["SamplingRuleRecord"] = (
            aws_sdk_xray.types.sampling_rule_record.serialize_json(
                value["sampling_rule_record"]
            )
        )
    return out


def deserialize_json(data: dict) -> DeleteSamplingRuleResult:
    out: DeleteSamplingRuleResult = {}  # type: ignore[typeddict-item]
    if "SamplingRuleRecord" in data:
        import aws_sdk_xray.types.sampling_rule_record

        out["sampling_rule_record"] = (
            aws_sdk_xray.types.sampling_rule_record.deserialize_json(
                data["SamplingRuleRecord"]
            )
        )
    return out
