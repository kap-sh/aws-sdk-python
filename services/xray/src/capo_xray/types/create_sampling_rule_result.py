"""Generated from Smithy shape ``com.amazonaws.xray#CreateSamplingRuleResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_xray.types.sampling_rule_record


class CreateSamplingRuleResult(TypedDict, closed=True):
    sampling_rule_record: NotRequired[
        "capo_xray.types.sampling_rule_record.SamplingRuleRecord"
    ]
    """<p>The saved rule definition and metadata.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSamplingRuleResult) -> dict:
    out: dict = {}
    if "sampling_rule_record" in value:
        import capo_xray.types.sampling_rule_record

        out["SamplingRuleRecord"] = capo_xray.types.sampling_rule_record.serialize_json(
            value["sampling_rule_record"]
        )
    return out


def deserialize_json(data: dict) -> CreateSamplingRuleResult:
    out: CreateSamplingRuleResult = {}  # type: ignore[typeddict-item]
    if "SamplingRuleRecord" in data:
        import capo_xray.types.sampling_rule_record

        out["sampling_rule_record"] = (
            capo_xray.types.sampling_rule_record.deserialize_json(
                data["SamplingRuleRecord"]
            )
        )
    return out
