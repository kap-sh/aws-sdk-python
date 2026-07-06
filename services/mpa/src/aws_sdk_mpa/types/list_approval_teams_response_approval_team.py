"""Generated from Smithy shape ``com.amazonaws.mpa#ListApprovalTeamsResponseApprovalTeam``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mpa.types.approval_strategy_response
    import aws_sdk_mpa.types.approval_team_arn
    import aws_sdk_mpa.types.approval_team_name
    import aws_sdk_mpa.types.approval_team_status
    import aws_sdk_mpa.types.approval_team_status_code
    import aws_sdk_mpa.types.description
    import aws_sdk_mpa.types.iso_timestamp
    import aws_sdk_mpa.types.message


class ListApprovalTeamsResponseApprovalTeam(TypedDict, closed=True):
    creation_time: NotRequired["aws_sdk_mpa.types.iso_timestamp.IsoTimestamp"]
    """<p>Timestamp when the team was created.</p>"""
    approval_strategy: NotRequired[
        "aws_sdk_mpa.types.approval_strategy_response.ApprovalStrategyResponse"
    ]
    """<p>An <code>ApprovalStrategyResponse</code> object. Contains details for how an approval team grants approval.</p>"""
    number_of_approvers: NotRequired["int"]
    """<p>Total number of approvers in the team.</p>"""
    arn: NotRequired["aws_sdk_mpa.types.approval_team_arn.ApprovalTeamArn"]
    """<p>Amazon Resource Name (ARN) for the team.</p>"""
    name: NotRequired["aws_sdk_mpa.types.approval_team_name.ApprovalTeamName"]
    """<p>Name of the team.</p>"""
    description: NotRequired["aws_sdk_mpa.types.description.Description"]
    """<p>Description for the team.</p>"""
    status: NotRequired["aws_sdk_mpa.types.approval_team_status.ApprovalTeamStatus"]
    r"""<p>Status for the team. For more information, see <a href=\"https://docs.aws.amazon.com/mpa/latest/userguide/mpa-health.html\">Team health</a> in the <i>Multi-party approval User Guide</i>.</p>"""
    status_code: NotRequired[
        "aws_sdk_mpa.types.approval_team_status_code.ApprovalTeamStatusCode"
    ]
    r"""<p>Status code for the team. For more information, see <a href=\"https://docs.aws.amazon.com/mpa/latest/userguide/mpa-health.html\">Team health</a> in the <i>Multi-party approval User Guide</i>.</p>"""
    status_message: NotRequired["aws_sdk_mpa.types.message.Message"]
    """<p>Message describing the status for the team.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListApprovalTeamsResponseApprovalTeam) -> dict:
    out: dict = {}
    if "creation_time" in value:
        import aws_sdk_mpa.types.iso_timestamp

        out["CreationTime"] = aws_sdk_mpa.types.iso_timestamp.serialize_json(
            value["creation_time"]
        )
    if "approval_strategy" in value:
        import aws_sdk_mpa.types.approval_strategy_response

        out["ApprovalStrategy"] = (
            aws_sdk_mpa.types.approval_strategy_response.serialize_json(
                value["approval_strategy"]
            )
        )
    if "number_of_approvers" in value:
        out["NumberOfApprovers"] = value["number_of_approvers"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "status" in value:
        import aws_sdk_mpa.types.approval_team_status

        out["Status"] = aws_sdk_mpa.types.approval_team_status.serialize_json(
            value["status"]
        )
    if "status_code" in value:
        import aws_sdk_mpa.types.approval_team_status_code

        out["StatusCode"] = aws_sdk_mpa.types.approval_team_status_code.serialize_json(
            value["status_code"]
        )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    return out


def deserialize_json(data: dict) -> ListApprovalTeamsResponseApprovalTeam:
    out: ListApprovalTeamsResponseApprovalTeam = {}  # type: ignore[typeddict-item]
    if "CreationTime" in data:
        import aws_sdk_mpa.types.iso_timestamp

        out["creation_time"] = aws_sdk_mpa.types.iso_timestamp.deserialize_json(
            data["CreationTime"]
        )
    if "ApprovalStrategy" in data:
        import aws_sdk_mpa.types.approval_strategy_response

        out["approval_strategy"] = (
            aws_sdk_mpa.types.approval_strategy_response.deserialize_json(
                data["ApprovalStrategy"]
            )
        )
    if "NumberOfApprovers" in data:
        out["number_of_approvers"] = data["NumberOfApprovers"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Status" in data:
        import aws_sdk_mpa.types.approval_team_status

        out["status"] = aws_sdk_mpa.types.approval_team_status.deserialize_json(
            data["Status"]
        )
    if "StatusCode" in data:
        import aws_sdk_mpa.types.approval_team_status_code

        out["status_code"] = (
            aws_sdk_mpa.types.approval_team_status_code.deserialize_json(
                data["StatusCode"]
            )
        )
    if "StatusMessage" in data:
        out["status_message"] = data["StatusMessage"]
    return out
