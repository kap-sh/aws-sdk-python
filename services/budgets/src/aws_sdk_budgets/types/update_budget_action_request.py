"""Generated from Smithy shape ``com.amazonaws.budgets#UpdateBudgetActionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_budgets.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_budgets.types.account_id
    import aws_sdk_budgets.types.action_id
    import aws_sdk_budgets.types.action_threshold
    import aws_sdk_budgets.types.approval_model
    import aws_sdk_budgets.types.budget_name
    import aws_sdk_budgets.types.definition
    import aws_sdk_budgets.types.notification_type
    import aws_sdk_budgets.types.role_arn
    import aws_sdk_budgets.types.subscribers


class UpdateBudgetActionRequest(TypedDict):
    account_id: "aws_sdk_budgets.types.account_id.AccountId"
    budget_name: "aws_sdk_budgets.types.budget_name.BudgetName"
    action_id: "aws_sdk_budgets.types.action_id.ActionId"
    """<p> A system-generated universally unique identifier (UUID) for the action. </p>"""
    notification_type: NotRequired[
        "aws_sdk_budgets.types.notification_type.NotificationType"
    ]
    action_threshold: NotRequired[
        "aws_sdk_budgets.types.action_threshold.ActionThreshold"
    ]
    definition: NotRequired["aws_sdk_budgets.types.definition.Definition"]
    execution_role_arn: NotRequired["aws_sdk_budgets.types.role_arn.RoleArn"]
    """<p> The role passed for action execution and reversion. Roles and actions must be in the same account. </p>"""
    approval_model: NotRequired["aws_sdk_budgets.types.approval_model.ApprovalModel"]
    """<p> This specifies if the action needs manual or automatic approval. </p>"""
    subscribers: NotRequired["aws_sdk_budgets.types.subscribers.Subscribers"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateBudgetActionRequest) -> dict:
    out: dict = {}
    out["AccountId"] = value["account_id"]
    out["BudgetName"] = value["budget_name"]
    out["ActionId"] = value["action_id"]
    if "notification_type" in value:
        import aws_sdk_budgets.types.notification_type

        out["NotificationType"] = (
            aws_sdk_budgets.types.notification_type.serialize_aws_json_1_1(
                value["notification_type"]
            )
        )
    if "action_threshold" in value:
        import aws_sdk_budgets.types.action_threshold

        out["ActionThreshold"] = (
            aws_sdk_budgets.types.action_threshold.serialize_aws_json_1_1(
                value["action_threshold"]
            )
        )
    if "definition" in value:
        import aws_sdk_budgets.types.definition

        out["Definition"] = aws_sdk_budgets.types.definition.serialize_aws_json_1_1(
            value["definition"]
        )
    if "execution_role_arn" in value:
        out["ExecutionRoleArn"] = value["execution_role_arn"]
    if "approval_model" in value:
        import aws_sdk_budgets.types.approval_model

        out["ApprovalModel"] = (
            aws_sdk_budgets.types.approval_model.serialize_aws_json_1_1(
                value["approval_model"]
            )
        )
    if "subscribers" in value:
        import aws_sdk_budgets.types.subscribers

        out["Subscribers"] = aws_sdk_budgets.types.subscribers.serialize_aws_json_1_1(
            value["subscribers"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateBudgetActionRequest:
    out: UpdateBudgetActionRequest = {}  # type: ignore[typeddict-item]
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    else:
        raise DeserializationError("UpdateBudgetActionRequest.account_id required")
    if "BudgetName" in data:
        out["budget_name"] = data["BudgetName"]
    else:
        raise DeserializationError("UpdateBudgetActionRequest.budget_name required")
    if "ActionId" in data:
        out["action_id"] = data["ActionId"]
    else:
        raise DeserializationError("UpdateBudgetActionRequest.action_id required")
    if "NotificationType" in data:
        import aws_sdk_budgets.types.notification_type

        out["notification_type"] = (
            aws_sdk_budgets.types.notification_type.deserialize_aws_json_1_1(
                data["NotificationType"]
            )
        )
    if "ActionThreshold" in data:
        import aws_sdk_budgets.types.action_threshold

        out["action_threshold"] = (
            aws_sdk_budgets.types.action_threshold.deserialize_aws_json_1_1(
                data["ActionThreshold"]
            )
        )
    if "Definition" in data:
        import aws_sdk_budgets.types.definition

        out["definition"] = aws_sdk_budgets.types.definition.deserialize_aws_json_1_1(
            data["Definition"]
        )
    if "ExecutionRoleArn" in data:
        out["execution_role_arn"] = data["ExecutionRoleArn"]
    if "ApprovalModel" in data:
        import aws_sdk_budgets.types.approval_model

        out["approval_model"] = (
            aws_sdk_budgets.types.approval_model.deserialize_aws_json_1_1(
                data["ApprovalModel"]
            )
        )
    if "Subscribers" in data:
        import aws_sdk_budgets.types.subscribers

        out["subscribers"] = aws_sdk_budgets.types.subscribers.deserialize_aws_json_1_1(
            data["Subscribers"]
        )
    return out
