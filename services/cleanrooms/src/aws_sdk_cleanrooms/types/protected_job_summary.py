"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ProtectedJobSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_cleanrooms.types.account_id
    import aws_sdk_cleanrooms.types.membership_arn
    import aws_sdk_cleanrooms.types.membership_identifier
    import aws_sdk_cleanrooms.types.protected_job_receiver_configurations
    import aws_sdk_cleanrooms.types.protected_job_status
    import aws_sdk_cleanrooms.types.uuid


class ProtectedJobSummary(TypedDict, closed=True):
    id: "aws_sdk_cleanrooms.types.uuid.UUID"
    """<p> The ID of the protected job.</p>"""
    membership_id: "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier"
    """<p>The unique ID for the membership that initiated the protected job.</p>"""
    membership_arn: "aws_sdk_cleanrooms.types.membership_arn.MembershipArn"
    """<p>The unique ARN for the membership that initiated the protected job.</p>"""
    create_time: "datetime.datetime"
    """<p>The time the protected job was created.</p>"""
    status: "aws_sdk_cleanrooms.types.protected_job_status.ProtectedJobStatus"
    """<p>The status of the protected job.</p>"""
    receiver_configurations: "aws_sdk_cleanrooms.types.protected_job_receiver_configurations.ProtectedJobReceiverConfigurations"
    """<p> The receiver configurations for the protected job.</p>"""
    job_compute_payer_account_id: NotRequired[
        "aws_sdk_cleanrooms.types.account_id.AccountId"
    ]
    """<p>The account ID of the member that pays for the job compute costs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProtectedJobSummary) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["membershipId"] = value["membership_id"]
    out["membershipArn"] = value["membership_arn"]
    import aws_sdk_cleanrooms.types._prelude.timestamp

    out["createTime"] = aws_sdk_cleanrooms.types._prelude.timestamp.serialize_json(
        value["create_time"]
    )
    import aws_sdk_cleanrooms.types.protected_job_status

    out["status"] = aws_sdk_cleanrooms.types.protected_job_status.serialize_json(
        value["status"]
    )
    import aws_sdk_cleanrooms.types.protected_job_receiver_configurations

    out["receiverConfigurations"] = (
        aws_sdk_cleanrooms.types.protected_job_receiver_configurations.serialize_json(
            value.get("receiver_configurations", [])
        )
    )
    if "job_compute_payer_account_id" in value:
        out["jobComputePayerAccountId"] = value["job_compute_payer_account_id"]
    return out


def deserialize_json(data: dict) -> ProtectedJobSummary:
    out: ProtectedJobSummary = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("ProtectedJobSummary.id required")
    if "membershipId" in data:
        out["membership_id"] = data["membershipId"]
    else:
        raise DeserializationError("ProtectedJobSummary.membership_id required")
    if "membershipArn" in data:
        out["membership_arn"] = data["membershipArn"]
    else:
        raise DeserializationError("ProtectedJobSummary.membership_arn required")
    if "createTime" in data:
        import aws_sdk_cleanrooms.types._prelude.timestamp

        out["create_time"] = (
            aws_sdk_cleanrooms.types._prelude.timestamp.deserialize_json(
                data["createTime"]
            )
        )
    else:
        raise DeserializationError("ProtectedJobSummary.create_time required")
    if "status" in data:
        import aws_sdk_cleanrooms.types.protected_job_status

        out["status"] = aws_sdk_cleanrooms.types.protected_job_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("ProtectedJobSummary.status required")
    if "receiverConfigurations" in data:
        import aws_sdk_cleanrooms.types.protected_job_receiver_configurations

        out["receiver_configurations"] = (
            aws_sdk_cleanrooms.types.protected_job_receiver_configurations.deserialize_json(
                data["receiverConfigurations"]
            )
        )
    else:
        out["receiver_configurations"] = []
    if "jobComputePayerAccountId" in data:
        out["job_compute_payer_account_id"] = data["jobComputePayerAccountId"]
    return out
