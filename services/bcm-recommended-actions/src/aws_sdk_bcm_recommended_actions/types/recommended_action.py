"""Generated from Smithy shape ``com.amazonaws.bcmrecommendedactions#RecommendedAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bcm_recommended_actions.types.account_id
    import aws_sdk_bcm_recommended_actions.types.action_type
    import aws_sdk_bcm_recommended_actions.types.context
    import aws_sdk_bcm_recommended_actions.types.feature
    import aws_sdk_bcm_recommended_actions.types.next_steps
    import aws_sdk_bcm_recommended_actions.types.severity


class RecommendedAction(TypedDict, closed=True):
    id: NotRequired["str"]
    """<p>The ID for the recommended action.</p>"""
    type: NotRequired["aws_sdk_bcm_recommended_actions.types.action_type.ActionType"]
    """<p>The type of action you can take by adopting the recommended action.</p>"""
    account_id: NotRequired[
        "aws_sdk_bcm_recommended_actions.types.account_id.AccountId"
    ]
    """<p>The account that the recommended action is for.</p>"""
    severity: NotRequired["aws_sdk_bcm_recommended_actions.types.severity.Severity"]
    """<p>The severity associated with the recommended action.</p>"""
    feature: NotRequired["aws_sdk_bcm_recommended_actions.types.feature.Feature"]
    """<p>The feature associated with the recommended action.</p>"""
    context: NotRequired["aws_sdk_bcm_recommended_actions.types.context.Context"]
    """<p>Context that applies to the recommended action.</p>"""
    next_steps: NotRequired[
        "aws_sdk_bcm_recommended_actions.types.next_steps.NextSteps"
    ]
    """<p>The possible next steps to execute the recommended action.</p>"""
    last_updated_time_stamp: NotRequired["str"]
    """<p>The time when the recommended action status was last updated.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RecommendedAction) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "type" in value:
        import aws_sdk_bcm_recommended_actions.types.action_type

        out["type"] = (
            aws_sdk_bcm_recommended_actions.types.action_type.serialize_aws_json_1_0(
                value["type"]
            )
        )
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "severity" in value:
        import aws_sdk_bcm_recommended_actions.types.severity

        out["severity"] = (
            aws_sdk_bcm_recommended_actions.types.severity.serialize_aws_json_1_0(
                value["severity"]
            )
        )
    if "feature" in value:
        import aws_sdk_bcm_recommended_actions.types.feature

        out["feature"] = (
            aws_sdk_bcm_recommended_actions.types.feature.serialize_aws_json_1_0(
                value["feature"]
            )
        )
    if "context" in value:
        import aws_sdk_bcm_recommended_actions.types.context

        out["context"] = (
            aws_sdk_bcm_recommended_actions.types.context.serialize_aws_json_1_0(
                value["context"]
            )
        )
    if "next_steps" in value:
        import aws_sdk_bcm_recommended_actions.types.next_steps

        out["nextSteps"] = (
            aws_sdk_bcm_recommended_actions.types.next_steps.serialize_aws_json_1_0(
                value["next_steps"]
            )
        )
    if "last_updated_time_stamp" in value:
        out["lastUpdatedTimeStamp"] = value["last_updated_time_stamp"]
    return out


def deserialize_aws_json_1_0(data: dict) -> RecommendedAction:
    out: RecommendedAction = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "type" in data:
        import aws_sdk_bcm_recommended_actions.types.action_type

        out["type"] = (
            aws_sdk_bcm_recommended_actions.types.action_type.deserialize_aws_json_1_0(
                data["type"]
            )
        )
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    if "severity" in data:
        import aws_sdk_bcm_recommended_actions.types.severity

        out["severity"] = (
            aws_sdk_bcm_recommended_actions.types.severity.deserialize_aws_json_1_0(
                data["severity"]
            )
        )
    if "feature" in data:
        import aws_sdk_bcm_recommended_actions.types.feature

        out["feature"] = (
            aws_sdk_bcm_recommended_actions.types.feature.deserialize_aws_json_1_0(
                data["feature"]
            )
        )
    if "context" in data:
        import aws_sdk_bcm_recommended_actions.types.context

        out["context"] = (
            aws_sdk_bcm_recommended_actions.types.context.deserialize_aws_json_1_0(
                data["context"]
            )
        )
    if "nextSteps" in data:
        import aws_sdk_bcm_recommended_actions.types.next_steps

        out["next_steps"] = (
            aws_sdk_bcm_recommended_actions.types.next_steps.deserialize_aws_json_1_0(
                data["nextSteps"]
            )
        )
    if "lastUpdatedTimeStamp" in data:
        out["last_updated_time_stamp"] = data["lastUpdatedTimeStamp"]
    return out
