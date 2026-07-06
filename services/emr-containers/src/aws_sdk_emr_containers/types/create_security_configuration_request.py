"""Generated from Smithy shape ``com.amazonaws.emrcontainers#CreateSecurityConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_emr_containers.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_emr_containers.types.client_token
    import aws_sdk_emr_containers.types.container_provider
    import aws_sdk_emr_containers.types.resource_name_string
    import aws_sdk_emr_containers.types.security_configuration_data
    import aws_sdk_emr_containers.types.tag_map


class CreateSecurityConfigurationRequest(TypedDict, closed=True):
    client_token: "aws_sdk_emr_containers.types.client_token.ClientToken"
    """<p>The client idempotency token to use when creating the security configuration.</p>"""
    name: "aws_sdk_emr_containers.types.resource_name_string.ResourceNameString"
    """<p>The name of the security configuration.</p>"""
    container_provider: NotRequired[
        "aws_sdk_emr_containers.types.container_provider.ContainerProvider"
    ]
    """<p>The container provider associated with the security configuration.</p>"""
    security_configuration_data: "aws_sdk_emr_containers.types.security_configuration_data.SecurityConfigurationData"
    """<p>Security configuration input for the request.</p>"""
    tags: NotRequired["aws_sdk_emr_containers.types.tag_map.TagMap"]
    """<p>The tags to add to the security configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSecurityConfigurationRequest) -> dict:
    out: dict = {}
    out["clientToken"] = value["client_token"]
    out["name"] = value["name"]
    if "container_provider" in value:
        import aws_sdk_emr_containers.types.container_provider

        out["containerProvider"] = (
            aws_sdk_emr_containers.types.container_provider.serialize_json(
                value["container_provider"]
            )
        )
    import aws_sdk_emr_containers.types.security_configuration_data

    out["securityConfigurationData"] = (
        aws_sdk_emr_containers.types.security_configuration_data.serialize_json(
            value["security_configuration_data"]
        )
    )
    if "tags" in value:
        import aws_sdk_emr_containers.types.tag_map

        out["tags"] = aws_sdk_emr_containers.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateSecurityConfigurationRequest:
    out: CreateSecurityConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    else:
        raise DeserializationError(
            "CreateSecurityConfigurationRequest.client_token required"
        )
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateSecurityConfigurationRequest.name required")
    if "containerProvider" in data:
        import aws_sdk_emr_containers.types.container_provider

        out["container_provider"] = (
            aws_sdk_emr_containers.types.container_provider.deserialize_json(
                data["containerProvider"]
            )
        )
    if "securityConfigurationData" in data:
        import aws_sdk_emr_containers.types.security_configuration_data

        out["security_configuration_data"] = (
            aws_sdk_emr_containers.types.security_configuration_data.deserialize_json(
                data["securityConfigurationData"]
            )
        )
    else:
        raise DeserializationError(
            "CreateSecurityConfigurationRequest.security_configuration_data required"
        )
    if "tags" in data:
        import aws_sdk_emr_containers.types.tag_map

        out["tags"] = aws_sdk_emr_containers.types.tag_map.deserialize_json(
            data["tags"]
        )
    return out
