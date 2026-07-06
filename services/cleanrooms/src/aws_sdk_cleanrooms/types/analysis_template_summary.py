"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AnalysisTemplateSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_cleanrooms.types.analysis_template_arn
    import aws_sdk_cleanrooms.types.analysis_template_identifier
    import aws_sdk_cleanrooms.types.collaboration_arn
    import aws_sdk_cleanrooms.types.membership_arn
    import aws_sdk_cleanrooms.types.resource_alias
    import aws_sdk_cleanrooms.types.resource_description
    import aws_sdk_cleanrooms.types.uuid


class AnalysisTemplateSummary(TypedDict, closed=True):
    arn: "aws_sdk_cleanrooms.types.analysis_template_arn.AnalysisTemplateArn"
    """<p>The Amazon Resource Name (ARN) of the analysis template.</p>"""
    create_time: "datetime.datetime"
    """<p>The time that the analysis template summary was created.</p>"""
    id: "aws_sdk_cleanrooms.types.analysis_template_identifier.AnalysisTemplateIdentifier"
    """<p>The identifier of the analysis template.</p>"""
    name: "aws_sdk_cleanrooms.types.resource_alias.ResourceAlias"
    """<p>The name of the analysis template. </p>"""
    update_time: "datetime.datetime"
    """<p>The time that the analysis template summary was last updated.</p>"""
    membership_arn: "aws_sdk_cleanrooms.types.membership_arn.MembershipArn"
    """<p>The Amazon Resource Name (ARN) of the member who created the analysis template.</p>"""
    membership_id: "aws_sdk_cleanrooms.types.uuid.UUID"
    """<p>The identifier for a membership resource.</p>"""
    collaboration_arn: "aws_sdk_cleanrooms.types.collaboration_arn.CollaborationArn"
    """<p>The unique ARN for the analysis template summary’s associated collaboration.</p>"""
    collaboration_id: "aws_sdk_cleanrooms.types.uuid.UUID"
    """<p>A unique identifier for the collaboration that the analysis template summary belongs to. Currently accepts collaboration ID.</p>"""
    description: NotRequired[
        "aws_sdk_cleanrooms.types.resource_description.ResourceDescription"
    ]
    """<p>The description of the analysis template.</p>"""
    is_synthetic_data: NotRequired["bool"]
    """<p>Indicates if this analysis template summary generated synthetic data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnalysisTemplateSummary) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    import aws_sdk_cleanrooms.types._prelude.timestamp

    out["createTime"] = aws_sdk_cleanrooms.types._prelude.timestamp.serialize_json(
        value["create_time"]
    )
    out["id"] = value["id"]
    out["name"] = value["name"]
    import aws_sdk_cleanrooms.types._prelude.timestamp

    out["updateTime"] = aws_sdk_cleanrooms.types._prelude.timestamp.serialize_json(
        value["update_time"]
    )
    out["membershipArn"] = value["membership_arn"]
    out["membershipId"] = value["membership_id"]
    out["collaborationArn"] = value["collaboration_arn"]
    out["collaborationId"] = value["collaboration_id"]
    if "description" in value:
        out["description"] = value["description"]
    if "is_synthetic_data" in value:
        out["isSyntheticData"] = value["is_synthetic_data"]
    return out


def deserialize_json(data: dict) -> AnalysisTemplateSummary:
    out: AnalysisTemplateSummary = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("AnalysisTemplateSummary.arn required")
    if "createTime" in data:
        import aws_sdk_cleanrooms.types._prelude.timestamp

        out["create_time"] = (
            aws_sdk_cleanrooms.types._prelude.timestamp.deserialize_json(
                data["createTime"]
            )
        )
    else:
        raise DeserializationError("AnalysisTemplateSummary.create_time required")
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("AnalysisTemplateSummary.id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("AnalysisTemplateSummary.name required")
    if "updateTime" in data:
        import aws_sdk_cleanrooms.types._prelude.timestamp

        out["update_time"] = (
            aws_sdk_cleanrooms.types._prelude.timestamp.deserialize_json(
                data["updateTime"]
            )
        )
    else:
        raise DeserializationError("AnalysisTemplateSummary.update_time required")
    if "membershipArn" in data:
        out["membership_arn"] = data["membershipArn"]
    else:
        raise DeserializationError("AnalysisTemplateSummary.membership_arn required")
    if "membershipId" in data:
        out["membership_id"] = data["membershipId"]
    else:
        raise DeserializationError("AnalysisTemplateSummary.membership_id required")
    if "collaborationArn" in data:
        out["collaboration_arn"] = data["collaborationArn"]
    else:
        raise DeserializationError("AnalysisTemplateSummary.collaboration_arn required")
    if "collaborationId" in data:
        out["collaboration_id"] = data["collaborationId"]
    else:
        raise DeserializationError("AnalysisTemplateSummary.collaboration_id required")
    if "description" in data:
        out["description"] = data["description"]
    if "isSyntheticData" in data:
        out["is_synthetic_data"] = data["isSyntheticData"]
    return out
