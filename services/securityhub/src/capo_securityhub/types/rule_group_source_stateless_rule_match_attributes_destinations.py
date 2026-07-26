"""Generated from Smithy shape ``com.amazonaws.securityhub#RuleGroupSourceStatelessRuleMatchAttributesDestinations``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string


class RuleGroupSourceStatelessRuleMatchAttributesDestinations(TypedDict, closed=True):
    address_definition: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>An IP address or a block of IP addresses.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: RuleGroupSourceStatelessRuleMatchAttributesDestinations,
) -> dict:
    out: dict = {}
    if "address_definition" in value:
        out["AddressDefinition"] = value["address_definition"]
    return out


def deserialize_json(
    data: dict,
) -> RuleGroupSourceStatelessRuleMatchAttributesDestinations:
    out: RuleGroupSourceStatelessRuleMatchAttributesDestinations = {}  # type: ignore[typeddict-item]
    if "AddressDefinition" in data:
        out["address_definition"] = data["AddressDefinition"]
    return out
