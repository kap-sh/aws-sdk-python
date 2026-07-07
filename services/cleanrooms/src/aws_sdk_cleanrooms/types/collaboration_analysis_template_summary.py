"""Generated from Smithy shape ``com.amazonaws.cleanrooms#CollaborationAnalysisTemplateSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_cleanrooms.types.account_id
    import aws_sdk_cleanrooms.types.analysis_template_arn
    import aws_sdk_cleanrooms.types.analysis_template_identifier
    import aws_sdk_cleanrooms.types.collaboration_arn
    import aws_sdk_cleanrooms.types.resource_alias
    import aws_sdk_cleanrooms.types.resource_description
    import aws_sdk_cleanrooms.types.uuid


class CollaborationAnalysisTemplateSummary(TypedDict, closed=True):
    arn: "aws_sdk_cleanrooms.types.analysis_template_arn.AnalysisTemplateArn"
    """<p>The Amazon Resource Name (ARN) of the analysis template.</p>"""
    create_time: "datetime.datetime"
    """<p>The time that the summary of the analysis template in a collaboration was created.</p>"""
    id: "aws_sdk_cleanrooms.types.analysis_template_identifier.AnalysisTemplateIdentifier"
    """<p>The identifier of the analysis template.</p>"""
    name: "aws_sdk_cleanrooms.types.resource_alias.ResourceAlias"
    """<p>The name of the analysis template.</p>"""
    update_time: "datetime.datetime"
    """<p>The time that the summary of the analysis template in the collaboration was last updated.</p>"""
    collaboration_arn: "aws_sdk_cleanrooms.types.collaboration_arn.CollaborationArn"
    """<p>The unique ARN for the analysis template’s associated collaboration.</p>"""
    collaboration_id: "aws_sdk_cleanrooms.types.uuid.UUID"
    """<p>A unique identifier for the collaboration that the analysis templates belong to. Currently accepts collaboration ID.</p>"""
    creator_account_id: "aws_sdk_cleanrooms.types.account_id.AccountId"
    """<p>The identifier used to reference members of the collaboration. Currently only supports Amazon Web Services account ID.</p>"""
    description: NotRequired[
        "aws_sdk_cleanrooms.types.resource_description.ResourceDescription"
    ]
    """<p>The description of the analysis template.</p>"""
    is_synthetic_data: NotRequired["bool"]
    """<p>Indicates if this collaboration analysis template uses synthetic data generation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CollaborationAnalysisTemplateSummary) -> dict:
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
    out["collaborationArn"] = value["collaboration_arn"]
    out["collaborationId"] = value["collaboration_id"]
    out["creatorAccountId"] = value["creator_account_id"]
    if "description" in value:
        out["description"] = value["description"]
    if "is_synthetic_data" in value:
        out["isSyntheticData"] = value["is_synthetic_data"]
    return out


def deserialize_json(data: dict) -> CollaborationAnalysisTemplateSummary:
    out: CollaborationAnalysisTemplateSummary = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("CollaborationAnalysisTemplateSummary.arn required")
    if "createTime" in data:
        import aws_sdk_cleanrooms.types._prelude.timestamp

        out["create_time"] = (
            aws_sdk_cleanrooms.types._prelude.timestamp.deserialize_json(
                data["createTime"]
            )
        )
    else:
        raise DeserializationError(
            "CollaborationAnalysisTemplateSummary.create_time required"
        )
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("CollaborationAnalysisTemplateSummary.id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CollaborationAnalysisTemplateSummary.name required")
    if "updateTime" in data:
        import aws_sdk_cleanrooms.types._prelude.timestamp

        out["update_time"] = (
            aws_sdk_cleanrooms.types._prelude.timestamp.deserialize_json(
                data["updateTime"]
            )
        )
    else:
        raise DeserializationError(
            "CollaborationAnalysisTemplateSummary.update_time required"
        )
    if "collaborationArn" in data:
        out["collaboration_arn"] = data["collaborationArn"]
    else:
        raise DeserializationError(
            "CollaborationAnalysisTemplateSummary.collaboration_arn required"
        )
    if "collaborationId" in data:
        out["collaboration_id"] = data["collaborationId"]
    else:
        raise DeserializationError(
            "CollaborationAnalysisTemplateSummary.collaboration_id required"
        )
    if "creatorAccountId" in data:
        out["creator_account_id"] = data["creatorAccountId"]
    else:
        raise DeserializationError(
            "CollaborationAnalysisTemplateSummary.creator_account_id required"
        )
    if "description" in data:
        out["description"] = data["description"]
    if "isSyntheticData" in data:
        out["is_synthetic_data"] = data["isSyntheticData"]
    return out
