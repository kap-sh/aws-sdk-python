"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GetPaymentManagerResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.authorizer_configuration
    import capo_bedrock_agentcore_control.types.date_timestamp
    import capo_bedrock_agentcore_control.types.payment_manager_arn
    import capo_bedrock_agentcore_control.types.payment_manager_id
    import capo_bedrock_agentcore_control.types.payment_manager_name
    import capo_bedrock_agentcore_control.types.payment_manager_status
    import capo_bedrock_agentcore_control.types.payments_authorizer_type
    import capo_bedrock_agentcore_control.types.payments_description
    import capo_bedrock_agentcore_control.types.role_arn
    import capo_bedrock_agentcore_control.types.tags_map
    import capo_bedrock_agentcore_control.types.workload_identity_details


class GetPaymentManagerResponse(TypedDict, closed=True):
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
    authorizer_configuration: NotRequired[
        "capo_bedrock_agentcore_control.types.authorizer_configuration.AuthorizerConfiguration"
    ]
    role_arn: "capo_bedrock_agentcore_control.types.role_arn.RoleArn"
    """<p>The Amazon Resource Name (ARN) of the IAM role associated with the payment manager.</p>"""
    workload_identity_details: NotRequired[
        "capo_bedrock_agentcore_control.types.workload_identity_details.WorkloadIdentityDetails"
    ]
    created_at: "capo_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the payment manager was created.</p>"""
    last_updated_at: "capo_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the payment manager was last updated.</p>"""
    status: "capo_bedrock_agentcore_control.types.payment_manager_status.PaymentManagerStatus"
    """<p>The current status of the payment manager. Possible values include <code>CREATING</code>, <code>READY</code>, <code>UPDATING</code>, <code>DELETING</code>, <code>CREATE_FAILED</code>, <code>UPDATE_FAILED</code>, and <code>DELETE_FAILED</code>.</p>"""
    tags: NotRequired["capo_bedrock_agentcore_control.types.tags_map.TagsMap"]
    """<p>The tags associated with the payment manager.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPaymentManagerResponse) -> dict:
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
    if "authorizer_configuration" in value:
        import capo_bedrock_agentcore_control.types.authorizer_configuration

        out["authorizerConfiguration"] = (
            capo_bedrock_agentcore_control.types.authorizer_configuration.serialize_json(
                value["authorizer_configuration"]
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
    import capo_bedrock_agentcore_control.types.payment_manager_status

    out["status"] = (
        capo_bedrock_agentcore_control.types.payment_manager_status.serialize_json(
            value["status"]
        )
    )
    if "tags" in value:
        import capo_bedrock_agentcore_control.types.tags_map

        out["tags"] = capo_bedrock_agentcore_control.types.tags_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> GetPaymentManagerResponse:
    out: GetPaymentManagerResponse = {}  # type: ignore[typeddict-item]
    if "paymentManagerArn" in data:
        out["payment_manager_arn"] = data["paymentManagerArn"]
    else:
        raise DeserializationError(
            "GetPaymentManagerResponse.payment_manager_arn required"
        )
    if "paymentManagerId" in data:
        out["payment_manager_id"] = data["paymentManagerId"]
    else:
        raise DeserializationError(
            "GetPaymentManagerResponse.payment_manager_id required"
        )
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GetPaymentManagerResponse.name required")
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
        raise DeserializationError("GetPaymentManagerResponse.authorizer_type required")
    if "authorizerConfiguration" in data:
        import capo_bedrock_agentcore_control.types.authorizer_configuration

        out["authorizer_configuration"] = (
            capo_bedrock_agentcore_control.types.authorizer_configuration.deserialize_json(
                data["authorizerConfiguration"]
            )
        )
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("GetPaymentManagerResponse.role_arn required")
    if "workloadIdentityDetails" in data:
        import capo_bedrock_agentcore_control.types.workload_identity_details

        out["workload_identity_details"] = (
            capo_bedrock_agentcore_control.types.workload_identity_details.deserialize_json(
                data["workloadIdentityDetails"]
            )
        )
    if "createdAt" in data:
        import capo_bedrock_agentcore_control.types.date_timestamp

        out["created_at"] = (
            capo_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("GetPaymentManagerResponse.created_at required")
    if "lastUpdatedAt" in data:
        import capo_bedrock_agentcore_control.types.date_timestamp

        out["last_updated_at"] = (
            capo_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["lastUpdatedAt"]
            )
        )
    else:
        raise DeserializationError("GetPaymentManagerResponse.last_updated_at required")
    if "status" in data:
        import capo_bedrock_agentcore_control.types.payment_manager_status

        out["status"] = (
            capo_bedrock_agentcore_control.types.payment_manager_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("GetPaymentManagerResponse.status required")
    if "tags" in data:
        import capo_bedrock_agentcore_control.types.tags_map

        out["tags"] = capo_bedrock_agentcore_control.types.tags_map.deserialize_json(
            data["tags"]
        )
    return out
