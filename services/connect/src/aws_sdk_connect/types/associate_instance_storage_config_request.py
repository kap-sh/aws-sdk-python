"""Generated from Smithy shape ``com.amazonaws.connect#AssociateInstanceStorageConfigRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.client_token
    import aws_sdk_connect.types.instance_id
    import aws_sdk_connect.types.instance_storage_config
    import aws_sdk_connect.types.instance_storage_resource_type


class AssociateInstanceStorageConfigRequest(TypedDict):
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    resource_type: "aws_sdk_connect.types.instance_storage_resource_type.InstanceStorageResourceType"
    """<p>A valid resource type. To <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/enable-contact-analysis-segment-streams.html\">enable streaming for real-time analysis of contacts</a>, use the following types:</p> <ul> <li> <p>For chat contacts, use <code>REAL_TIME_CONTACT_ANALYSIS_CHAT_SEGMENTS</code>.</p> </li> <li> <p>For voice contacts, use <code>REAL_TIME_CONTACT_ANALYSIS_VOICE_SEGMENTS</code>.</p> </li> </ul> <note> <p> <code>REAL_TIME_CONTACT_ANALYSIS_SEGMENTS</code> is deprecated, but it is still supported and will apply only to VOICE channel contacts. Use <code>REAL_TIME_CONTACT_ANALYSIS_VOICE_SEGMENTS</code> for voice contacts moving forward.</p> <p>If you have previously associated a stream with <code>REAL_TIME_CONTACT_ANALYSIS_SEGMENTS</code>, no action is needed to update the stream to <code>REAL_TIME_CONTACT_ANALYSIS_VOICE_SEGMENTS</code>.</p> </note>"""
    storage_config: (
        "aws_sdk_connect.types.instance_storage_config.InstanceStorageConfig"
    )
    """<p>A valid storage type.</p>"""
    client_token: NotRequired["aws_sdk_connect.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href=\"https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/\">Making retries safe with idempotent APIs</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateInstanceStorageConfigRequest) -> dict:
    out: dict = {}
    import aws_sdk_connect.types.instance_storage_resource_type

    out["ResourceType"] = (
        aws_sdk_connect.types.instance_storage_resource_type.serialize_json(
            value["resource_type"]
        )
    )
    import aws_sdk_connect.types.instance_storage_config

    out["StorageConfig"] = aws_sdk_connect.types.instance_storage_config.serialize_json(
        value["storage_config"]
    )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> AssociateInstanceStorageConfigRequest:
    out: AssociateInstanceStorageConfigRequest = {}  # type: ignore[typeddict-item]
    if "ResourceType" in data:
        import aws_sdk_connect.types.instance_storage_resource_type

        out["resource_type"] = (
            aws_sdk_connect.types.instance_storage_resource_type.deserialize_json(
                data["ResourceType"]
            )
        )
    else:
        raise DeserializationError(
            "AssociateInstanceStorageConfigRequest.resource_type required"
        )
    if "StorageConfig" in data:
        import aws_sdk_connect.types.instance_storage_config

        out["storage_config"] = (
            aws_sdk_connect.types.instance_storage_config.deserialize_json(
                data["StorageConfig"]
            )
        )
    else:
        raise DeserializationError(
            "AssociateInstanceStorageConfigRequest.storage_config required"
        )
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    return out
