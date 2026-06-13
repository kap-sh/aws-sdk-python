"""Generated from Smithy shape ``com.amazonaws.cleanrooms#CollaborationPrivacyBudgetTemplate``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_cleanrooms.types.account_id
    import aws_sdk_cleanrooms.types.collaboration_arn
    import aws_sdk_cleanrooms.types.privacy_budget_template_arn
    import aws_sdk_cleanrooms.types.privacy_budget_template_auto_refresh
    import aws_sdk_cleanrooms.types.privacy_budget_template_identifier
    import aws_sdk_cleanrooms.types.privacy_budget_template_parameters_output
    import aws_sdk_cleanrooms.types.privacy_budget_type
    import aws_sdk_cleanrooms.types.uuid


class CollaborationPrivacyBudgetTemplate(TypedDict):
    id: "aws_sdk_cleanrooms.types.privacy_budget_template_identifier.PrivacyBudgetTemplateIdentifier"
    """<p>The unique identifier of the collaboration privacy budget template.</p>"""
    arn: "aws_sdk_cleanrooms.types.privacy_budget_template_arn.PrivacyBudgetTemplateArn"
    """<p>The ARN of the collaboration privacy budget template.</p>"""
    collaboration_id: "aws_sdk_cleanrooms.types.uuid.UUID"
    """<p>The unique identifier of the collaboration that includes this collaboration privacy budget template.</p>"""
    collaboration_arn: "aws_sdk_cleanrooms.types.collaboration_arn.CollaborationArn"
    """<p>The ARN of the collaboration that includes this collaboration privacy budget template.</p>"""
    creator_account_id: "aws_sdk_cleanrooms.types.account_id.AccountId"
    """<p>The unique identifier of the account that created this collaboration privacy budget template.</p>"""
    create_time: "datetime.datetime"
    """<p>The time at which the collaboration privacy budget template was created.</p>"""
    update_time: "datetime.datetime"
    """<p>The most recent time at which the collaboration privacy budget template was updated.</p>"""
    privacy_budget_type: (
        "aws_sdk_cleanrooms.types.privacy_budget_type.PrivacyBudgetType"
    )
    """<p>The type of privacy budget template.</p>"""
    auto_refresh: "aws_sdk_cleanrooms.types.privacy_budget_template_auto_refresh.PrivacyBudgetTemplateAutoRefresh"
    """<p>How often the privacy budget refreshes.</p> <important> <p>If you plan to regularly bring new data into the collaboration, use <code>CALENDAR_MONTH</code> to automatically get a new privacy budget for the collaboration every calendar month. Choosing this option allows arbitrary amounts of information to be revealed about rows of the data when repeatedly queried across refreshes. Avoid choosing this if the same rows will be repeatedly queried between privacy budget refreshes.</p> </important>"""
    parameters: "aws_sdk_cleanrooms.types.privacy_budget_template_parameters_output.PrivacyBudgetTemplateParametersOutput"
    """<p>Specifies the epsilon and noise parameters for the privacy budget template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CollaborationPrivacyBudgetTemplate) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    out["collaborationId"] = value["collaboration_id"]
    out["collaborationArn"] = value["collaboration_arn"]
    out["creatorAccountId"] = value["creator_account_id"]
    import aws_sdk_cleanrooms.types._prelude.timestamp

    out["createTime"] = aws_sdk_cleanrooms.types._prelude.timestamp.serialize_json(
        value["create_time"]
    )
    import aws_sdk_cleanrooms.types._prelude.timestamp

    out["updateTime"] = aws_sdk_cleanrooms.types._prelude.timestamp.serialize_json(
        value["update_time"]
    )
    import aws_sdk_cleanrooms.types.privacy_budget_type

    out["privacyBudgetType"] = (
        aws_sdk_cleanrooms.types.privacy_budget_type.serialize_json(
            value["privacy_budget_type"]
        )
    )
    import aws_sdk_cleanrooms.types.privacy_budget_template_auto_refresh

    out["autoRefresh"] = (
        aws_sdk_cleanrooms.types.privacy_budget_template_auto_refresh.serialize_json(
            value["auto_refresh"]
        )
    )
    import aws_sdk_cleanrooms.types.privacy_budget_template_parameters_output

    out["parameters"] = (
        aws_sdk_cleanrooms.types.privacy_budget_template_parameters_output.serialize_json(
            value["parameters"]
        )
    )
    return out


def deserialize_json(data: dict) -> CollaborationPrivacyBudgetTemplate:
    out: CollaborationPrivacyBudgetTemplate = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("CollaborationPrivacyBudgetTemplate.id required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("CollaborationPrivacyBudgetTemplate.arn required")
    if "collaborationId" in data:
        out["collaboration_id"] = data["collaborationId"]
    else:
        raise DeserializationError(
            "CollaborationPrivacyBudgetTemplate.collaboration_id required"
        )
    if "collaborationArn" in data:
        out["collaboration_arn"] = data["collaborationArn"]
    else:
        raise DeserializationError(
            "CollaborationPrivacyBudgetTemplate.collaboration_arn required"
        )
    if "creatorAccountId" in data:
        out["creator_account_id"] = data["creatorAccountId"]
    else:
        raise DeserializationError(
            "CollaborationPrivacyBudgetTemplate.creator_account_id required"
        )
    if "createTime" in data:
        import aws_sdk_cleanrooms.types._prelude.timestamp

        out["create_time"] = (
            aws_sdk_cleanrooms.types._prelude.timestamp.deserialize_json(
                data["createTime"]
            )
        )
    else:
        raise DeserializationError(
            "CollaborationPrivacyBudgetTemplate.create_time required"
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
            "CollaborationPrivacyBudgetTemplate.update_time required"
        )
    if "privacyBudgetType" in data:
        import aws_sdk_cleanrooms.types.privacy_budget_type

        out["privacy_budget_type"] = (
            aws_sdk_cleanrooms.types.privacy_budget_type.deserialize_json(
                data["privacyBudgetType"]
            )
        )
    else:
        raise DeserializationError(
            "CollaborationPrivacyBudgetTemplate.privacy_budget_type required"
        )
    if "autoRefresh" in data:
        import aws_sdk_cleanrooms.types.privacy_budget_template_auto_refresh

        out["auto_refresh"] = (
            aws_sdk_cleanrooms.types.privacy_budget_template_auto_refresh.deserialize_json(
                data["autoRefresh"]
            )
        )
    else:
        raise DeserializationError(
            "CollaborationPrivacyBudgetTemplate.auto_refresh required"
        )
    if "parameters" in data:
        import aws_sdk_cleanrooms.types.privacy_budget_template_parameters_output

        out["parameters"] = (
            aws_sdk_cleanrooms.types.privacy_budget_template_parameters_output.deserialize_json(
                data["parameters"]
            )
        )
    else:
        raise DeserializationError(
            "CollaborationPrivacyBudgetTemplate.parameters required"
        )
    return out
