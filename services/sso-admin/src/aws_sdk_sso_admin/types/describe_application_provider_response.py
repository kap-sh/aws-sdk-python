"""Generated from Smithy shape ``com.amazonaws.ssoadmin#DescribeApplicationProviderResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_sso_admin.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.application_provider_arn
    import aws_sdk_sso_admin.types.display_data
    import aws_sdk_sso_admin.types.federation_protocol
    import aws_sdk_sso_admin.types.resource_server_config


class DescribeApplicationProviderResponse(TypedDict, closed=True):
    application_provider_arn: (
        "aws_sdk_sso_admin.types.application_provider_arn.ApplicationProviderArn"
    )
    """<p>The ARN of the application provider.</p>"""
    federation_protocol: NotRequired[
        "aws_sdk_sso_admin.types.federation_protocol.FederationProtocol"
    ]
    """<p>The protocol used to federate to the application provider.</p>"""
    display_data: NotRequired["aws_sdk_sso_admin.types.display_data.DisplayData"]
    """<p>A structure with details about the display data for the application provider.</p>"""
    resource_server_config: NotRequired[
        "aws_sdk_sso_admin.types.resource_server_config.ResourceServerConfig"
    ]
    """<p>A structure with details about the receiving application.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeApplicationProviderResponse) -> dict:
    out: dict = {}
    out["ApplicationProviderArn"] = value["application_provider_arn"]
    if "federation_protocol" in value:
        import aws_sdk_sso_admin.types.federation_protocol

        out["FederationProtocol"] = (
            aws_sdk_sso_admin.types.federation_protocol.serialize_aws_json_1_1(
                value["federation_protocol"]
            )
        )
    if "display_data" in value:
        import aws_sdk_sso_admin.types.display_data

        out["DisplayData"] = (
            aws_sdk_sso_admin.types.display_data.serialize_aws_json_1_1(
                value["display_data"]
            )
        )
    if "resource_server_config" in value:
        import aws_sdk_sso_admin.types.resource_server_config

        out["ResourceServerConfig"] = (
            aws_sdk_sso_admin.types.resource_server_config.serialize_aws_json_1_1(
                value["resource_server_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeApplicationProviderResponse:
    out: DescribeApplicationProviderResponse = {}  # type: ignore[typeddict-item]
    if "ApplicationProviderArn" in data:
        out["application_provider_arn"] = data["ApplicationProviderArn"]
    else:
        raise DeserializationError(
            "DescribeApplicationProviderResponse.application_provider_arn required"
        )
    if "FederationProtocol" in data:
        import aws_sdk_sso_admin.types.federation_protocol

        out["federation_protocol"] = (
            aws_sdk_sso_admin.types.federation_protocol.deserialize_aws_json_1_1(
                data["FederationProtocol"]
            )
        )
    if "DisplayData" in data:
        import aws_sdk_sso_admin.types.display_data

        out["display_data"] = (
            aws_sdk_sso_admin.types.display_data.deserialize_aws_json_1_1(
                data["DisplayData"]
            )
        )
    if "ResourceServerConfig" in data:
        import aws_sdk_sso_admin.types.resource_server_config

        out["resource_server_config"] = (
            aws_sdk_sso_admin.types.resource_server_config.deserialize_aws_json_1_1(
                data["ResourceServerConfig"]
            )
        )
    return out
