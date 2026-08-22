"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#UpdatePaymentManagerResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.date_timestamp
    import capo_bedrock_agentcore_control.types.payment_manager_arn
    import capo_bedrock_agentcore_control.types.payment_manager_id
    import capo_bedrock_agentcore_control.types.payment_manager_name
    import capo_bedrock_agentcore_control.types.payment_manager_status
    import capo_bedrock_agentcore_control.types.payments_authorizer_type
    import capo_bedrock_agentcore_control.types.role_arn
    import capo_bedrock_agentcore_control.types.workload_identity_details


class UpdatePaymentManagerResponse(TypedDict, closed=True):
    payment_manager_arn: (
        "capo_bedrock_agentcore_control.types.payment_manager_arn.PaymentManagerArn"
    )
    """<p>The Amazon Resource Name (ARN) of the updated payment manager.</p>"""
    payment_manager_id: (
        "capo_bedrock_agentcore_control.types.payment_manager_id.PaymentManagerId"
    )
    """<p>The unique identifier of the updated payment manager.</p>"""
    name: "capo_bedrock_agentcore_control.types.payment_manager_name.PaymentManagerName"
    """<p>The name of the updated payment manager.</p>"""
    authorizer_type: "capo_bedrock_agentcore_control.types.payments_authorizer_type.PaymentsAuthorizerType"
    """<p>The type of authorizer for the updated payment manager.</p>"""
    role_arn: "capo_bedrock_agentcore_control.types.role_arn.RoleArn"
    """<p>The Amazon Resource Name (ARN) of the IAM role associated with the updated payment manager.</p>"""
    workload_identity_details: NotRequired[
        "capo_bedrock_agentcore_control.types.workload_identity_details.WorkloadIdentityDetails"
    ]
    last_updated_at: "capo_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the payment manager was last updated.</p>"""
    status: "capo_bedrock_agentcore_control.types.payment_manager_status.PaymentManagerStatus"
    """<p>The current status of the updated payment manager. Possible values include <code>CREATING</code>, <code>READY</code>, <code>UPDATING</code>, <code>DELETING</code>, <code>CREATE_FAILED</code>, <code>UPDATE_FAILED</code>, and <code>DELETE_FAILED</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePaymentManagerResponse) -> dict:
    out: dict = {}
    out["paymentManagerArn"] = value["payment_manager_arn"]
    out["paymentManagerId"] = value["payment_manager_id"]
    out["name"] = value["name"]
    import capo_bedrock_agentcore_control.types.payments_authorizer_type

    out["authorizerType"] = (
        capo_bedrock_agentcore_control.types.payments_authorizer_type.serialize_json(
            value["authorizer_type"]
        )
    )
    out["roleArn"] = value["role_arn"]
    if "workload_identity_details" in value:
        import capo_bedrock_agentcore_control.types.workload_identity_details

        out["workloadIdentityDetails"] = (
            capo_bedrock_agentcore_control.types.workload_identity_details.serialize_json(
                value["workload_identity_details"]
            )
        )
    import capo_bedrock_agentcore_control.types.date_timestamp

    out["lastUpdatedAt"] = (
        capo_bedrock_agentcore_control.types.date_timestamp.serialize_json(
            value["last_updated_at"]
        )
    )
    import capo_bedrock_agentcore_control.types.payment_manager_status

    out["status"] = (
        capo_bedrock_agentcore_control.types.payment_manager_status.serialize_json(
            value["status"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdatePaymentManagerResponse:
    out: UpdatePaymentManagerResponse = {}  # type: ignore[typeddict-item]
    if data.get("paymentManagerArn") is not None:
        out["payment_manager_arn"] = data["paymentManagerArn"]
    else:
        raise DeserializationError(
            "UpdatePaymentManagerResponse.payment_manager_arn required"
        )
    if data.get("paymentManagerId") is not None:
        out["payment_manager_id"] = data["paymentManagerId"]
    else:
        raise DeserializationError(
            "UpdatePaymentManagerResponse.payment_manager_id required"
        )
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("UpdatePaymentManagerResponse.name required")
    if data.get("authorizerType") is not None:
        import capo_bedrock_agentcore_control.types.payments_authorizer_type

        out["authorizer_type"] = (
            capo_bedrock_agentcore_control.types.payments_authorizer_type.deserialize_json(
                data["authorizerType"]
            )
        )
    else:
        raise DeserializationError(
            "UpdatePaymentManagerResponse.authorizer_type required"
        )
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("UpdatePaymentManagerResponse.role_arn required")
    if data.get("workloadIdentityDetails") is not None:
        import capo_bedrock_agentcore_control.types.workload_identity_details

        out["workload_identity_details"] = (
            capo_bedrock_agentcore_control.types.workload_identity_details.deserialize_json(
                data["workloadIdentityDetails"]
            )
        )
    if data.get("lastUpdatedAt") is not None:
        import capo_bedrock_agentcore_control.types.date_timestamp

        out["last_updated_at"] = (
            capo_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["lastUpdatedAt"]
            )
        )
    else:
        raise DeserializationError(
            "UpdatePaymentManagerResponse.last_updated_at required"
        )
    if data.get("status") is not None:
        import capo_bedrock_agentcore_control.types.payment_manager_status

        out["status"] = (
            capo_bedrock_agentcore_control.types.payment_manager_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("UpdatePaymentManagerResponse.status required")
    return out
