"""Generated from Smithy shape ``com.amazonaws.mailmanager#RuleSet``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import aws_sdk_mailmanager.types.rule_set_id
    import aws_sdk_mailmanager.types.rule_set_name


class RuleSet(TypedDict, closed=True):
    rule_set_id: NotRequired["aws_sdk_mailmanager.types.rule_set_id.RuleSetId"]
    """<p>The identifier of the rule set.</p>"""
    rule_set_name: NotRequired["aws_sdk_mailmanager.types.rule_set_name.RuleSetName"]
    """<p>A user-friendly name for the rule set.</p>"""
    last_modification_date: NotRequired["datetime.datetime"]
    """<p>The last modification date of the rule set.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RuleSet) -> dict:
    out: dict = {}
    if "rule_set_id" in value:
        out["RuleSetId"] = value["rule_set_id"]
    if "rule_set_name" in value:
        out["RuleSetName"] = value["rule_set_name"]
    if "last_modification_date" in value:
        import aws_sdk_mailmanager.types._prelude.timestamp

        out["LastModificationDate"] = (
            aws_sdk_mailmanager.types._prelude.timestamp.serialize_aws_json_1_0(
                value["last_modification_date"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> RuleSet:
    out: RuleSet = {}  # type: ignore[typeddict-item]
    if "RuleSetId" in data:
        out["rule_set_id"] = data["RuleSetId"]
    if "RuleSetName" in data:
        out["rule_set_name"] = data["RuleSetName"]
    if "LastModificationDate" in data:
        import aws_sdk_mailmanager.types._prelude.timestamp

        out["last_modification_date"] = (
            aws_sdk_mailmanager.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["LastModificationDate"]
            )
        )
    return out
