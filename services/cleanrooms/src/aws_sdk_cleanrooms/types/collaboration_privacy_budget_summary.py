"""Generated from Smithy shape ``com.amazonaws.cleanrooms#CollaborationPrivacyBudgetSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_cleanrooms.types.account_id
    import aws_sdk_cleanrooms.types.collaboration_arn
    import aws_sdk_cleanrooms.types.privacy_budget
    import aws_sdk_cleanrooms.types.privacy_budget_template_arn
    import aws_sdk_cleanrooms.types.privacy_budget_template_identifier
    import aws_sdk_cleanrooms.types.privacy_budget_type
    import aws_sdk_cleanrooms.types.uuid


class CollaborationPrivacyBudgetSummary(TypedDict, closed=True):
    id: "aws_sdk_cleanrooms.types.uuid.UUID"
    """<p>The unique identifier of the collaboration privacy budget.</p>"""
    privacy_budget_template_id: "aws_sdk_cleanrooms.types.privacy_budget_template_identifier.PrivacyBudgetTemplateIdentifier"
    """<p>The unique identifier of the collaboration privacy budget template.</p>"""
    privacy_budget_template_arn: (
        "aws_sdk_cleanrooms.types.privacy_budget_template_arn.PrivacyBudgetTemplateArn"
    )
    """<p>The ARN of the collaboration privacy budget template.</p>"""
    collaboration_id: "aws_sdk_cleanrooms.types.uuid.UUID"
    """<p>The unique identifier of the collaboration that includes this privacy budget.</p>"""
    collaboration_arn: "aws_sdk_cleanrooms.types.collaboration_arn.CollaborationArn"
    """<p>The ARN of the collaboration that includes this privacy budget.</p>"""
    creator_account_id: "aws_sdk_cleanrooms.types.account_id.AccountId"
    """<p>The unique identifier of the account that created this privacy budget.</p>"""
    type: "aws_sdk_cleanrooms.types.privacy_budget_type.PrivacyBudgetType"
    """<p>The type of privacy budget template.</p>"""
    create_time: "datetime.datetime"
    """<p>The time at which the privacy budget was created.</p>"""
    update_time: "datetime.datetime"
    """<p>The most recent time at which the privacy budget was updated.</p>"""
    budget: "aws_sdk_cleanrooms.types.privacy_budget.PrivacyBudget"
    """<p>The includes epsilon provided and utility in terms of aggregations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CollaborationPrivacyBudgetSummary) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["privacyBudgetTemplateId"] = value["privacy_budget_template_id"]
    out["privacyBudgetTemplateArn"] = value["privacy_budget_template_arn"]
    out["collaborationId"] = value["collaboration_id"]
    out["collaborationArn"] = value["collaboration_arn"]
    out["creatorAccountId"] = value["creator_account_id"]
    import aws_sdk_cleanrooms.types.privacy_budget_type

    out["type"] = aws_sdk_cleanrooms.types.privacy_budget_type.serialize_json(
        value["type"]
    )
    import aws_sdk_cleanrooms.types._prelude.timestamp

    out["createTime"] = aws_sdk_cleanrooms.types._prelude.timestamp.serialize_json(
        value["create_time"]
    )
    import aws_sdk_cleanrooms.types._prelude.timestamp

    out["updateTime"] = aws_sdk_cleanrooms.types._prelude.timestamp.serialize_json(
        value["update_time"]
    )
    import aws_sdk_cleanrooms.types.privacy_budget

    out["budget"] = aws_sdk_cleanrooms.types.privacy_budget.serialize_json(
        value["budget"]
    )
    return out


def deserialize_json(data: dict) -> CollaborationPrivacyBudgetSummary:
    out: CollaborationPrivacyBudgetSummary = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("CollaborationPrivacyBudgetSummary.id required")
    if "privacyBudgetTemplateId" in data:
        out["privacy_budget_template_id"] = data["privacyBudgetTemplateId"]
    else:
        raise DeserializationError(
            "CollaborationPrivacyBudgetSummary.privacy_budget_template_id required"
        )
    if "privacyBudgetTemplateArn" in data:
        out["privacy_budget_template_arn"] = data["privacyBudgetTemplateArn"]
    else:
        raise DeserializationError(
            "CollaborationPrivacyBudgetSummary.privacy_budget_template_arn required"
        )
    if "collaborationId" in data:
        out["collaboration_id"] = data["collaborationId"]
    else:
        raise DeserializationError(
            "CollaborationPrivacyBudgetSummary.collaboration_id required"
        )
    if "collaborationArn" in data:
        out["collaboration_arn"] = data["collaborationArn"]
    else:
        raise DeserializationError(
            "CollaborationPrivacyBudgetSummary.collaboration_arn required"
        )
    if "creatorAccountId" in data:
        out["creator_account_id"] = data["creatorAccountId"]
    else:
        raise DeserializationError(
            "CollaborationPrivacyBudgetSummary.creator_account_id required"
        )
    if "type" in data:
        import aws_sdk_cleanrooms.types.privacy_budget_type

        out["type"] = aws_sdk_cleanrooms.types.privacy_budget_type.deserialize_json(
            data["type"]
        )
    else:
        raise DeserializationError("CollaborationPrivacyBudgetSummary.type required")
    if "createTime" in data:
        import aws_sdk_cleanrooms.types._prelude.timestamp

        out["create_time"] = (
            aws_sdk_cleanrooms.types._prelude.timestamp.deserialize_json(
                data["createTime"]
            )
        )
    else:
        raise DeserializationError(
            "CollaborationPrivacyBudgetSummary.create_time required"
        )
    if "updateTime" in data:
        import aws_sdk_cleanrooms.types._prelude.timestamp

        out["update_time"] = (
            aws_sdk_cleanrooms.types._prelude.timestamp.deserialize_json(
                data["updateTime"]
            )
        )
    else:
        raise DeserializationError(
            "CollaborationPrivacyBudgetSummary.update_time required"
        )
    if "budget" in data:
        import aws_sdk_cleanrooms.types.privacy_budget

        out["budget"] = aws_sdk_cleanrooms.types.privacy_budget.deserialize_json(
            data["budget"]
        )
    else:
        raise DeserializationError("CollaborationPrivacyBudgetSummary.budget required")
    return out
