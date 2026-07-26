"""Generated from Smithy shape ``com.amazonaws.configservice#GetCustomRulePolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.config_rule_name


class GetCustomRulePolicyRequest(TypedDict, closed=True):
    config_rule_name: NotRequired[
        "capo_config_service.types.config_rule_name.ConfigRuleName"
    ]
    """<p>The name of your Config Custom Policy rule.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetCustomRulePolicyRequest) -> dict:
    out: dict = {}
    if "config_rule_name" in value:
        out["ConfigRuleName"] = value["config_rule_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetCustomRulePolicyRequest:
    out: GetCustomRulePolicyRequest = {}  # type: ignore[typeddict-item]
    if "ConfigRuleName" in data:
        out["config_rule_name"] = data["ConfigRuleName"]
    return out
