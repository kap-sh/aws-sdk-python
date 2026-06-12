"""Generated from Smithy shape ``com.amazonaws.cloudwatch#ManagedRuleDescription``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudwatch.types.amazon_resource_name
    import aws_sdk_cloudwatch.types.managed_rule_state
    import aws_sdk_cloudwatch.types.template_name


class ManagedRuleDescription(TypedDict):
    template_name: NotRequired["aws_sdk_cloudwatch.types.template_name.TemplateName"]
    """<p> The template name for the managed rule. Used to enable managed rules using <code>PutManagedInsightRules</code>. </p>"""
    resource_arn: NotRequired[
        "aws_sdk_cloudwatch.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p> If a managed rule is enabled, this is the ARN for the related Amazon Web Services resource. </p>"""
    rule_state: NotRequired[
        "aws_sdk_cloudwatch.types.managed_rule_state.ManagedRuleState"
    ]
    """<p> Describes the state of a managed rule. If present, it contains information about the Contributor Insights rule that contains information about the related Amazon Web Services resource. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ManagedRuleDescription) -> dict:
    out: dict = {}
    if "template_name" in value:
        out["TemplateName"] = value["template_name"]
    if "resource_arn" in value:
        out["ResourceARN"] = value["resource_arn"]
    if "rule_state" in value:
        import aws_sdk_cloudwatch.types.managed_rule_state

        out["RuleState"] = (
            aws_sdk_cloudwatch.types.managed_rule_state.serialize_aws_json_1_0(
                value["rule_state"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ManagedRuleDescription:
    out: ManagedRuleDescription = {}  # type: ignore[typeddict-item]
    if "TemplateName" in data:
        out["template_name"] = data["TemplateName"]
    if "ResourceARN" in data:
        out["resource_arn"] = data["ResourceARN"]
    if "RuleState" in data:
        import aws_sdk_cloudwatch.types.managed_rule_state

        out["rule_state"] = (
            aws_sdk_cloudwatch.types.managed_rule_state.deserialize_aws_json_1_0(
                data["RuleState"]
            )
        )
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: ManagedRuleDescription, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "template_name" in value:
        pairs.append((f"{prefix}.TemplateName", str(value["template_name"])))
    if "resource_arn" in value:
        pairs.append((f"{prefix}.ResourceARN", str(value["resource_arn"])))
    if "rule_state" in value:
        import aws_sdk_cloudwatch.types.managed_rule_state

        aws_sdk_cloudwatch.types.managed_rule_state.serialize_query(
            value["rule_state"], pairs, f"{prefix}.RuleState"
        )


def deserialize_query(el: Element) -> ManagedRuleDescription:
    out: ManagedRuleDescription = {}  # type: ignore[typeddict-item]
    child_template_name = el.find("TemplateName")
    if child_template_name is not None:
        out["template_name"] = str(child_template_name.text or "")
    child_resource_arn = el.find("ResourceARN")
    if child_resource_arn is not None:
        out["resource_arn"] = str(child_resource_arn.text or "")
    child_rule_state = el.find("RuleState")
    if child_rule_state is not None:
        import aws_sdk_cloudwatch.types.managed_rule_state

        out["rule_state"] = (
            aws_sdk_cloudwatch.types.managed_rule_state.deserialize_query(
                child_rule_state
            )
        )
    return out
