"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#DeleteSipRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.non_empty_string


class DeleteSipRuleRequest(TypedDict, closed=True):
    sip_rule_id: "capo_chime_sdk_voice.types.non_empty_string.NonEmptyString"
    """<p>The SIP rule ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteSipRuleRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteSipRuleRequest:
    out: DeleteSipRuleRequest = {}  # type: ignore[typeddict-item]
    return out
