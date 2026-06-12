"""Generated from Smithy shape ``com.amazonaws.securityhub#RuleGroupSourceStatelessRuleMatchAttributesSources``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class RuleGroupSourceStatelessRuleMatchAttributesSources(TypedDict):
    address_definition: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>An IP address or a block of IP addresses.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RuleGroupSourceStatelessRuleMatchAttributesSources) -> dict:
    out: dict = {}
    if "address_definition" in value:
        out["AddressDefinition"] = value["address_definition"]
    return out


def deserialize_json(data: dict) -> RuleGroupSourceStatelessRuleMatchAttributesSources:
    out: RuleGroupSourceStatelessRuleMatchAttributesSources = {}  # type: ignore[typeddict-item]
    if "AddressDefinition" in data:
        out["address_definition"] = data["AddressDefinition"]
    return out
