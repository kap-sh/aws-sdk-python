"""Generated from Smithy shape ``com.amazonaws.securityhub#RuleGroupSourceStatelessRuleMatchAttributesTcpFlags``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string_list


class RuleGroupSourceStatelessRuleMatchAttributesTcpFlags(TypedDict, closed=True):
    flags: NotRequired[
        "capo_securityhub.types.non_empty_string_list.NonEmptyStringList"
    ]
    """<p>Defines the flags from the <code>Masks</code> setting that must be set in order for the packet to match. Flags that are listed must be set. Flags that are not listed must not be set.</p>"""
    masks: NotRequired[
        "capo_securityhub.types.non_empty_string_list.NonEmptyStringList"
    ]
    """<p>The set of flags to consider in the inspection. If not specified, then all flags are inspected.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RuleGroupSourceStatelessRuleMatchAttributesTcpFlags) -> dict:
    out: dict = {}
    if "flags" in value:
        import capo_securityhub.types.non_empty_string_list

        out["Flags"] = capo_securityhub.types.non_empty_string_list.serialize_json(
            value["flags"]
        )
    if "masks" in value:
        import capo_securityhub.types.non_empty_string_list

        out["Masks"] = capo_securityhub.types.non_empty_string_list.serialize_json(
            value["masks"]
        )
    return out


def deserialize_json(data: dict) -> RuleGroupSourceStatelessRuleMatchAttributesTcpFlags:
    out: RuleGroupSourceStatelessRuleMatchAttributesTcpFlags = {}  # type: ignore[typeddict-item]
    if "Flags" in data:
        import capo_securityhub.types.non_empty_string_list

        out["flags"] = capo_securityhub.types.non_empty_string_list.deserialize_json(
            data["Flags"]
        )
    if "Masks" in data:
        import capo_securityhub.types.non_empty_string_list

        out["masks"] = capo_securityhub.types.non_empty_string_list.deserialize_json(
            data["Masks"]
        )
    return out
