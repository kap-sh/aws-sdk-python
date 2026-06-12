"""Generated from Smithy shape ``com.amazonaws.rbin#RuleSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_rbin.types.description
    import aws_sdk_rbin.types.lock_state
    import aws_sdk_rbin.types.retention_period
    import aws_sdk_rbin.types.rule_arn
    import aws_sdk_rbin.types.rule_identifier


class RuleSummary(TypedDict):
    identifier: NotRequired["aws_sdk_rbin.types.rule_identifier.RuleIdentifier"]
    """<p>The unique ID of the retention rule.</p>"""
    description: NotRequired["aws_sdk_rbin.types.description.Description"]
    """<p>The retention rule description.</p>"""
    retention_period: NotRequired["aws_sdk_rbin.types.retention_period.RetentionPeriod"]
    """<p>Information about the retention period for which the retention rule is to retain resources.</p>"""
    lock_state: NotRequired["aws_sdk_rbin.types.lock_state.LockState"]
    """<p>[Region-level retention rules only] The lock state for the retention rule.</p> <ul> <li> <p> <code>locked</code> - The retention rule is locked and can't be modified or deleted.</p> </li> <li> <p> <code>pending_unlock</code> - The retention rule has been unlocked but it is still within the unlock delay period. The retention rule can be modified or deleted only after the unlock delay period has expired.</p> </li> <li> <p> <code>unlocked</code> - The retention rule is unlocked and it can be modified or deleted by any user with the required permissions.</p> </li> <li> <p> <code>null</code> - The retention rule has never been locked. Once a retention rule has been locked, it can transition between the <code>locked</code> and <code>unlocked</code> states only; it can never transition back to <code>null</code>.</p> </li> </ul>"""
    rule_arn: NotRequired["aws_sdk_rbin.types.rule_arn.RuleArn"]
    """<p>The Amazon Resource Name (ARN) of the retention rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RuleSummary) -> dict:
    out: dict = {}
    if "identifier" in value:
        out["Identifier"] = value["identifier"]
    if "description" in value:
        out["Description"] = value["description"]
    if "retention_period" in value:
        import aws_sdk_rbin.types.retention_period

        out["RetentionPeriod"] = aws_sdk_rbin.types.retention_period.serialize_json(
            value["retention_period"]
        )
    if "lock_state" in value:
        import aws_sdk_rbin.types.lock_state

        out["LockState"] = aws_sdk_rbin.types.lock_state.serialize_json(
            value["lock_state"]
        )
    if "rule_arn" in value:
        out["RuleArn"] = value["rule_arn"]
    return out


def deserialize_json(data: dict) -> RuleSummary:
    out: RuleSummary = {}  # type: ignore[typeddict-item]
    if "Identifier" in data:
        out["identifier"] = data["Identifier"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "RetentionPeriod" in data:
        import aws_sdk_rbin.types.retention_period

        out["retention_period"] = aws_sdk_rbin.types.retention_period.deserialize_json(
            data["RetentionPeriod"]
        )
    if "LockState" in data:
        import aws_sdk_rbin.types.lock_state

        out["lock_state"] = aws_sdk_rbin.types.lock_state.deserialize_json(
            data["LockState"]
        )
    if "RuleArn" in data:
        out["rule_arn"] = data["RuleArn"]
    return out
