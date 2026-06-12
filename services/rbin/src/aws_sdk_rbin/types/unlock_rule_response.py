"""Generated from Smithy shape ``com.amazonaws.rbin#UnlockRuleResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_rbin.types.description
    import aws_sdk_rbin.types.exclude_resource_tags
    import aws_sdk_rbin.types.lock_configuration
    import aws_sdk_rbin.types.lock_state
    import aws_sdk_rbin.types.resource_tags
    import aws_sdk_rbin.types.resource_type
    import aws_sdk_rbin.types.retention_period
    import aws_sdk_rbin.types.rule_arn
    import aws_sdk_rbin.types.rule_identifier
    import aws_sdk_rbin.types.rule_status
    import aws_sdk_rbin.types.time_stamp


class UnlockRuleResponse(TypedDict):
    identifier: NotRequired["aws_sdk_rbin.types.rule_identifier.RuleIdentifier"]
    """<p>The unique ID of the retention rule.</p>"""
    description: NotRequired["aws_sdk_rbin.types.description.Description"]
    """<p>The retention rule description.</p>"""
    resource_type: NotRequired["aws_sdk_rbin.types.resource_type.ResourceType"]
    """<p>The resource type retained by the retention rule.</p>"""
    retention_period: NotRequired["aws_sdk_rbin.types.retention_period.RetentionPeriod"]
    resource_tags: NotRequired["aws_sdk_rbin.types.resource_tags.ResourceTags"]
    """<p>[Tag-level retention rules only] Information about the resource tags used to identify resources that are retained by the retention rule.</p>"""
    status: NotRequired["aws_sdk_rbin.types.rule_status.RuleStatus"]
    """<p>The state of the retention rule. Only retention rules that are in the <code>available</code> state retain resources.</p>"""
    lock_configuration: NotRequired[
        "aws_sdk_rbin.types.lock_configuration.LockConfiguration"
    ]
    """<p>Information about the retention rule lock configuration.</p>"""
    lock_state: NotRequired["aws_sdk_rbin.types.lock_state.LockState"]
    """<p>[Region-level retention rules only] The lock state for the retention rule.</p> <ul> <li> <p> <code>locked</code> - The retention rule is locked and can't be modified or deleted.</p> </li> <li> <p> <code>pending_unlock</code> - The retention rule has been unlocked but it is still within the unlock delay period. The retention rule can be modified or deleted only after the unlock delay period has expired.</p> </li> <li> <p> <code>unlocked</code> - The retention rule is unlocked and it can be modified or deleted by any user with the required permissions.</p> </li> <li> <p> <code>null</code> - The retention rule has never been locked. Once a retention rule has been locked, it can transition between the <code>locked</code> and <code>unlocked</code> states only; it can never transition back to <code>null</code>.</p> </li> </ul>"""
    lock_end_time: NotRequired["aws_sdk_rbin.types.time_stamp.TimeStamp"]
    """<p>The date and time at which the unlock delay is set to expire. Only returned for retention rules that have been unlocked and that are still within the unlock delay period.</p>"""
    rule_arn: NotRequired["aws_sdk_rbin.types.rule_arn.RuleArn"]
    """<p>The Amazon Resource Name (ARN) of the retention rule.</p>"""
    exclude_resource_tags: NotRequired[
        "aws_sdk_rbin.types.exclude_resource_tags.ExcludeResourceTags"
    ]
    """<p>[Region-level retention rules only] Information about the exclusion tags used to identify resources that are to be excluded, or ignored, by the retention rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UnlockRuleResponse) -> dict:
    out: dict = {}
    if "identifier" in value:
        out["Identifier"] = value["identifier"]
    if "description" in value:
        out["Description"] = value["description"]
    if "resource_type" in value:
        import aws_sdk_rbin.types.resource_type

        out["ResourceType"] = aws_sdk_rbin.types.resource_type.serialize_json(
            value["resource_type"]
        )
    if "retention_period" in value:
        import aws_sdk_rbin.types.retention_period

        out["RetentionPeriod"] = aws_sdk_rbin.types.retention_period.serialize_json(
            value["retention_period"]
        )
    if "resource_tags" in value:
        import aws_sdk_rbin.types.resource_tags

        out["ResourceTags"] = aws_sdk_rbin.types.resource_tags.serialize_json(
            value["resource_tags"]
        )
    if "status" in value:
        import aws_sdk_rbin.types.rule_status

        out["Status"] = aws_sdk_rbin.types.rule_status.serialize_json(value["status"])
    if "lock_configuration" in value:
        import aws_sdk_rbin.types.lock_configuration

        out["LockConfiguration"] = aws_sdk_rbin.types.lock_configuration.serialize_json(
            value["lock_configuration"]
        )
    if "lock_state" in value:
        import aws_sdk_rbin.types.lock_state

        out["LockState"] = aws_sdk_rbin.types.lock_state.serialize_json(
            value["lock_state"]
        )
    if "lock_end_time" in value:
        import aws_sdk_rbin.types.time_stamp

        out["LockEndTime"] = aws_sdk_rbin.types.time_stamp.serialize_json(
            value["lock_end_time"]
        )
    if "rule_arn" in value:
        out["RuleArn"] = value["rule_arn"]
    if "exclude_resource_tags" in value:
        import aws_sdk_rbin.types.exclude_resource_tags

        out["ExcludeResourceTags"] = (
            aws_sdk_rbin.types.exclude_resource_tags.serialize_json(
                value["exclude_resource_tags"]
            )
        )
    return out


def deserialize_json(data: dict) -> UnlockRuleResponse:
    out: UnlockRuleResponse = {}  # type: ignore[typeddict-item]
    if "Identifier" in data:
        out["identifier"] = data["Identifier"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "ResourceType" in data:
        import aws_sdk_rbin.types.resource_type

        out["resource_type"] = aws_sdk_rbin.types.resource_type.deserialize_json(
            data["ResourceType"]
        )
    if "RetentionPeriod" in data:
        import aws_sdk_rbin.types.retention_period

        out["retention_period"] = aws_sdk_rbin.types.retention_period.deserialize_json(
            data["RetentionPeriod"]
        )
    if "ResourceTags" in data:
        import aws_sdk_rbin.types.resource_tags

        out["resource_tags"] = aws_sdk_rbin.types.resource_tags.deserialize_json(
            data["ResourceTags"]
        )
    if "Status" in data:
        import aws_sdk_rbin.types.rule_status

        out["status"] = aws_sdk_rbin.types.rule_status.deserialize_json(data["Status"])
    if "LockConfiguration" in data:
        import aws_sdk_rbin.types.lock_configuration

        out["lock_configuration"] = (
            aws_sdk_rbin.types.lock_configuration.deserialize_json(
                data["LockConfiguration"]
            )
        )
    if "LockState" in data:
        import aws_sdk_rbin.types.lock_state

        out["lock_state"] = aws_sdk_rbin.types.lock_state.deserialize_json(
            data["LockState"]
        )
    if "LockEndTime" in data:
        import aws_sdk_rbin.types.time_stamp

        out["lock_end_time"] = aws_sdk_rbin.types.time_stamp.deserialize_json(
            data["LockEndTime"]
        )
    if "RuleArn" in data:
        out["rule_arn"] = data["RuleArn"]
    if "ExcludeResourceTags" in data:
        import aws_sdk_rbin.types.exclude_resource_tags

        out["exclude_resource_tags"] = (
            aws_sdk_rbin.types.exclude_resource_tags.deserialize_json(
                data["ExcludeResourceTags"]
            )
        )
    return out
