"""Generated from Smithy shape ``com.amazonaws.configservice#DescribeConfigRulesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_config_service.types.config_rule_names
    import aws_sdk_config_service.types.describe_config_rules_filters
    import aws_sdk_config_service.types.string


class DescribeConfigRulesRequest(TypedDict):
    config_rule_names: NotRequired[
        "aws_sdk_config_service.types.config_rule_names.ConfigRuleNames"
    ]
    """<p>The names of the Config rules for which you want details. If you do not specify any names, Config returns details for all your rules.</p>"""
    next_token: NotRequired["aws_sdk_config_service.types.string.String"]
    """<p>The <code>nextToken</code> string returned on a previous page that you use to get the next page of results in a paginated response.</p>"""
    filters: NotRequired[
        "aws_sdk_config_service.types.describe_config_rules_filters.DescribeConfigRulesFilters"
    ]
    """<p>Returns a list of Detective or Proactive Config rules. By default, this API returns an unfiltered list. For more information on Detective or Proactive Config rules, see <a href=\"https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config-rules.html\"> <b>Evaluation Mode</b> </a> in the <i>Config Developer Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeConfigRulesRequest) -> dict:
    out: dict = {}
    if "config_rule_names" in value:
        import aws_sdk_config_service.types.config_rule_names

        out["ConfigRuleNames"] = (
            aws_sdk_config_service.types.config_rule_names.serialize_aws_json_1_1(
                value["config_rule_names"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "filters" in value:
        import aws_sdk_config_service.types.describe_config_rules_filters

        out["Filters"] = (
            aws_sdk_config_service.types.describe_config_rules_filters.serialize_aws_json_1_1(
                value["filters"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeConfigRulesRequest:
    out: DescribeConfigRulesRequest = {}  # type: ignore[typeddict-item]
    if "ConfigRuleNames" in data:
        import aws_sdk_config_service.types.config_rule_names

        out["config_rule_names"] = (
            aws_sdk_config_service.types.config_rule_names.deserialize_aws_json_1_1(
                data["ConfigRuleNames"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Filters" in data:
        import aws_sdk_config_service.types.describe_config_rules_filters

        out["filters"] = (
            aws_sdk_config_service.types.describe_config_rules_filters.deserialize_aws_json_1_1(
                data["Filters"]
            )
        )
    return out
