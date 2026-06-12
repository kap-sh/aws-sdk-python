"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsWafRegionalWebAclRulesListActionDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsWafRegionalWebAclRulesListActionDetails(TypedDict):
    type: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>For actions that are associated with a rule, the action that WAF takes when a web request matches all conditions in a rule. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsWafRegionalWebAclRulesListActionDetails) -> dict:
    out: dict = {}
    if "type" in value:
        out["Type"] = value["type"]
    return out


def deserialize_json(data: dict) -> AwsWafRegionalWebAclRulesListActionDetails:
    out: AwsWafRegionalWebAclRulesListActionDetails = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        out["type"] = data["Type"]
    return out
