"""Generated from Smithy shape ``com.amazonaws.mailmanager#GetRuleSetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_mailmanager.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_mailmanager.types.rule_set_arn
    import aws_sdk_mailmanager.types.rule_set_id
    import aws_sdk_mailmanager.types.rule_set_name
    import aws_sdk_mailmanager.types.rules


class GetRuleSetResponse(TypedDict, closed=True):
    rule_set_id: "aws_sdk_mailmanager.types.rule_set_id.RuleSetId"
    """<p>The identifier of the rule set resource.</p>"""
    rule_set_arn: "aws_sdk_mailmanager.types.rule_set_arn.RuleSetArn"
    """<p>The Amazon Resource Name (ARN) of the rule set resource.</p>"""
    rule_set_name: "aws_sdk_mailmanager.types.rule_set_name.RuleSetName"
    """<p>A user-friendly name for the rule set resource.</p>"""
    created_date: "datetime.datetime"
    """<p>The date of when then rule set was created.</p>"""
    last_modification_date: "datetime.datetime"
    """<p>The date of when the rule set was last modified.</p>"""
    rules: "aws_sdk_mailmanager.types.rules.Rules"
    """<p>The rules contained in the rule set.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetRuleSetResponse) -> dict:
    out: dict = {}
    out["RuleSetId"] = value["rule_set_id"]
    out["RuleSetArn"] = value["rule_set_arn"]
    out["RuleSetName"] = value["rule_set_name"]
    import aws_sdk_mailmanager.types._prelude.timestamp

    out["CreatedDate"] = (
        aws_sdk_mailmanager.types._prelude.timestamp.serialize_aws_json_1_0(
            value["created_date"]
        )
    )
    import aws_sdk_mailmanager.types._prelude.timestamp

    out["LastModificationDate"] = (
        aws_sdk_mailmanager.types._prelude.timestamp.serialize_aws_json_1_0(
            value["last_modification_date"]
        )
    )
    import aws_sdk_mailmanager.types.rules

    out["Rules"] = aws_sdk_mailmanager.types.rules.serialize_aws_json_1_0(
        value["rules"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetRuleSetResponse:
    out: GetRuleSetResponse = {}  # type: ignore[typeddict-item]
    if "RuleSetId" in data:
        out["rule_set_id"] = data["RuleSetId"]
    else:
        raise DeserializationError("GetRuleSetResponse.rule_set_id required")
    if "RuleSetArn" in data:
        out["rule_set_arn"] = data["RuleSetArn"]
    else:
        raise DeserializationError("GetRuleSetResponse.rule_set_arn required")
    if "RuleSetName" in data:
        out["rule_set_name"] = data["RuleSetName"]
    else:
        raise DeserializationError("GetRuleSetResponse.rule_set_name required")
    if "CreatedDate" in data:
        import aws_sdk_mailmanager.types._prelude.timestamp

        out["created_date"] = (
            aws_sdk_mailmanager.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["CreatedDate"]
            )
        )
    else:
        raise DeserializationError("GetRuleSetResponse.created_date required")
    if "LastModificationDate" in data:
        import aws_sdk_mailmanager.types._prelude.timestamp

        out["last_modification_date"] = (
            aws_sdk_mailmanager.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["LastModificationDate"]
            )
        )
    else:
        raise DeserializationError("GetRuleSetResponse.last_modification_date required")
    if "Rules" in data:
        import aws_sdk_mailmanager.types.rules

        out["rules"] = aws_sdk_mailmanager.types.rules.deserialize_aws_json_1_0(
            data["Rules"]
        )
    else:
        raise DeserializationError("GetRuleSetResponse.rules required")
    return out
