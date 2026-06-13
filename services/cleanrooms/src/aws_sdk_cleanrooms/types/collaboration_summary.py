"""Generated from Smithy shape ``com.amazonaws.cleanrooms#CollaborationSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_cleanrooms.types.account_id
    import aws_sdk_cleanrooms.types.analytics_engine
    import aws_sdk_cleanrooms.types.collaboration_arn
    import aws_sdk_cleanrooms.types.collaboration_name
    import aws_sdk_cleanrooms.types.display_name
    import aws_sdk_cleanrooms.types.member_status
    import aws_sdk_cleanrooms.types.membership_arn
    import aws_sdk_cleanrooms.types.uuid


class CollaborationSummary(TypedDict):
    id: "aws_sdk_cleanrooms.types.uuid.UUID"
    """<p>The identifier for the collaboration.</p>"""
    arn: "aws_sdk_cleanrooms.types.collaboration_arn.CollaborationArn"
    """<p>The ARN of the collaboration.</p>"""
    name: "aws_sdk_cleanrooms.types.collaboration_name.CollaborationName"
    """<p>A human-readable identifier provided by the collaboration owner. Display names are not unique.</p>"""
    creator_account_id: "aws_sdk_cleanrooms.types.account_id.AccountId"
    """<p>The identifier used to reference members of the collaboration. Currently only supports Amazon Web Services account ID.</p>"""
    creator_display_name: "aws_sdk_cleanrooms.types.display_name.DisplayName"
    """<p>The display name of the collaboration creator.</p>"""
    create_time: "datetime.datetime"
    """<p>The time when the collaboration was created.</p>"""
    update_time: "datetime.datetime"
    """<p>The time the collaboration metadata was last updated.</p>"""
    member_status: "aws_sdk_cleanrooms.types.member_status.MemberStatus"
    """<p>The status of a member in a collaboration.</p>"""
    membership_id: NotRequired["aws_sdk_cleanrooms.types.uuid.UUID"]
    """<p>The identifier of a member in a collaboration.</p>"""
    membership_arn: NotRequired["aws_sdk_cleanrooms.types.membership_arn.MembershipArn"]
    """<p>The ARN of a member in a collaboration.</p>"""
    analytics_engine: NotRequired[
        "aws_sdk_cleanrooms.types.analytics_engine.AnalyticsEngine"
    ]
    """<p> The analytics engine.</p> <note> <p>After July 16, 2025, the <code>CLEAN_ROOMS_SQL</code> parameter will no longer be available. </p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: CollaborationSummary) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    out["name"] = value["name"]
    out["creatorAccountId"] = value["creator_account_id"]
    out["creatorDisplayName"] = value["creator_display_name"]
    import aws_sdk_cleanrooms.types._prelude.timestamp

    out["createTime"] = aws_sdk_cleanrooms.types._prelude.timestamp.serialize_json(
        value["create_time"]
    )
    import aws_sdk_cleanrooms.types._prelude.timestamp

    out["updateTime"] = aws_sdk_cleanrooms.types._prelude.timestamp.serialize_json(
        value["update_time"]
    )
    out["memberStatus"] = value["member_status"]
    if "membership_id" in value:
        out["membershipId"] = value["membership_id"]
    if "membership_arn" in value:
        out["membershipArn"] = value["membership_arn"]
    if "analytics_engine" in value:
        import aws_sdk_cleanrooms.types.analytics_engine

        out["analyticsEngine"] = (
            aws_sdk_cleanrooms.types.analytics_engine.serialize_json(
                value["analytics_engine"]
            )
        )
    return out


def deserialize_json(data: dict) -> CollaborationSummary:
    out: CollaborationSummary = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("CollaborationSummary.id required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("CollaborationSummary.arn required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CollaborationSummary.name required")
    if "creatorAccountId" in data:
        out["creator_account_id"] = data["creatorAccountId"]
    else:
        raise DeserializationError("CollaborationSummary.creator_account_id required")
    if "creatorDisplayName" in data:
        out["creator_display_name"] = data["creatorDisplayName"]
    else:
        raise DeserializationError("CollaborationSummary.creator_display_name required")
    if "createTime" in data:
        import aws_sdk_cleanrooms.types._prelude.timestamp

        out["create_time"] = (
            aws_sdk_cleanrooms.types._prelude.timestamp.deserialize_json(
                data["createTime"]
            )
        )
    else:
        raise DeserializationError("CollaborationSummary.create_time required")
    if "updateTime" in data:
        import aws_sdk_cleanrooms.types._prelude.timestamp

        out["update_time"] = (
            aws_sdk_cleanrooms.types._prelude.timestamp.deserialize_json(
                data["updateTime"]
            )
        )
    else:
        raise DeserializationError("CollaborationSummary.update_time required")
    if "memberStatus" in data:
        out["member_status"] = data["memberStatus"]
    else:
        raise DeserializationError("CollaborationSummary.member_status required")
    if "membershipId" in data:
        out["membership_id"] = data["membershipId"]
    if "membershipArn" in data:
        out["membership_arn"] = data["membershipArn"]
    if "analyticsEngine" in data:
        import aws_sdk_cleanrooms.types.analytics_engine

        out["analytics_engine"] = (
            aws_sdk_cleanrooms.types.analytics_engine.deserialize_json(
                data["analyticsEngine"]
            )
        )
    return out
