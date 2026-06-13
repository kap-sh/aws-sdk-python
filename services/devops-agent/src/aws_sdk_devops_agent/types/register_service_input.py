"""Generated from Smithy shape ``com.amazonaws.devopsagent#RegisterServiceInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.kms_key_arn
    import aws_sdk_devops_agent.types.post_register_service_supported_service
    import aws_sdk_devops_agent.types.private_connection_name
    import aws_sdk_devops_agent.types.service_details
    import aws_sdk_devops_agent.types.service_name
    import aws_sdk_devops_agent.types.tags


class RegisterServiceInput(TypedDict):
    service: "aws_sdk_devops_agent.types.post_register_service_supported_service.PostRegisterServiceSupportedService"
    service_details: "aws_sdk_devops_agent.types.service_details.ServiceDetails"
    """<p>Service-specific authorization configuration parameters</p>"""
    kms_key_arn: NotRequired["aws_sdk_devops_agent.types.kms_key_arn.KmsKeyArn"]
    """<p>The ARN of the AWS Key Management Service (AWS KMS) customer managed key that's used to encrypt resources.</p>"""
    private_connection_name: NotRequired[
        "aws_sdk_devops_agent.types.private_connection_name.PrivateConnectionName"
    ]
    """<p>The name of the private connection to use for VPC connectivity.</p>"""
    target_url_private_connection_name: NotRequired[
        "aws_sdk_devops_agent.types.private_connection_name.PrivateConnectionName"
    ]
    """<p>The name of the private connection to use for API calls (target URL) only. Cannot be specified when privateConnectionName is provided.</p>"""
    exchange_url_private_connection_name: NotRequired[
        "aws_sdk_devops_agent.types.private_connection_name.PrivateConnectionName"
    ]
    """<p>The name of the private connection to use for OAuth token exchange requests only. Cannot be specified when privateConnectionName is provided.</p>"""
    name: NotRequired["aws_sdk_devops_agent.types.service_name.ServiceName"]
    """<p>The display name for the service registration.</p>"""
    tags: NotRequired["aws_sdk_devops_agent.types.tags.Tags"]
    """<p>Tags to add to the Service at registration time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisterServiceInput) -> dict:
    out: dict = {}
    import aws_sdk_devops_agent.types.service_details

    out["serviceDetails"] = aws_sdk_devops_agent.types.service_details.serialize_json(
        value["service_details"]
    )
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    if "private_connection_name" in value:
        out["privateConnectionName"] = value["private_connection_name"]
    if "target_url_private_connection_name" in value:
        out["targetUrlPrivateConnectionName"] = value[
            "target_url_private_connection_name"
        ]
    if "exchange_url_private_connection_name" in value:
        out["exchangeUrlPrivateConnectionName"] = value[
            "exchange_url_private_connection_name"
        ]
    if "name" in value:
        out["name"] = value["name"]
    if "tags" in value:
        import aws_sdk_devops_agent.types.tags

        out["tags"] = aws_sdk_devops_agent.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> RegisterServiceInput:
    out: RegisterServiceInput = {}  # type: ignore[typeddict-item]
    if "serviceDetails" in data:
        import aws_sdk_devops_agent.types.service_details

        out["service_details"] = (
            aws_sdk_devops_agent.types.service_details.deserialize_json(
                data["serviceDetails"]
            )
        )
    else:
        raise DeserializationError("RegisterServiceInput.service_details required")
    if "kmsKeyArn" in data:
        out["kms_key_arn"] = data["kmsKeyArn"]
    if "privateConnectionName" in data:
        out["private_connection_name"] = data["privateConnectionName"]
    if "targetUrlPrivateConnectionName" in data:
        out["target_url_private_connection_name"] = data[
            "targetUrlPrivateConnectionName"
        ]
    if "exchangeUrlPrivateConnectionName" in data:
        out["exchange_url_private_connection_name"] = data[
            "exchangeUrlPrivateConnectionName"
        ]
    if "name" in data:
        out["name"] = data["name"]
    if "tags" in data:
        import aws_sdk_devops_agent.types.tags

        out["tags"] = aws_sdk_devops_agent.types.tags.deserialize_json(data["tags"])
    return out
