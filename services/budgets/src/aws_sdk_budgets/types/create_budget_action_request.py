"""Generated from Smithy shape ``com.amazonaws.budgets#CreateBudgetActionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_budgets.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_budgets.types.account_id
    import aws_sdk_budgets.types.action_threshold
    import aws_sdk_budgets.types.action_type
    import aws_sdk_budgets.types.approval_model
    import aws_sdk_budgets.types.budget_name
    import aws_sdk_budgets.types.definition
    import aws_sdk_budgets.types.notification_type
    import aws_sdk_budgets.types.resource_tag_list
    import aws_sdk_budgets.types.role_arn
    import aws_sdk_budgets.types.subscribers


class CreateBudgetActionRequest(TypedDict, closed=True):
    account_id: "aws_sdk_budgets.types.account_id.AccountId"
    budget_name: "aws_sdk_budgets.types.budget_name.BudgetName"
    notification_type: "aws_sdk_budgets.types.notification_type.NotificationType"
    action_type: "aws_sdk_budgets.types.action_type.ActionType"
    """<p> The type of action. This defines the type of tasks that can be carried out by this action. This field also determines the format for definition. </p>"""
    action_threshold: "aws_sdk_budgets.types.action_threshold.ActionThreshold"
    definition: "aws_sdk_budgets.types.definition.Definition"
    execution_role_arn: "aws_sdk_budgets.types.role_arn.RoleArn"
    """<p> The role passed for action execution and reversion. Roles and actions must be in the same account. </p>"""
    approval_model: "aws_sdk_budgets.types.approval_model.ApprovalModel"
    """<p> This specifies if the action needs manual or automatic approval. </p>"""
    subscribers: "aws_sdk_budgets.types.subscribers.Subscribers"
    resource_tags: NotRequired[
        "aws_sdk_budgets.types.resource_tag_list.ResourceTagList"
    ]
    """<p>An optional list of tags to associate with the specified budget action. Each tag consists of a key and a value, and each key must be unique for the resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateBudgetActionRequest) -> dict:
    out: dict = {}
    out["AccountId"] = value["account_id"]
    out["BudgetName"] = value["budget_name"]
    import aws_sdk_budgets.types.notification_type

    out["NotificationType"] = (
        aws_sdk_budgets.types.notification_type.serialize_aws_json_1_1(
            value["notification_type"]
        )
    )
    import aws_sdk_budgets.types.action_type

    out["ActionType"] = aws_sdk_budgets.types.action_type.serialize_aws_json_1_1(
        value["action_type"]
    )
    import aws_sdk_budgets.types.action_threshold

    out["ActionThreshold"] = (
        aws_sdk_budgets.types.action_threshold.serialize_aws_json_1_1(
            value["action_threshold"]
        )
    )
    import aws_sdk_budgets.types.definition

    out["Definition"] = aws_sdk_budgets.types.definition.serialize_aws_json_1_1(
        value["definition"]
    )
    out["ExecutionRoleArn"] = value["execution_role_arn"]
    import aws_sdk_budgets.types.approval_model

    out["ApprovalModel"] = aws_sdk_budgets.types.approval_model.serialize_aws_json_1_1(
        value["approval_model"]
    )
    import aws_sdk_budgets.types.subscribers

    out["Subscribers"] = aws_sdk_budgets.types.subscribers.serialize_aws_json_1_1(
        value["subscribers"]
    )
    if "resource_tags" in value:
        import aws_sdk_budgets.types.resource_tag_list

        out["ResourceTags"] = (
            aws_sdk_budgets.types.resource_tag_list.serialize_aws_json_1_1(
                value["resource_tags"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateBudgetActionRequest:
    out: CreateBudgetActionRequest = {}  # type: ignore[typeddict-item]
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    else:
        raise DeserializationError("CreateBudgetActionRequest.account_id required")
    if "BudgetName" in data:
        out["budget_name"] = data["BudgetName"]
    else:
        raise DeserializationError("CreateBudgetActionRequest.budget_name required")
    if "NotificationType" in data:
        import aws_sdk_budgets.types.notification_type

        out["notification_type"] = (
            aws_sdk_budgets.types.notification_type.deserialize_aws_json_1_1(
                data["NotificationType"]
            )
        )
    else:
        raise DeserializationError(
            "CreateBudgetActionRequest.notification_type required"
        )
    if "ActionType" in data:
        import aws_sdk_budgets.types.action_type

        out["action_type"] = aws_sdk_budgets.types.action_type.deserialize_aws_json_1_1(
            data["ActionType"]
        )
    else:
        raise DeserializationError("CreateBudgetActionRequest.action_type required")
    if "ActionThreshold" in data:
        import aws_sdk_budgets.types.action_threshold

        out["action_threshold"] = (
            aws_sdk_budgets.types.action_threshold.deserialize_aws_json_1_1(
                data["ActionThreshold"]
            )
        )
    else:
        raise DeserializationError(
            "CreateBudgetActionRequest.action_threshold required"
        )
    if "Definition" in data:
        import aws_sdk_budgets.types.definition

        out["definition"] = aws_sdk_budgets.types.definition.deserialize_aws_json_1_1(
            data["Definition"]
        )
    else:
        raise DeserializationError("CreateBudgetActionRequest.definition required")
    if "ExecutionRoleArn" in data:
        out["execution_role_arn"] = data["ExecutionRoleArn"]
    else:
        raise DeserializationError(
            "CreateBudgetActionRequest.execution_role_arn required"
        )
    if "ApprovalModel" in data:
        import aws_sdk_budgets.types.approval_model

        out["approval_model"] = (
            aws_sdk_budgets.types.approval_model.deserialize_aws_json_1_1(
                data["ApprovalModel"]
            )
        )
    else:
        raise DeserializationError("CreateBudgetActionRequest.approval_model required")
    if "Subscribers" in data:
        import aws_sdk_budgets.types.subscribers

        out["subscribers"] = aws_sdk_budgets.types.subscribers.deserialize_aws_json_1_1(
            data["Subscribers"]
        )
    else:
        raise DeserializationError("CreateBudgetActionRequest.subscribers required")
    if "ResourceTags" in data:
        import aws_sdk_budgets.types.resource_tag_list

        out["resource_tags"] = (
            aws_sdk_budgets.types.resource_tag_list.deserialize_aws_json_1_1(
                data["ResourceTags"]
            )
        )
    return out
