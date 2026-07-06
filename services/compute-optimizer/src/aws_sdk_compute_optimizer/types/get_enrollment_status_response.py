"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#GetEnrollmentStatusResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.last_updated_timestamp
    import aws_sdk_compute_optimizer.types.member_accounts_enrolled
    import aws_sdk_compute_optimizer.types.number_of_member_accounts_opted_in
    import aws_sdk_compute_optimizer.types.status
    import aws_sdk_compute_optimizer.types.status_reason


class GetEnrollmentStatusResponse(TypedDict, closed=True):
    status: NotRequired["aws_sdk_compute_optimizer.types.status.Status"]
    """<p>The enrollment status of the account.</p>"""
    status_reason: NotRequired[
        "aws_sdk_compute_optimizer.types.status_reason.StatusReason"
    ]
    """<p>The reason for the enrollment status of the account.</p> <p>For example, an account might show a status of <code>Pending</code> because member accounts of an organization require more time to be enrolled in the service.</p>"""
    member_accounts_enrolled: "aws_sdk_compute_optimizer.types.member_accounts_enrolled.MemberAccountsEnrolled"
    """<p>Confirms the enrollment status of member accounts of the organization, if the account is a management account of an organization.</p>"""
    last_updated_timestamp: NotRequired[
        "aws_sdk_compute_optimizer.types.last_updated_timestamp.LastUpdatedTimestamp"
    ]
    """<p>The Unix epoch timestamp, in seconds, of when the account enrollment status was last updated.</p>"""
    number_of_member_accounts_opted_in: NotRequired[
        "aws_sdk_compute_optimizer.types.number_of_member_accounts_opted_in.NumberOfMemberAccountsOptedIn"
    ]
    """<p>The count of organization member accounts that are opted in to the service, if your account is an organization management account.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetEnrollmentStatusResponse) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_compute_optimizer.types.status

        out["status"] = aws_sdk_compute_optimizer.types.status.serialize_aws_json_1_0(
            value["status"]
        )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    out["memberAccountsEnrolled"] = value.get("member_accounts_enrolled", False)
    if "last_updated_timestamp" in value:
        import aws_sdk_compute_optimizer.types.last_updated_timestamp

        out["lastUpdatedTimestamp"] = (
            aws_sdk_compute_optimizer.types.last_updated_timestamp.serialize_aws_json_1_0(
                value["last_updated_timestamp"]
            )
        )
    if "number_of_member_accounts_opted_in" in value:
        out["numberOfMemberAccountsOptedIn"] = value[
            "number_of_member_accounts_opted_in"
        ]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetEnrollmentStatusResponse:
    out: GetEnrollmentStatusResponse = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import aws_sdk_compute_optimizer.types.status

        out["status"] = aws_sdk_compute_optimizer.types.status.deserialize_aws_json_1_0(
            data["status"]
        )
    if "statusReason" in data:
        out["status_reason"] = data["statusReason"]
    if "memberAccountsEnrolled" in data:
        out["member_accounts_enrolled"] = data["memberAccountsEnrolled"]
    else:
        out["member_accounts_enrolled"] = False
    if "lastUpdatedTimestamp" in data:
        import aws_sdk_compute_optimizer.types.last_updated_timestamp

        out["last_updated_timestamp"] = (
            aws_sdk_compute_optimizer.types.last_updated_timestamp.deserialize_aws_json_1_0(
                data["lastUpdatedTimestamp"]
            )
        )
    if "numberOfMemberAccountsOptedIn" in data:
        out["number_of_member_accounts_opted_in"] = data[
            "numberOfMemberAccountsOptedIn"
        ]
    return out
