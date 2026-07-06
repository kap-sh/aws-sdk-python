"""Generated from Smithy shape ``com.amazonaws.iot#TopicRulePayload``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot.types.action
    import aws_sdk_iot.types.action_list
    import aws_sdk_iot.types.aws_iot_sql_version
    import aws_sdk_iot.types.description
    import aws_sdk_iot.types.is_disabled
    import aws_sdk_iot.types.sql


class TopicRulePayload(TypedDict, closed=True):
    sql: "aws_sdk_iot.types.sql.SQL"
    r"""<p>The SQL statement used to query the topic. For more information, see <a href=\"https://docs.aws.amazon.com/iot/latest/developerguide/iot-sql-reference.html\">IoT SQL Reference</a> in the <i>IoT Developer Guide</i>.</p>"""
    description: NotRequired["aws_sdk_iot.types.description.Description"]
    """<p>The description of the rule.</p>"""
    actions: "aws_sdk_iot.types.action_list.ActionList"
    """<p>The actions associated with the rule.</p>"""
    rule_disabled: NotRequired["aws_sdk_iot.types.is_disabled.IsDisabled"]
    """<p>Specifies whether the rule is disabled.</p>"""
    aws_iot_sql_version: NotRequired[
        "aws_sdk_iot.types.aws_iot_sql_version.AwsIotSqlVersion"
    ]
    """<p>The version of the SQL rules engine to use when evaluating the rule.</p>"""
    error_action: NotRequired["aws_sdk_iot.types.action.Action"]
    """<p>The action to take when an error occurs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TopicRulePayload) -> dict:
    out: dict = {}
    out["sql"] = value["sql"]
    if "description" in value:
        out["description"] = value["description"]
    import aws_sdk_iot.types.action_list

    out["actions"] = aws_sdk_iot.types.action_list.serialize_json(value["actions"])
    if "rule_disabled" in value:
        out["ruleDisabled"] = value["rule_disabled"]
    if "aws_iot_sql_version" in value:
        out["awsIotSqlVersion"] = value["aws_iot_sql_version"]
    if "error_action" in value:
        import aws_sdk_iot.types.action

        out["errorAction"] = aws_sdk_iot.types.action.serialize_json(
            value["error_action"]
        )
    return out


def deserialize_json(data: dict) -> TopicRulePayload:
    out: TopicRulePayload = {}  # type: ignore[typeddict-item]
    if "sql" in data:
        out["sql"] = data["sql"]
    else:
        raise DeserializationError("TopicRulePayload.sql required")
    if "description" in data:
        out["description"] = data["description"]
    if "actions" in data:
        import aws_sdk_iot.types.action_list

        out["actions"] = aws_sdk_iot.types.action_list.deserialize_json(data["actions"])
    else:
        raise DeserializationError("TopicRulePayload.actions required")
    if "ruleDisabled" in data:
        out["rule_disabled"] = data["ruleDisabled"]
    if "awsIotSqlVersion" in data:
        out["aws_iot_sql_version"] = data["awsIotSqlVersion"]
    if "errorAction" in data:
        import aws_sdk_iot.types.action

        out["error_action"] = aws_sdk_iot.types.action.deserialize_json(
            data["errorAction"]
        )
    return out
