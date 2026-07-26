"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#PaymentManagerSummary``."""

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
    import capo_bedrock_agentcore_control.types.payments_description
    import capo_bedrock_agentcore_control.types.role_arn


class PaymentManagerSummary(TypedDict, closed=True):
    payment_manager_arn: (
        "capo_bedrock_agentcore_control.types.payment_manager_arn.PaymentManagerArn"
    )
    """<p>The Amazon Resource Name (ARN) of the payment manager.</p>"""
    payment_manager_id: (
        "capo_bedrock_agentcore_control.types.payment_manager_id.PaymentManagerId"
    )
    """<p>The unique identifier of the payment manager.</p>"""
    name: "capo_bedrock_agentcore_control.types.payment_manager_name.PaymentManagerName"
    """<p>The name of the payment manager.</p>"""
    description: NotRequired[
        "capo_bedrock_agentcore_control.types.payments_description.PaymentsDescription"
    ]
    """<p>The description of the payment manager.</p>"""
    authorizer_type: "capo_bedrock_agentcore_control.types.payments_authorizer_type.PaymentsAuthorizerType"
    """<p>The type of authorizer used by the payment manager.</p> <ul> <li> <p> <code>CUSTOM_JWT</code> - Authorize with a bearer token.</p> </li> <li> <p> <code>AWS_IAM</code> - Authorize with your Amazon Web Services IAM credentials.</p> </li> </ul>"""
    role_arn: "capo_bedrock_agentcore_control.types.role_arn.RoleArn"
    """<p>The Amazon Resource Name (ARN) of the IAM role associated with the payment manager.</p>"""
    status: "capo_bedrock_agentcore_control.types.payment_manager_status.PaymentManagerStatus"
    """<p>The current status of the payment manager. Possible values include <code>CREATING</code>, <code>READY</code>, <code>UPDATING</code>, <code>DELETING</code>, <code>CREATE_FAILED</code>, <code>UPDATE_FAILED</code>, and <code>DELETE_FAILED</code>.</p>"""
    created_at: NotRequired[
        "capo_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    ]
    """<p>The timestamp when the payment manager was created.</p>"""
    last_updated_at: "capo_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the payment manager was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PaymentManagerSummary) -> dict:
    out: dict = {}
    out["paymentManagerArn"] = value["payment_manager_arn"]
    out["paymentManagerId"] = value["payment_manager_id"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_bedrock_agentcore_control.types.payments_authorizer_type

    out["authorizerType"] = (
        capo_bedrock_agentcore_control.types.payments_authorizer_type.serialize_json(
            value["authorizer_type"]
        )
    )
    out["roleArn"] = value["role_arn"]
    import capo_bedrock_agentcore_control.types.payment_manager_status

    out["status"] = (
        capo_bedrock_agentcore_control.types.payment_manager_status.serialize_json(
            value["status"]
        )
    )
    if "created_at" in value:
        import capo_bedrock_agentcore_control.types.date_timestamp

        out["createdAt"] = (
            capo_bedrock_agentcore_control.types.date_timestamp.serialize_json(
                value["created_at"]
            )
        )
    import capo_bedrock_agentcore_control.types.date_timestamp

    out["lastUpdatedAt"] = (
        capo_bedrock_agentcore_control.types.date_timestamp.serialize_json(
            value["last_updated_at"]
        )
    )
    return out


def deserialize_json(data: dict) -> PaymentManagerSummary:
    out: PaymentManagerSummary = {}  # type: ignore[typeddict-item]
    if "paymentManagerArn" in data:
        out["payment_manager_arn"] = data["paymentManagerArn"]
    else:
        raise DeserializationError("PaymentManagerSummary.payment_manager_arn required")
    if "paymentManagerId" in data:
        out["payment_manager_id"] = data["paymentManagerId"]
    else:
        raise DeserializationError("PaymentManagerSummary.payment_manager_id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("PaymentManagerSummary.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "authorizerType" in data:
        import capo_bedrock_agentcore_control.types.payments_authorizer_type

        out["authorizer_type"] = (
            capo_bedrock_agentcore_control.types.payments_authorizer_type.deserialize_json(
                data["authorizerType"]
            )
        )
    else:
        raise DeserializationError("PaymentManagerSummary.authorizer_type required")
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("PaymentManagerSummary.role_arn required")
    if "status" in data:
        import capo_bedrock_agentcore_control.types.payment_manager_status

        out["status"] = (
            capo_bedrock_agentcore_control.types.payment_manager_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("PaymentManagerSummary.status required")
    if "createdAt" in data:
        import capo_bedrock_agentcore_control.types.date_timestamp

        out["created_at"] = (
            capo_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    if "lastUpdatedAt" in data:
        import capo_bedrock_agentcore_control.types.date_timestamp

        out["last_updated_at"] = (
            capo_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["lastUpdatedAt"]
            )
        )
    else:
        raise DeserializationError("PaymentManagerSummary.last_updated_at required")
    return out
