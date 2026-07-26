"""Generated from Smithy shape ``com.amazonaws.iot#TopicRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.action
    import capo_iot.types.action_list
    import capo_iot.types.aws_iot_sql_version
    import capo_iot.types.created_at_date
    import capo_iot.types.description
    import capo_iot.types.is_disabled
    import capo_iot.types.rule_name
    import capo_iot.types.sql


class TopicRule(TypedDict, closed=True):
    rule_name: NotRequired["capo_iot.types.rule_name.RuleName"]
    """<p>The name of the rule.</p>"""
    sql: NotRequired["capo_iot.types.sql.SQL"]
    """<p>The SQL statement used to query the topic. When using a SQL query with multiple lines, be sure to escape the newline characters.</p>"""
    description: NotRequired["capo_iot.types.description.Description"]
    """<p>The description of the rule.</p>"""
    created_at: NotRequired["capo_iot.types.created_at_date.CreatedAtDate"]
    """<p>The date and time the rule was created.</p>"""
    actions: NotRequired["capo_iot.types.action_list.ActionList"]
    """<p>The actions associated with the rule.</p>"""
    rule_disabled: NotRequired["capo_iot.types.is_disabled.IsDisabled"]
    """<p>Specifies whether the rule is disabled.</p>"""
    aws_iot_sql_version: NotRequired[
        "capo_iot.types.aws_iot_sql_version.AwsIotSqlVersion"
    ]
    """<p>The version of the SQL rules engine to use when evaluating the rule.</p>"""
    error_action: NotRequired["capo_iot.types.action.Action"]
    """<p>The action to perform when an error occurs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TopicRule) -> dict:
    out: dict = {}
    if "rule_name" in value:
        out["ruleName"] = value["rule_name"]
    if "sql" in value:
        out["sql"] = value["sql"]
    if "description" in value:
        out["description"] = value["description"]
    if "created_at" in value:
        import capo_iot.types.created_at_date

        out["createdAt"] = capo_iot.types.created_at_date.serialize_json(
            value["created_at"]
        )
    if "actions" in value:
        import capo_iot.types.action_list

        out["actions"] = capo_iot.types.action_list.serialize_json(value["actions"])
    if "rule_disabled" in value:
        out["ruleDisabled"] = value["rule_disabled"]
    if "aws_iot_sql_version" in value:
        out["awsIotSqlVersion"] = value["aws_iot_sql_version"]
    if "error_action" in value:
        import capo_iot.types.action

        out["errorAction"] = capo_iot.types.action.serialize_json(value["error_action"])
    return out


def deserialize_json(data: dict) -> TopicRule:
    out: TopicRule = {}  # type: ignore[typeddict-item]
    if "ruleName" in data:
        out["rule_name"] = data["ruleName"]
    if "sql" in data:
        out["sql"] = data["sql"]
    if "description" in data:
        out["description"] = data["description"]
    if "createdAt" in data:
        import capo_iot.types.created_at_date

        out["created_at"] = capo_iot.types.created_at_date.deserialize_json(
            data["createdAt"]
        )
    if "actions" in data:
        import capo_iot.types.action_list

        out["actions"] = capo_iot.types.action_list.deserialize_json(data["actions"])
    if "ruleDisabled" in data:
        out["rule_disabled"] = data["ruleDisabled"]
    if "awsIotSqlVersion" in data:
        out["aws_iot_sql_version"] = data["awsIotSqlVersion"]
    if "errorAction" in data:
        import capo_iot.types.action

        out["error_action"] = capo_iot.types.action.deserialize_json(
            data["errorAction"]
        )
    return out
