"""Generated from Smithy shape ``com.amazonaws.securityhub#WafOverrideAction``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class WafOverrideAction(TypedDict):
    type: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> <code>COUNT</code> overrides the action specified by the individual rule within a <code>RuleGroup</code> .</p> <p>If set to <code>NONE</code>, the rule's action takes place.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WafOverrideAction) -> dict:
    out: dict = {}
    if "type" in value:
        out["Type"] = value["type"]
    return out


def deserialize_json(data: dict) -> WafOverrideAction:
    out: WafOverrideAction = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        out["type"] = data["Type"]
    return out
