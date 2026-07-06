"""Generated from Smithy shape ``com.amazonaws.cleanrooms#PrivacyBudgetSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_cleanrooms.types.collaboration_arn
    import aws_sdk_cleanrooms.types.membership_arn
    import aws_sdk_cleanrooms.types.membership_identifier
    import aws_sdk_cleanrooms.types.privacy_budget
    import aws_sdk_cleanrooms.types.privacy_budget_template_arn
    import aws_sdk_cleanrooms.types.privacy_budget_template_identifier
    import aws_sdk_cleanrooms.types.privacy_budget_type
    import aws_sdk_cleanrooms.types.uuid


class PrivacyBudgetSummary(TypedDict, closed=True):
    id: "aws_sdk_cleanrooms.types.uuid.UUID"
    """<p>The unique identifier of the privacy budget.</p>"""
    privacy_budget_template_id: "aws_sdk_cleanrooms.types.privacy_budget_template_identifier.PrivacyBudgetTemplateIdentifier"
    """<p>The unique identifier of the privacy budget template.</p>"""
    privacy_budget_template_arn: (
        "aws_sdk_cleanrooms.types.privacy_budget_template_arn.PrivacyBudgetTemplateArn"
    )
    """<p>The ARN of the privacy budget template.</p>"""
    membership_id: "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier"
    """<p>The identifier for a membership resource.</p>"""
    membership_arn: "aws_sdk_cleanrooms.types.membership_arn.MembershipArn"
    """<p>The Amazon Resource Name (ARN) of the member who created the privacy budget summary.</p>"""
    collaboration_id: "aws_sdk_cleanrooms.types.uuid.UUID"
    """<p>The unique identifier of the collaboration that contains this privacy budget.</p>"""
    collaboration_arn: "aws_sdk_cleanrooms.types.collaboration_arn.CollaborationArn"
    """<p>The ARN of the collaboration that contains this privacy budget.</p>"""
    type: "aws_sdk_cleanrooms.types.privacy_budget_type.PrivacyBudgetType"
    """<p>Specifies the type of the privacy budget.</p>"""
    create_time: "datetime.datetime"
    """<p>The time at which the privacy budget was created.</p>"""
    update_time: "datetime.datetime"
    """<p>The most recent time at which the privacy budget was updated.</p>"""
    budget: "aws_sdk_cleanrooms.types.privacy_budget.PrivacyBudget"
    """<p>The provided privacy budget.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PrivacyBudgetSummary) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["privacyBudgetTemplateId"] = value["privacy_budget_template_id"]
    out["privacyBudgetTemplateArn"] = value["privacy_budget_template_arn"]
    out["membershipId"] = value["membership_id"]
    out["membershipArn"] = value["membership_arn"]
    out["collaborationId"] = value["collaboration_id"]
    out["collaborationArn"] = value["collaboration_arn"]
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


def deserialize_json(data: dict) -> PrivacyBudgetSummary:
    out: PrivacyBudgetSummary = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("PrivacyBudgetSummary.id required")
    if "privacyBudgetTemplateId" in data:
        out["privacy_budget_template_id"] = data["privacyBudgetTemplateId"]
    else:
        raise DeserializationError(
            "PrivacyBudgetSummary.privacy_budget_template_id required"
        )
    if "privacyBudgetTemplateArn" in data:
        out["privacy_budget_template_arn"] = data["privacyBudgetTemplateArn"]
    else:
        raise DeserializationError(
            "PrivacyBudgetSummary.privacy_budget_template_arn required"
        )
    if "membershipId" in data:
        out["membership_id"] = data["membershipId"]
    else:
        raise DeserializationError("PrivacyBudgetSummary.membership_id required")
    if "membershipArn" in data:
        out["membership_arn"] = data["membershipArn"]
    else:
        raise DeserializationError("PrivacyBudgetSummary.membership_arn required")
    if "collaborationId" in data:
        out["collaboration_id"] = data["collaborationId"]
    else:
        raise DeserializationError("PrivacyBudgetSummary.collaboration_id required")
    if "collaborationArn" in data:
        out["collaboration_arn"] = data["collaborationArn"]
    else:
        raise DeserializationError("PrivacyBudgetSummary.collaboration_arn required")
    if "type" in data:
        import aws_sdk_cleanrooms.types.privacy_budget_type

        out["type"] = aws_sdk_cleanrooms.types.privacy_budget_type.deserialize_json(
            data["type"]
        )
    else:
        raise DeserializationError("PrivacyBudgetSummary.type required")
    if "createTime" in data:
        import aws_sdk_cleanrooms.types._prelude.timestamp

        out["create_time"] = (
            aws_sdk_cleanrooms.types._prelude.timestamp.deserialize_json(
                data["createTime"]
            )
        )
    else:
        raise DeserializationError("PrivacyBudgetSummary.create_time required")
    if "updateTime" in data:
        import aws_sdk_cleanrooms.types._prelude.timestamp

        out["update_time"] = (
            aws_sdk_cleanrooms.types._prelude.timestamp.deserialize_json(
                data["updateTime"]
            )
        )
    else:
        raise DeserializationError("PrivacyBudgetSummary.update_time required")
    if "budget" in data:
        import aws_sdk_cleanrooms.types.privacy_budget

        out["budget"] = aws_sdk_cleanrooms.types.privacy_budget.deserialize_json(
            data["budget"]
        )
    else:
        raise DeserializationError("PrivacyBudgetSummary.budget required")
    return out
