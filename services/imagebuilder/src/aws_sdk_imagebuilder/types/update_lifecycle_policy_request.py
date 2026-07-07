"""Generated from Smithy shape ``com.amazonaws.imagebuilder#UpdateLifecyclePolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_imagebuilder.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.client_token
    import aws_sdk_imagebuilder.types.lifecycle_policy_arn
    import aws_sdk_imagebuilder.types.lifecycle_policy_details
    import aws_sdk_imagebuilder.types.lifecycle_policy_resource_selection
    import aws_sdk_imagebuilder.types.lifecycle_policy_resource_type
    import aws_sdk_imagebuilder.types.lifecycle_policy_status
    import aws_sdk_imagebuilder.types.non_empty_string
    import aws_sdk_imagebuilder.types.role_name_or_arn


class UpdateLifecyclePolicyRequest(TypedDict, closed=True):
    lifecycle_policy_arn: (
        "aws_sdk_imagebuilder.types.lifecycle_policy_arn.LifecyclePolicyArn"
    )
    """<p>The Amazon Resource Name (ARN) of the lifecycle policy resource.</p>"""
    description: NotRequired[
        "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>Optional description for the lifecycle policy.</p>"""
    status: NotRequired[
        "aws_sdk_imagebuilder.types.lifecycle_policy_status.LifecyclePolicyStatus"
    ]
    """<p>Indicates whether the lifecycle policy resource is enabled.</p>"""
    execution_role: "aws_sdk_imagebuilder.types.role_name_or_arn.RoleNameOrArn"
    """<p>The name or Amazon Resource Name (ARN) of the IAM role that Image Builder uses to update the lifecycle policy.</p>"""
    resource_type: "aws_sdk_imagebuilder.types.lifecycle_policy_resource_type.LifecyclePolicyResourceType"
    """<p>The type of image resource that the lifecycle policy applies to.</p>"""
    policy_details: (
        "aws_sdk_imagebuilder.types.lifecycle_policy_details.LifecyclePolicyDetails"
    )
    """<p>The configuration details for a lifecycle policy resource.</p>"""
    resource_selection: "aws_sdk_imagebuilder.types.lifecycle_policy_resource_selection.LifecyclePolicyResourceSelection"
    """<p>Selection criteria for resources that the lifecycle policy applies to.</p>"""
    client_token: "aws_sdk_imagebuilder.types.client_token.ClientToken"
    r"""<p>Unique, case-sensitive identifier you provide to ensure idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a> in the <i>Amazon EC2 API Reference</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateLifecyclePolicyRequest) -> dict:
    out: dict = {}
    out["lifecyclePolicyArn"] = value["lifecycle_policy_arn"]
    if "description" in value:
        out["description"] = value["description"]
    if "status" in value:
        import aws_sdk_imagebuilder.types.lifecycle_policy_status

        out["status"] = (
            aws_sdk_imagebuilder.types.lifecycle_policy_status.serialize_json(
                value["status"]
            )
        )
    out["executionRole"] = value["execution_role"]
    import aws_sdk_imagebuilder.types.lifecycle_policy_resource_type

    out["resourceType"] = (
        aws_sdk_imagebuilder.types.lifecycle_policy_resource_type.serialize_json(
            value["resource_type"]
        )
    )
    import aws_sdk_imagebuilder.types.lifecycle_policy_details

    out["policyDetails"] = (
        aws_sdk_imagebuilder.types.lifecycle_policy_details.serialize_json(
            value["policy_details"]
        )
    )
    import aws_sdk_imagebuilder.types.lifecycle_policy_resource_selection

    out["resourceSelection"] = (
        aws_sdk_imagebuilder.types.lifecycle_policy_resource_selection.serialize_json(
            value["resource_selection"]
        )
    )
    out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> UpdateLifecyclePolicyRequest:
    out: UpdateLifecyclePolicyRequest = {}  # type: ignore[typeddict-item]
    if "lifecyclePolicyArn" in data:
        out["lifecycle_policy_arn"] = data["lifecyclePolicyArn"]
    else:
        raise DeserializationError(
            "UpdateLifecyclePolicyRequest.lifecycle_policy_arn required"
        )
    if "description" in data:
        out["description"] = data["description"]
    if "status" in data:
        import aws_sdk_imagebuilder.types.lifecycle_policy_status

        out["status"] = (
            aws_sdk_imagebuilder.types.lifecycle_policy_status.deserialize_json(
                data["status"]
            )
        )
    if "executionRole" in data:
        out["execution_role"] = data["executionRole"]
    else:
        raise DeserializationError(
            "UpdateLifecyclePolicyRequest.execution_role required"
        )
    if "resourceType" in data:
        import aws_sdk_imagebuilder.types.lifecycle_policy_resource_type

        out["resource_type"] = (
            aws_sdk_imagebuilder.types.lifecycle_policy_resource_type.deserialize_json(
                data["resourceType"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateLifecyclePolicyRequest.resource_type required"
        )
    if "policyDetails" in data:
        import aws_sdk_imagebuilder.types.lifecycle_policy_details

        out["policy_details"] = (
            aws_sdk_imagebuilder.types.lifecycle_policy_details.deserialize_json(
                data["policyDetails"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateLifecyclePolicyRequest.policy_details required"
        )
    if "resourceSelection" in data:
        import aws_sdk_imagebuilder.types.lifecycle_policy_resource_selection

        out["resource_selection"] = (
            aws_sdk_imagebuilder.types.lifecycle_policy_resource_selection.deserialize_json(
                data["resourceSelection"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateLifecyclePolicyRequest.resource_selection required"
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    else:
        raise DeserializationError("UpdateLifecyclePolicyRequest.client_token required")
    return out
