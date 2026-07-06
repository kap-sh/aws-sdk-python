"""Generated from Smithy shape ``com.amazonaws.cleanrooms#PrivacyBudgetTemplate``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_cleanrooms.types.collaboration_arn
    import aws_sdk_cleanrooms.types.membership_arn
    import aws_sdk_cleanrooms.types.privacy_budget_template_arn
    import aws_sdk_cleanrooms.types.privacy_budget_template_auto_refresh
    import aws_sdk_cleanrooms.types.privacy_budget_template_identifier
    import aws_sdk_cleanrooms.types.privacy_budget_template_parameters_output
    import aws_sdk_cleanrooms.types.privacy_budget_type
    import aws_sdk_cleanrooms.types.uuid


class PrivacyBudgetTemplate(TypedDict, closed=True):
    id: "aws_sdk_cleanrooms.types.privacy_budget_template_identifier.PrivacyBudgetTemplateIdentifier"
    """<p>The unique identifier of the privacy budget template.</p>"""
    arn: "aws_sdk_cleanrooms.types.privacy_budget_template_arn.PrivacyBudgetTemplateArn"
    """<p>The ARN of the privacy budget template.</p>"""
    membership_id: "aws_sdk_cleanrooms.types.uuid.UUID"
    """<p>The identifier for a membership resource.</p>"""
    membership_arn: "aws_sdk_cleanrooms.types.membership_arn.MembershipArn"
    """<p>The Amazon Resource Name (ARN) of the member who created the privacy budget template.</p>"""
    collaboration_id: "aws_sdk_cleanrooms.types.uuid.UUID"
    """<p>The unique ID of the collaboration that contains this privacy budget template.</p>"""
    collaboration_arn: "aws_sdk_cleanrooms.types.collaboration_arn.CollaborationArn"
    """<p>The ARN of the collaboration that contains this privacy budget template.</p>"""
    create_time: "datetime.datetime"
    """<p>The time at which the privacy budget template was created.</p>"""
    update_time: "datetime.datetime"
    """<p>The most recent time at which the privacy budget template was updated.</p>"""
    privacy_budget_type: (
        "aws_sdk_cleanrooms.types.privacy_budget_type.PrivacyBudgetType"
    )
    """<p>Specifies the type of the privacy budget template.</p>"""
    auto_refresh: "aws_sdk_cleanrooms.types.privacy_budget_template_auto_refresh.PrivacyBudgetTemplateAutoRefresh"
    """<p>How often the privacy budget refreshes.</p> <important> <p>If you plan to regularly bring new data into the collaboration, use <code>CALENDAR_MONTH</code> to automatically get a new privacy budget for the collaboration every calendar month. Choosing this option allows arbitrary amounts of information to be revealed about rows of the data when repeatedly queried across refreshes. Avoid choosing this if the same rows will be repeatedly queried between privacy budget refreshes.</p> </important>"""
    parameters: "aws_sdk_cleanrooms.types.privacy_budget_template_parameters_output.PrivacyBudgetTemplateParametersOutput"
    """<p>Specifies the epsilon and noise parameters for the privacy budget template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PrivacyBudgetTemplate) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    out["membershipId"] = value["membership_id"]
    out["membershipArn"] = value["membership_arn"]
    out["collaborationId"] = value["collaboration_id"]
    out["collaborationArn"] = value["collaboration_arn"]
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


def deserialize_json(data: dict) -> PrivacyBudgetTemplate:
    out: PrivacyBudgetTemplate = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("PrivacyBudgetTemplate.id required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("PrivacyBudgetTemplate.arn required")
    if "membershipId" in data:
        out["membership_id"] = data["membershipId"]
    else:
        raise DeserializationError("PrivacyBudgetTemplate.membership_id required")
    if "membershipArn" in data:
        out["membership_arn"] = data["membershipArn"]
    else:
        raise DeserializationError("PrivacyBudgetTemplate.membership_arn required")
    if "collaborationId" in data:
        out["collaboration_id"] = data["collaborationId"]
    else:
        raise DeserializationError("PrivacyBudgetTemplate.collaboration_id required")
    if "collaborationArn" in data:
        out["collaboration_arn"] = data["collaborationArn"]
    else:
        raise DeserializationError("PrivacyBudgetTemplate.collaboration_arn required")
    if "createTime" in data:
        import aws_sdk_cleanrooms.types._prelude.timestamp

        out["create_time"] = (
            aws_sdk_cleanrooms.types._prelude.timestamp.deserialize_json(
                data["createTime"]
            )
        )
    else:
        raise DeserializationError("PrivacyBudgetTemplate.create_time required")
    if "updateTime" in data:
        import aws_sdk_cleanrooms.types._prelude.timestamp

        out["update_time"] = (
            aws_sdk_cleanrooms.types._prelude.timestamp.deserialize_json(
                data["updateTime"]
            )
        )
    else:
        raise DeserializationError("PrivacyBudgetTemplate.update_time required")
    if "privacyBudgetType" in data:
        import aws_sdk_cleanrooms.types.privacy_budget_type

        out["privacy_budget_type"] = (
            aws_sdk_cleanrooms.types.privacy_budget_type.deserialize_json(
                data["privacyBudgetType"]
            )
        )
    else:
        raise DeserializationError("PrivacyBudgetTemplate.privacy_budget_type required")
    if "autoRefresh" in data:
        import aws_sdk_cleanrooms.types.privacy_budget_template_auto_refresh

        out["auto_refresh"] = (
            aws_sdk_cleanrooms.types.privacy_budget_template_auto_refresh.deserialize_json(
                data["autoRefresh"]
            )
        )
    else:
        raise DeserializationError("PrivacyBudgetTemplate.auto_refresh required")
    if "parameters" in data:
        import aws_sdk_cleanrooms.types.privacy_budget_template_parameters_output

        out["parameters"] = (
            aws_sdk_cleanrooms.types.privacy_budget_template_parameters_output.deserialize_json(
                data["parameters"]
            )
        )
    else:
        raise DeserializationError("PrivacyBudgetTemplate.parameters required")
    return out
