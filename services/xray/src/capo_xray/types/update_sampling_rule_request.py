"""Generated from Smithy shape ``com.amazonaws.xray#UpdateSamplingRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_xray.errors import DeserializationError

if TYPE_CHECKING:
    import capo_xray.types.sampling_rule_update


class UpdateSamplingRuleRequest(TypedDict, closed=True):
    sampling_rule_update: "capo_xray.types.sampling_rule_update.SamplingRuleUpdate"
    """<p>The rule and fields to change.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSamplingRuleRequest) -> dict:
    out: dict = {}
    import capo_xray.types.sampling_rule_update

    out["SamplingRuleUpdate"] = capo_xray.types.sampling_rule_update.serialize_json(
        value["sampling_rule_update"]
    )
    return out


def deserialize_json(data: dict) -> UpdateSamplingRuleRequest:
    out: UpdateSamplingRuleRequest = {}  # type: ignore[typeddict-item]
    if "SamplingRuleUpdate" in data:
        import capo_xray.types.sampling_rule_update

        out["sampling_rule_update"] = (
            capo_xray.types.sampling_rule_update.deserialize_json(
                data["SamplingRuleUpdate"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateSamplingRuleRequest.sampling_rule_update required"
        )
    return out
