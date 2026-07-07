"""Generated from Smithy shape ``com.amazonaws.cloudwatch#PutAlarmMuteRuleInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudwatch.types.alarm_description
    import aws_sdk_cloudwatch.types.mute_targets
    import aws_sdk_cloudwatch.types.name
    import aws_sdk_cloudwatch.types.rule
    import aws_sdk_cloudwatch.types.tag_list
    import aws_sdk_cloudwatch.types.timestamp


class PutAlarmMuteRuleInput(TypedDict, closed=True):
    name: NotRequired["aws_sdk_cloudwatch.types.name.Name"]
    """<p>The name of the alarm mute rule. This name must be unique within your Amazon Web Services account and region.</p>"""
    description: NotRequired[
        "aws_sdk_cloudwatch.types.alarm_description.AlarmDescription"
    ]
    """<p>A description of the alarm mute rule that helps you identify its purpose.</p>"""
    rule: NotRequired["aws_sdk_cloudwatch.types.rule.Rule"]
    """<p>The configuration that defines when and how long alarms should be muted.</p>"""
    mute_targets: NotRequired["aws_sdk_cloudwatch.types.mute_targets.MuteTargets"]
    """<p>Specifies which alarms this rule applies to.</p>"""
    tags: NotRequired["aws_sdk_cloudwatch.types.tag_list.TagList"]
    """<p>A list of key-value pairs to associate with the alarm mute rule. You can use tags to categorize and manage your mute rules.</p>"""
    start_date: NotRequired["aws_sdk_cloudwatch.types.timestamp.Timestamp"]
    """<p>The date and time after which the mute rule takes effect, specified as a timestamp in ISO 8601 format (for example, <code>2026-04-15T08:00:00Z</code>). If not specified, the mute rule takes effect immediately upon creation and the mutes are applied as per the schedule expression.</p>"""
    expire_date: NotRequired["aws_sdk_cloudwatch.types.timestamp.Timestamp"]
    """<p>The date and time when the mute rule expires and is no longer evaluated, specified as a timestamp in ISO 8601 format (for example, <code>2026-12-31T23:59:59Z</code>). After this time, the rule status becomes EXPIRED and will no longer mute the targeted alarms.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PutAlarmMuteRuleInput) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "rule" in value:
        import aws_sdk_cloudwatch.types.rule

        out["Rule"] = aws_sdk_cloudwatch.types.rule.serialize_aws_json_1_0(
            value["rule"]
        )
    if "mute_targets" in value:
        import aws_sdk_cloudwatch.types.mute_targets

        out["MuteTargets"] = (
            aws_sdk_cloudwatch.types.mute_targets.serialize_aws_json_1_0(
                value["mute_targets"]
            )
        )
    if "tags" in value:
        import aws_sdk_cloudwatch.types.tag_list

        out["Tags"] = aws_sdk_cloudwatch.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    if "start_date" in value:
        import aws_sdk_cloudwatch.types.timestamp

        out["StartDate"] = aws_sdk_cloudwatch.types.timestamp.serialize_aws_json_1_0(
            value["start_date"]
        )
    if "expire_date" in value:
        import aws_sdk_cloudwatch.types.timestamp

        out["ExpireDate"] = aws_sdk_cloudwatch.types.timestamp.serialize_aws_json_1_0(
            value["expire_date"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> PutAlarmMuteRuleInput:
    out: PutAlarmMuteRuleInput = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Rule" in data:
        import aws_sdk_cloudwatch.types.rule

        out["rule"] = aws_sdk_cloudwatch.types.rule.deserialize_aws_json_1_0(
            data["Rule"]
        )
    if "MuteTargets" in data:
        import aws_sdk_cloudwatch.types.mute_targets

        out["mute_targets"] = (
            aws_sdk_cloudwatch.types.mute_targets.deserialize_aws_json_1_0(
                data["MuteTargets"]
            )
        )
    if "Tags" in data:
        import aws_sdk_cloudwatch.types.tag_list

        out["tags"] = aws_sdk_cloudwatch.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    if "StartDate" in data:
        import aws_sdk_cloudwatch.types.timestamp

        out["start_date"] = aws_sdk_cloudwatch.types.timestamp.deserialize_aws_json_1_0(
            data["StartDate"]
        )
    if "ExpireDate" in data:
        import aws_sdk_cloudwatch.types.timestamp

        out["expire_date"] = (
            aws_sdk_cloudwatch.types.timestamp.deserialize_aws_json_1_0(
                data["ExpireDate"]
            )
        )
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: PutAlarmMuteRuleInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "name" in value:
        pairs.append((f"{prefix}.Name", str(value["name"])))
    if "description" in value:
        pairs.append((f"{prefix}.Description", str(value["description"])))
    if "rule" in value:
        import aws_sdk_cloudwatch.types.rule

        aws_sdk_cloudwatch.types.rule.serialize_query(
            value["rule"], pairs, f"{prefix}.Rule"
        )
    if "mute_targets" in value:
        import aws_sdk_cloudwatch.types.mute_targets

        aws_sdk_cloudwatch.types.mute_targets.serialize_query(
            value["mute_targets"], pairs, f"{prefix}.MuteTargets"
        )
    if "tags" in value:
        import aws_sdk_cloudwatch.types.tag_list

        aws_sdk_cloudwatch.types.tag_list.serialize_query(
            value["tags"], pairs, f"{prefix}.Tags"
        )
    if "start_date" in value:
        import aws_sdk_cloudwatch.types.timestamp

        aws_sdk_cloudwatch.types.timestamp.serialize_query(
            value["start_date"], pairs, f"{prefix}.StartDate"
        )
    if "expire_date" in value:
        import aws_sdk_cloudwatch.types.timestamp

        aws_sdk_cloudwatch.types.timestamp.serialize_query(
            value["expire_date"], pairs, f"{prefix}.ExpireDate"
        )


def deserialize_query(el: Element) -> PutAlarmMuteRuleInput:
    out: PutAlarmMuteRuleInput = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_rule = el.find("Rule")
    if child_rule is not None:
        import aws_sdk_cloudwatch.types.rule

        out["rule"] = aws_sdk_cloudwatch.types.rule.deserialize_query(child_rule)
    child_mute_targets = el.find("MuteTargets")
    if child_mute_targets is not None:
        import aws_sdk_cloudwatch.types.mute_targets

        out["mute_targets"] = aws_sdk_cloudwatch.types.mute_targets.deserialize_query(
            child_mute_targets
        )
    child_tags = el.find("Tags")
    if child_tags is not None:
        import aws_sdk_cloudwatch.types.tag_list

        out["tags"] = aws_sdk_cloudwatch.types.tag_list.deserialize_query(child_tags)
    child_start_date = el.find("StartDate")
    if child_start_date is not None:
        import aws_sdk_cloudwatch.types.timestamp

        out["start_date"] = aws_sdk_cloudwatch.types.timestamp.deserialize_query(
            child_start_date
        )
    child_expire_date = el.find("ExpireDate")
    if child_expire_date is not None:
        import aws_sdk_cloudwatch.types.timestamp

        out["expire_date"] = aws_sdk_cloudwatch.types.timestamp.deserialize_query(
            child_expire_date
        )
    return out
