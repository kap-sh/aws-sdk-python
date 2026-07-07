"""Generated from Smithy shape ``com.amazonaws.apprunner#CreateConnectionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_apprunner.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_apprunner.types.connection_name
    import aws_sdk_apprunner.types.provider_type
    import aws_sdk_apprunner.types.tag_list


class CreateConnectionRequest(TypedDict, closed=True):
    connection_name: "aws_sdk_apprunner.types.connection_name.ConnectionName"
    """<p>A name for the new connection. It must be unique across all App Runner connections for the Amazon Web Services account in the Amazon Web Services Region.</p>"""
    provider_type: "aws_sdk_apprunner.types.provider_type.ProviderType"
    """<p>The source repository provider.</p>"""
    tags: NotRequired["aws_sdk_apprunner.types.tag_list.TagList"]
    """<p>A list of metadata items that you can associate with your connection resource. A tag is a key-value pair.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateConnectionRequest) -> dict:
    out: dict = {}
    out["ConnectionName"] = value["connection_name"]
    import aws_sdk_apprunner.types.provider_type

    out["ProviderType"] = aws_sdk_apprunner.types.provider_type.serialize_aws_json_1_0(
        value["provider_type"]
    )
    if "tags" in value:
        import aws_sdk_apprunner.types.tag_list

        out["Tags"] = aws_sdk_apprunner.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateConnectionRequest:
    out: CreateConnectionRequest = {}  # type: ignore[typeddict-item]
    if "ConnectionName" in data:
        out["connection_name"] = data["ConnectionName"]
    else:
        raise DeserializationError("CreateConnectionRequest.connection_name required")
    if "ProviderType" in data:
        import aws_sdk_apprunner.types.provider_type

        out["provider_type"] = (
            aws_sdk_apprunner.types.provider_type.deserialize_aws_json_1_0(
                data["ProviderType"]
            )
        )
    else:
        raise DeserializationError("CreateConnectionRequest.provider_type required")
    if "Tags" in data:
        import aws_sdk_apprunner.types.tag_list

        out["tags"] = aws_sdk_apprunner.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    return out
