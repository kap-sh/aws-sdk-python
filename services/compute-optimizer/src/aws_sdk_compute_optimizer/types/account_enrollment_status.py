"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#AccountEnrollmentStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.account_id
    import aws_sdk_compute_optimizer.types.last_updated_timestamp
    import aws_sdk_compute_optimizer.types.status
    import aws_sdk_compute_optimizer.types.status_reason


class AccountEnrollmentStatus(TypedDict, closed=True):
    account_id: NotRequired["aws_sdk_compute_optimizer.types.account_id.AccountId"]
    """<p>The Amazon Web Services account ID.</p>"""
    status: NotRequired["aws_sdk_compute_optimizer.types.status.Status"]
    """<p>The account enrollment status.</p>"""
    status_reason: NotRequired[
        "aws_sdk_compute_optimizer.types.status_reason.StatusReason"
    ]
    """<p>The reason for the account enrollment status.</p> <p>For example, an account might show a status of <code>Pending</code> because member accounts of an organization require more time to be enrolled in the service.</p>"""
    last_updated_timestamp: NotRequired[
        "aws_sdk_compute_optimizer.types.last_updated_timestamp.LastUpdatedTimestamp"
    ]
    """<p>The Unix epoch timestamp, in seconds, of when the account enrollment status was last updated.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AccountEnrollmentStatus) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "status" in value:
        import aws_sdk_compute_optimizer.types.status

        out["status"] = aws_sdk_compute_optimizer.types.status.serialize_aws_json_1_0(
            value["status"]
        )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    if "last_updated_timestamp" in value:
        import aws_sdk_compute_optimizer.types.last_updated_timestamp

        out["lastUpdatedTimestamp"] = (
            aws_sdk_compute_optimizer.types.last_updated_timestamp.serialize_aws_json_1_0(
                value["last_updated_timestamp"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> AccountEnrollmentStatus:
    out: AccountEnrollmentStatus = {}  # type: ignore[typeddict-item]
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    if "status" in data:
        import aws_sdk_compute_optimizer.types.status

        out["status"] = aws_sdk_compute_optimizer.types.status.deserialize_aws_json_1_0(
            data["status"]
        )
    if "statusReason" in data:
        out["status_reason"] = data["statusReason"]
    if "lastUpdatedTimestamp" in data:
        import aws_sdk_compute_optimizer.types.last_updated_timestamp

        out["last_updated_timestamp"] = (
            aws_sdk_compute_optimizer.types.last_updated_timestamp.deserialize_aws_json_1_0(
                data["lastUpdatedTimestamp"]
            )
        )
    return out
