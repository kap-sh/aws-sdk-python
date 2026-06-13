"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ProtectedQuerySummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_cleanrooms.types.account_id
    import aws_sdk_cleanrooms.types.membership_arn
    import aws_sdk_cleanrooms.types.protected_query_status
    import aws_sdk_cleanrooms.types.receiver_configurations_list
    import aws_sdk_cleanrooms.types.uuid


class ProtectedQuerySummary(TypedDict):
    id: "aws_sdk_cleanrooms.types.uuid.UUID"
    """<p>The unique ID of the protected query.</p>"""
    membership_id: "aws_sdk_cleanrooms.types.uuid.UUID"
    """<p>The unique ID for the membership that initiated the protected query.</p>"""
    membership_arn: "aws_sdk_cleanrooms.types.membership_arn.MembershipArn"
    """<p>The unique ARN for the membership that initiated the protected query.</p>"""
    create_time: "datetime.datetime"
    """<p>The time the protected query was created.</p>"""
    status: "aws_sdk_cleanrooms.types.protected_query_status.ProtectedQueryStatus"
    """<p>The status of the protected query.</p>"""
    receiver_configurations: "aws_sdk_cleanrooms.types.receiver_configurations_list.ReceiverConfigurationsList"
    """<p> The receiver configuration.</p>"""
    query_compute_payer_account_id: NotRequired[
        "aws_sdk_cleanrooms.types.account_id.AccountId"
    ]
    """<p>The account ID of the member that pays for the query compute costs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProtectedQuerySummary) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["membershipId"] = value["membership_id"]
    out["membershipArn"] = value["membership_arn"]
    import aws_sdk_cleanrooms.types._prelude.timestamp

    out["createTime"] = aws_sdk_cleanrooms.types._prelude.timestamp.serialize_json(
        value["create_time"]
    )
    out["status"] = value["status"]
    import aws_sdk_cleanrooms.types.receiver_configurations_list

    out["receiverConfigurations"] = (
        aws_sdk_cleanrooms.types.receiver_configurations_list.serialize_json(
            value.get("receiver_configurations", [])
        )
    )
    if "query_compute_payer_account_id" in value:
        out["queryComputePayerAccountId"] = value["query_compute_payer_account_id"]
    return out


def deserialize_json(data: dict) -> ProtectedQuerySummary:
    out: ProtectedQuerySummary = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("ProtectedQuerySummary.id required")
    if "membershipId" in data:
        out["membership_id"] = data["membershipId"]
    else:
        raise DeserializationError("ProtectedQuerySummary.membership_id required")
    if "membershipArn" in data:
        out["membership_arn"] = data["membershipArn"]
    else:
        raise DeserializationError("ProtectedQuerySummary.membership_arn required")
    if "createTime" in data:
        import aws_sdk_cleanrooms.types._prelude.timestamp

        out["create_time"] = (
            aws_sdk_cleanrooms.types._prelude.timestamp.deserialize_json(
                data["createTime"]
            )
        )
    else:
        raise DeserializationError("ProtectedQuerySummary.create_time required")
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("ProtectedQuerySummary.status required")
    if "receiverConfigurations" in data:
        import aws_sdk_cleanrooms.types.receiver_configurations_list

        out["receiver_configurations"] = (
            aws_sdk_cleanrooms.types.receiver_configurations_list.deserialize_json(
                data["receiverConfigurations"]
            )
        )
    else:
        out["receiver_configurations"] = []
    if "queryComputePayerAccountId" in data:
        out["query_compute_payer_account_id"] = data["queryComputePayerAccountId"]
    return out
