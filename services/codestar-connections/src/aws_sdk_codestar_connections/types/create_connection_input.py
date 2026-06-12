"""Generated from Smithy shape ``com.amazonaws.codestarconnections#CreateConnectionInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_codestar_connections.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codestar_connections.types.connection_name
    import aws_sdk_codestar_connections.types.host_arn
    import aws_sdk_codestar_connections.types.provider_type
    import aws_sdk_codestar_connections.types.tag_list


class CreateConnectionInput(TypedDict):
    provider_type: NotRequired[
        "aws_sdk_codestar_connections.types.provider_type.ProviderType"
    ]
    """<p>The name of the external provider where your third-party code repository is configured.</p>"""
    connection_name: "aws_sdk_codestar_connections.types.connection_name.ConnectionName"
    """<p>The name of the connection to be created.</p>"""
    tags: NotRequired["aws_sdk_codestar_connections.types.tag_list.TagList"]
    """<p>The key-value pair to use when tagging the resource.</p>"""
    host_arn: NotRequired["aws_sdk_codestar_connections.types.host_arn.HostArn"]
    """<p>The Amazon Resource Name (ARN) of the host associated with the connection to be created.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateConnectionInput) -> dict:
    out: dict = {}
    if "provider_type" in value:
        import aws_sdk_codestar_connections.types.provider_type

        out["ProviderType"] = (
            aws_sdk_codestar_connections.types.provider_type.serialize_aws_json_1_0(
                value["provider_type"]
            )
        )
    out["ConnectionName"] = value["connection_name"]
    if "tags" in value:
        import aws_sdk_codestar_connections.types.tag_list

        out["Tags"] = (
            aws_sdk_codestar_connections.types.tag_list.serialize_aws_json_1_0(
                value["tags"]
            )
        )
    if "host_arn" in value:
        out["HostArn"] = value["host_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateConnectionInput:
    out: CreateConnectionInput = {}  # type: ignore[typeddict-item]
    if "ProviderType" in data:
        import aws_sdk_codestar_connections.types.provider_type

        out["provider_type"] = (
            aws_sdk_codestar_connections.types.provider_type.deserialize_aws_json_1_0(
                data["ProviderType"]
            )
        )
    if "ConnectionName" in data:
        out["connection_name"] = data["ConnectionName"]
    else:
        raise DeserializationError("CreateConnectionInput.connection_name required")
    if "Tags" in data:
        import aws_sdk_codestar_connections.types.tag_list

        out["tags"] = (
            aws_sdk_codestar_connections.types.tag_list.deserialize_aws_json_1_0(
                data["Tags"]
            )
        )
    if "HostArn" in data:
        out["host_arn"] = data["HostArn"]
    return out
