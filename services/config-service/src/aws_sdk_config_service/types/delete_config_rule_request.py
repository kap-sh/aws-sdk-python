"""Generated from Smithy shape ``com.amazonaws.configservice#DeleteConfigRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_config_service.types.config_rule_name


class DeleteConfigRuleRequest(TypedDict, closed=True):
    config_rule_name: "aws_sdk_config_service.types.config_rule_name.ConfigRuleName"
    """<p>The name of the Config rule that you want to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteConfigRuleRequest) -> dict:
    out: dict = {}
    out["ConfigRuleName"] = value["config_rule_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteConfigRuleRequest:
    out: DeleteConfigRuleRequest = {}  # type: ignore[typeddict-item]
    if "ConfigRuleName" in data:
        out["config_rule_name"] = data["ConfigRuleName"]
    else:
        raise DeserializationError("DeleteConfigRuleRequest.config_rule_name required")
    return out
