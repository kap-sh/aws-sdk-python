"""Generated from Smithy shape ``com.amazonaws.securityhub#WafAction``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class WafAction(TypedDict):
    type: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>Specifies how you want WAF to respond to requests that match the settings in a rule.</p> <p>Valid settings include the following:</p> <ul> <li> <p> <code>ALLOW</code> - WAF allows requests</p> </li> <li> <p> <code>BLOCK</code> - WAF blocks requests</p> </li> <li> <p> <code>COUNT</code> - WAF increments a counter of the requests that match all of the conditions in the rule. WAF then continues to inspect the web request based on the remaining rules in the web ACL. You can't specify <code>COUNT</code> for the default action for a web ACL.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: WafAction) -> dict:
    out: dict = {}
    if "type" in value:
        out["Type"] = value["type"]
    return out


def deserialize_json(data: dict) -> WafAction:
    out: WafAction = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        out["type"] = data["Type"]
    return out
