"""Generated from Smithy shape ``com.amazonaws.securityir#ListCasesItem``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_security_ir.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_security_ir.types.case_arn
    import aws_sdk_security_ir.types.case_id
    import aws_sdk_security_ir.types.case_status
    import aws_sdk_security_ir.types.case_title
    import aws_sdk_security_ir.types.engagement_type
    import aws_sdk_security_ir.types.pending_action
    import aws_sdk_security_ir.types.resolver_type


class ListCasesItem(TypedDict):
    case_id: "aws_sdk_security_ir.types.case_id.CaseId"
    """<p/>"""
    last_updated_date: NotRequired["datetime.datetime"]
    """<p/>"""
    title: NotRequired["aws_sdk_security_ir.types.case_title.CaseTitle"]
    """<p/>"""
    case_arn: NotRequired["aws_sdk_security_ir.types.case_arn.CaseArn"]
    """<p/>"""
    engagement_type: NotRequired[
        "aws_sdk_security_ir.types.engagement_type.EngagementType"
    ]
    """<p/>"""
    case_status: NotRequired["aws_sdk_security_ir.types.case_status.CaseStatus"]
    """<p/>"""
    created_date: NotRequired["datetime.datetime"]
    """<p/>"""
    closed_date: NotRequired["datetime.datetime"]
    """<p/>"""
    resolver_type: NotRequired["aws_sdk_security_ir.types.resolver_type.ResolverType"]
    """<p/>"""
    pending_action: NotRequired[
        "aws_sdk_security_ir.types.pending_action.PendingAction"
    ]
    """<p/>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCasesItem) -> dict:
    out: dict = {}
    out["caseId"] = value["case_id"]
    if "last_updated_date" in value:
        import aws_sdk_security_ir.types._prelude.timestamp

        out["lastUpdatedDate"] = (
            aws_sdk_security_ir.types._prelude.timestamp.serialize_json(
                value["last_updated_date"]
            )
        )
    if "title" in value:
        out["title"] = value["title"]
    if "case_arn" in value:
        out["caseArn"] = value["case_arn"]
    if "engagement_type" in value:
        import aws_sdk_security_ir.types.engagement_type

        out["engagementType"] = (
            aws_sdk_security_ir.types.engagement_type.serialize_json(
                value["engagement_type"]
            )
        )
    if "case_status" in value:
        import aws_sdk_security_ir.types.case_status

        out["caseStatus"] = aws_sdk_security_ir.types.case_status.serialize_json(
            value["case_status"]
        )
    if "created_date" in value:
        import aws_sdk_security_ir.types._prelude.timestamp

        out["createdDate"] = (
            aws_sdk_security_ir.types._prelude.timestamp.serialize_json(
                value["created_date"]
            )
        )
    if "closed_date" in value:
        import aws_sdk_security_ir.types._prelude.timestamp

        out["closedDate"] = aws_sdk_security_ir.types._prelude.timestamp.serialize_json(
            value["closed_date"]
        )
    if "resolver_type" in value:
        import aws_sdk_security_ir.types.resolver_type

        out["resolverType"] = aws_sdk_security_ir.types.resolver_type.serialize_json(
            value["resolver_type"]
        )
    if "pending_action" in value:
        import aws_sdk_security_ir.types.pending_action

        out["pendingAction"] = aws_sdk_security_ir.types.pending_action.serialize_json(
            value["pending_action"]
        )
    return out


def deserialize_json(data: dict) -> ListCasesItem:
    out: ListCasesItem = {}  # type: ignore[typeddict-item]
    if "caseId" in data:
        out["case_id"] = data["caseId"]
    else:
        raise DeserializationError("ListCasesItem.case_id required")
    if "lastUpdatedDate" in data:
        import aws_sdk_security_ir.types._prelude.timestamp

        out["last_updated_date"] = (
            aws_sdk_security_ir.types._prelude.timestamp.deserialize_json(
                data["lastUpdatedDate"]
            )
        )
    if "title" in data:
        out["title"] = data["title"]
    if "caseArn" in data:
        out["case_arn"] = data["caseArn"]
    if "engagementType" in data:
        import aws_sdk_security_ir.types.engagement_type

        out["engagement_type"] = (
            aws_sdk_security_ir.types.engagement_type.deserialize_json(
                data["engagementType"]
            )
        )
    if "caseStatus" in data:
        import aws_sdk_security_ir.types.case_status

        out["case_status"] = aws_sdk_security_ir.types.case_status.deserialize_json(
            data["caseStatus"]
        )
    if "createdDate" in data:
        import aws_sdk_security_ir.types._prelude.timestamp

        out["created_date"] = (
            aws_sdk_security_ir.types._prelude.timestamp.deserialize_json(
                data["createdDate"]
            )
        )
    if "closedDate" in data:
        import aws_sdk_security_ir.types._prelude.timestamp

        out["closed_date"] = (
            aws_sdk_security_ir.types._prelude.timestamp.deserialize_json(
                data["closedDate"]
            )
        )
    if "resolverType" in data:
        import aws_sdk_security_ir.types.resolver_type

        out["resolver_type"] = aws_sdk_security_ir.types.resolver_type.deserialize_json(
            data["resolverType"]
        )
    if "pendingAction" in data:
        import aws_sdk_security_ir.types.pending_action

        out["pending_action"] = (
            aws_sdk_security_ir.types.pending_action.deserialize_json(
                data["pendingAction"]
            )
        )
    return out
