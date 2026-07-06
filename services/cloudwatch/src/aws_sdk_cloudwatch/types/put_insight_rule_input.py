"""Generated from Smithy shape ``com.amazonaws.cloudwatch#PutInsightRuleInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudwatch.types.insight_rule_definition
    import aws_sdk_cloudwatch.types.insight_rule_name
    import aws_sdk_cloudwatch.types.insight_rule_on_transformed_logs
    import aws_sdk_cloudwatch.types.insight_rule_state
    import aws_sdk_cloudwatch.types.tag_list


class PutInsightRuleInput(TypedDict, closed=True):
    rule_name: NotRequired["aws_sdk_cloudwatch.types.insight_rule_name.InsightRuleName"]
    """<p>A unique name for the rule.</p>"""
    rule_state: NotRequired[
        "aws_sdk_cloudwatch.types.insight_rule_state.InsightRuleState"
    ]
    """<p>The state of the rule. Valid values are ENABLED and DISABLED.</p>"""
    rule_definition: NotRequired[
        "aws_sdk_cloudwatch.types.insight_rule_definition.InsightRuleDefinition"
    ]
    r"""<p>The definition of the rule, as a JSON object. For details on the valid syntax, see <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContributorInsights-RuleSyntax.html\">Contributor Insights Rule Syntax</a>.</p>"""
    tags: NotRequired["aws_sdk_cloudwatch.types.tag_list.TagList"]
    r"""<p>A list of key-value pairs to associate with the Contributor Insights rule. You can associate as many as 50 tags with a rule.</p> <p>Tags can help you organize and categorize your resources. You can also use them to scope user permissions, by granting a user permission to access or change only the resources that have certain tag values.</p> <p>To be able to associate tags with a rule, you must have the <code>cloudwatch:TagResource</code> permission in addition to the <code>cloudwatch:PutInsightRule</code> permission.</p> <p>If you are using this operation to update an existing Contributor Insights rule, any tags you specify in this parameter are ignored. To change the tags of an existing rule, use <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_TagResource.html\">TagResource</a>.</p>"""
    apply_on_transformed_logs: NotRequired[
        "aws_sdk_cloudwatch.types.insight_rule_on_transformed_logs.InsightRuleOnTransformedLogs"
    ]
    r"""<p>Specify <code>true</code> to have this rule evaluate log events after they have been transformed by <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html\">Log transformation</a>. If you specify <code>true</code>, then the log events in log groups that have transformers will be evaluated by Contributor Insights after being transformed. Log groups that don't have transformers will still have their original log events evaluated by Contributor Insights.</p> <p>The default is <code>false</code> </p> <note> <p>If a log group has a transformer, and transformation fails for some log events, those log events won't be evaluated by Contributor Insights. For information about investigating log transformation failures, see <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Transformation-Errors-Metrics.html\">Transformation metrics and errors</a>.</p> </note>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PutInsightRuleInput) -> dict:
    out: dict = {}
    if "rule_name" in value:
        out["RuleName"] = value["rule_name"]
    if "rule_state" in value:
        out["RuleState"] = value["rule_state"]
    if "rule_definition" in value:
        out["RuleDefinition"] = value["rule_definition"]
    if "tags" in value:
        import aws_sdk_cloudwatch.types.tag_list

        out["Tags"] = aws_sdk_cloudwatch.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    if "apply_on_transformed_logs" in value:
        out["ApplyOnTransformedLogs"] = value["apply_on_transformed_logs"]
    return out


def deserialize_aws_json_1_0(data: dict) -> PutInsightRuleInput:
    out: PutInsightRuleInput = {}  # type: ignore[typeddict-item]
    if "RuleName" in data:
        out["rule_name"] = data["RuleName"]
    if "RuleState" in data:
        out["rule_state"] = data["RuleState"]
    if "RuleDefinition" in data:
        out["rule_definition"] = data["RuleDefinition"]
    if "Tags" in data:
        import aws_sdk_cloudwatch.types.tag_list

        out["tags"] = aws_sdk_cloudwatch.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    if "ApplyOnTransformedLogs" in data:
        out["apply_on_transformed_logs"] = data["ApplyOnTransformedLogs"]
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: PutInsightRuleInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "rule_name" in value:
        pairs.append((f"{prefix}.RuleName", str(value["rule_name"])))
    if "rule_state" in value:
        pairs.append((f"{prefix}.RuleState", str(value["rule_state"])))
    if "rule_definition" in value:
        pairs.append((f"{prefix}.RuleDefinition", str(value["rule_definition"])))
    if "tags" in value:
        import aws_sdk_cloudwatch.types.tag_list

        aws_sdk_cloudwatch.types.tag_list.serialize_query(
            value["tags"], pairs, f"{prefix}.Tags"
        )
    if "apply_on_transformed_logs" in value:
        pairs.append(
            (
                f"{prefix}.ApplyOnTransformedLogs",
                "true" if value["apply_on_transformed_logs"] else "false",
            )
        )


def deserialize_query(el: Element) -> PutInsightRuleInput:
    out: PutInsightRuleInput = {}  # type: ignore[typeddict-item]
    child_rule_name = el.find("RuleName")
    if child_rule_name is not None:
        out["rule_name"] = str(child_rule_name.text or "")
    child_rule_state = el.find("RuleState")
    if child_rule_state is not None:
        out["rule_state"] = str(child_rule_state.text or "")
    child_rule_definition = el.find("RuleDefinition")
    if child_rule_definition is not None:
        out["rule_definition"] = str(child_rule_definition.text or "")
    child_tags = el.find("Tags")
    if child_tags is not None:
        import aws_sdk_cloudwatch.types.tag_list

        out["tags"] = aws_sdk_cloudwatch.types.tag_list.deserialize_query(child_tags)
    child_apply_on_transformed_logs = el.find("ApplyOnTransformedLogs")
    if child_apply_on_transformed_logs is not None:
        out["apply_on_transformed_logs"] = (
            child_apply_on_transformed_logs.text or ""
        ).lower() == "true"
    return out
