"""Generated from Smithy shape ``com.amazonaws.configservice#DescribeConfigRulesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.config_rules
    import capo_config_service.types.string


class DescribeConfigRulesResponse(TypedDict, closed=True):
    config_rules: NotRequired["capo_config_service.types.config_rules.ConfigRules"]
    """<p>The details about your Config rules.</p>"""
    next_token: NotRequired["capo_config_service.types.string.String"]
    """<p>The string that you use in a subsequent request to get the next page of results in a paginated response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeConfigRulesResponse) -> dict:
    out: dict = {}
    if "config_rules" in value:
        import capo_config_service.types.config_rules

        out["ConfigRules"] = (
            capo_config_service.types.config_rules.serialize_aws_json_1_1(
                value["config_rules"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeConfigRulesResponse:
    out: DescribeConfigRulesResponse = {}  # type: ignore[typeddict-item]
    if "ConfigRules" in data:
        import capo_config_service.types.config_rules

        out["config_rules"] = (
            capo_config_service.types.config_rules.deserialize_aws_json_1_1(
                data["ConfigRules"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
