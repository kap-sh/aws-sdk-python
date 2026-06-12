"""Generated from Smithy shape ``com.amazonaws.configservice#GetCustomRulePolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_config_service.types.config_rule_name


class GetCustomRulePolicyRequest(TypedDict):
    config_rule_name: NotRequired[
        "aws_sdk_config_service.types.config_rule_name.ConfigRuleName"
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
