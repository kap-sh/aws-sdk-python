"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CreatePaymentManagerResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.authorizer_configuration
    import aws_sdk_bedrock_agentcore_control.types.date_timestamp
    import aws_sdk_bedrock_agentcore_control.types.payment_manager_arn
    import aws_sdk_bedrock_agentcore_control.types.payment_manager_id
    import aws_sdk_bedrock_agentcore_control.types.payment_manager_name
    import aws_sdk_bedrock_agentcore_control.types.payment_manager_status
    import aws_sdk_bedrock_agentcore_control.types.payments_authorizer_type
    import aws_sdk_bedrock_agentcore_control.types.role_arn
    import aws_sdk_bedrock_agentcore_control.types.tags_map
    import aws_sdk_bedrock_agentcore_control.types.workload_identity_details


class CreatePaymentManagerResponse(TypedDict):
    payment_manager_arn: (
        "aws_sdk_bedrock_agentcore_control.types.payment_manager_arn.PaymentManagerArn"
    )
    """<p>The Amazon Resource Name (ARN) of the created payment manager.</p>"""
    payment_manager_id: (
        "aws_sdk_bedrock_agentcore_control.types.payment_manager_id.PaymentManagerId"
    )
    """<p>The unique identifier of the created payment manager.</p>"""
    name: "aws_sdk_bedrock_agentcore_control.types.payment_manager_name.PaymentManagerName"
    """<p>The name of the created payment manager.</p>"""
    authorizer_type: "aws_sdk_bedrock_agentcore_control.types.payments_authorizer_type.PaymentsAuthorizerType"
    """<p>The type of authorizer for the created payment manager.</p>"""
    authorizer_configuration: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.authorizer_configuration.AuthorizerConfiguration"
    ]
    role_arn: "aws_sdk_bedrock_agentcore_control.types.role_arn.RoleArn"
    """<p>The Amazon Resource Name (ARN) of the IAM role associated with the created payment manager.</p>"""
    workload_identity_details: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.workload_identity_details.WorkloadIdentityDetails"
    ]
    created_at: "aws_sdk_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the payment manager was created.</p>"""
    status: "aws_sdk_bedrock_agentcore_control.types.payment_manager_status.PaymentManagerStatus"
    """<p>The current status of the payment manager. Possible values include <code>CREATING</code>, <code>READY</code>, <code>UPDATING</code>, <code>DELETING</code>, <code>CREATE_FAILED</code>, <code>UPDATE_FAILED</code>, and <code>DELETE_FAILED</code>.</p>"""
    tags: NotRequired["aws_sdk_bedrock_agentcore_control.types.tags_map.TagsMap"]
    """<p>The tags associated with the created payment manager.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePaymentManagerResponse) -> dict:
    out: dict = {}
    out["paymentManagerArn"] = value["payment_manager_arn"]
    out["paymentManagerId"] = value["payment_manager_id"]
    out["name"] = value["name"]
    import aws_sdk_bedrock_agentcore_control.types.payments_authorizer_type

    out["authorizerType"] = (
        aws_sdk_bedrock_agentcore_control.types.payments_authorizer_type.serialize_json(
            value["authorizer_type"]
        )
    )
    if "authorizer_configuration" in value:
        import aws_sdk_bedrock_agentcore_control.types.authorizer_configuration

        out["authorizerConfiguration"] = (
            aws_sdk_bedrock_agentcore_control.types.authorizer_configuration.serialize_json(
                value["authorizer_configuration"]
            )
        )
    out["roleArn"] = value["role_arn"]
    if "workload_identity_details" in value:
        import aws_sdk_bedrock_agentcore_control.types.workload_identity_details

        out["workloadIdentityDetails"] = (
            aws_sdk_bedrock_agentcore_control.types.workload_identity_details.serialize_json(
                value["workload_identity_details"]
            )
        )
    import aws_sdk_bedrock_agentcore_control.types.date_timestamp

    out["createdAt"] = (
        aws_sdk_bedrock_agentcore_control.types.date_timestamp.serialize_json(
            value["created_at"]
        )
    )
    import aws_sdk_bedrock_agentcore_control.types.payment_manager_status

    out["status"] = (
        aws_sdk_bedrock_agentcore_control.types.payment_manager_status.serialize_json(
            value["status"]
        )
    )
    if "tags" in value:
        import aws_sdk_bedrock_agentcore_control.types.tags_map

        out["tags"] = aws_sdk_bedrock_agentcore_control.types.tags_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreatePaymentManagerResponse:
    out: CreatePaymentManagerResponse = {}  # type: ignore[typeddict-item]
    if "paymentManagerArn" in data:
        out["payment_manager_arn"] = data["paymentManagerArn"]
    else:
        raise DeserializationError(
            "CreatePaymentManagerResponse.payment_manager_arn required"
        )
    if "paymentManagerId" in data:
        out["payment_manager_id"] = data["paymentManagerId"]
    else:
        raise DeserializationError(
            "CreatePaymentManagerResponse.payment_manager_id required"
        )
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreatePaymentManagerResponse.name required")
    if "authorizerType" in data:
        import aws_sdk_bedrock_agentcore_control.types.payments_authorizer_type

        out["authorizer_type"] = (
            aws_sdk_bedrock_agentcore_control.types.payments_authorizer_type.deserialize_json(
                data["authorizerType"]
            )
        )
    else:
        raise DeserializationError(
            "CreatePaymentManagerResponse.authorizer_type required"
        )
    if "authorizerConfiguration" in data:
        import aws_sdk_bedrock_agentcore_control.types.authorizer_configuration

        out["authorizer_configuration"] = (
            aws_sdk_bedrock_agentcore_control.types.authorizer_configuration.deserialize_json(
                data["authorizerConfiguration"]
            )
        )
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("CreatePaymentManagerResponse.role_arn required")
    if "workloadIdentityDetails" in data:
        import aws_sdk_bedrock_agentcore_control.types.workload_identity_details

        out["workload_identity_details"] = (
            aws_sdk_bedrock_agentcore_control.types.workload_identity_details.deserialize_json(
                data["workloadIdentityDetails"]
            )
        )
    if "createdAt" in data:
        import aws_sdk_bedrock_agentcore_control.types.date_timestamp

        out["created_at"] = (
            aws_sdk_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("CreatePaymentManagerResponse.created_at required")
    if "status" in data:
        import aws_sdk_bedrock_agentcore_control.types.payment_manager_status

        out["status"] = (
            aws_sdk_bedrock_agentcore_control.types.payment_manager_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("CreatePaymentManagerResponse.status required")
    if "tags" in data:
        import aws_sdk_bedrock_agentcore_control.types.tags_map

        out["tags"] = aws_sdk_bedrock_agentcore_control.types.tags_map.deserialize_json(
            data["tags"]
        )
    return out
