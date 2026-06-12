"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsWafRegionalWebAclRulesListOverrideActionDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsWafRegionalWebAclRulesListOverrideActionDetails(TypedDict):
    type: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>Overrides the rule evaluation result in the rule group. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsWafRegionalWebAclRulesListOverrideActionDetails) -> dict:
    out: dict = {}
    if "type" in value:
        out["Type"] = value["type"]
    return out


def deserialize_json(data: dict) -> AwsWafRegionalWebAclRulesListOverrideActionDetails:
    out: AwsWafRegionalWebAclRulesListOverrideActionDetails = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        out["type"] = data["Type"]
    return out
