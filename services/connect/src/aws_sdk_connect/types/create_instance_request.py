"""Generated from Smithy shape ``com.amazonaws.connect#CreateInstanceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.client_token
    import aws_sdk_connect.types.directory_alias
    import aws_sdk_connect.types.directory_id
    import aws_sdk_connect.types.directory_type
    import aws_sdk_connect.types.inbound_calls_enabled
    import aws_sdk_connect.types.outbound_calls_enabled
    import aws_sdk_connect.types.tag_map


class CreateInstanceRequest(TypedDict, closed=True):
    client_token: NotRequired["aws_sdk_connect.types.client_token.ClientToken"]
    """<p>The idempotency token.</p>"""
    identity_management_type: "aws_sdk_connect.types.directory_type.DirectoryType"
    """<p>The type of identity management for your Connect Customer users.</p>"""
    instance_alias: NotRequired["aws_sdk_connect.types.directory_alias.DirectoryAlias"]
    """<p>The name for your instance.</p>"""
    directory_id: NotRequired["aws_sdk_connect.types.directory_id.DirectoryId"]
    """<p>The identifier for the directory.</p>"""
    inbound_calls_enabled: (
        "aws_sdk_connect.types.inbound_calls_enabled.InboundCallsEnabled"
    )
    """<p>Your contact center handles incoming contacts.</p>"""
    outbound_calls_enabled: (
        "aws_sdk_connect.types.outbound_calls_enabled.OutboundCallsEnabled"
    )
    """<p>Your contact center allows outbound calls.</p>"""
    tags: NotRequired["aws_sdk_connect.types.tag_map.TagMap"]
    r"""<p>The tags used to organize, track, or control access for this resource. For example, <code>{ \"tags\": {\"key1\":\"value1\", \"key2\":\"value2\"} }</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateInstanceRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    import aws_sdk_connect.types.directory_type

    out["IdentityManagementType"] = aws_sdk_connect.types.directory_type.serialize_json(
        value["identity_management_type"]
    )
    if "instance_alias" in value:
        out["InstanceAlias"] = value["instance_alias"]
    if "directory_id" in value:
        out["DirectoryId"] = value["directory_id"]
    out["InboundCallsEnabled"] = value["inbound_calls_enabled"]
    out["OutboundCallsEnabled"] = value["outbound_calls_enabled"]
    if "tags" in value:
        import aws_sdk_connect.types.tag_map

        out["Tags"] = aws_sdk_connect.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateInstanceRequest:
    out: CreateInstanceRequest = {}  # type: ignore[typeddict-item]
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    if "IdentityManagementType" in data:
        import aws_sdk_connect.types.directory_type

        out["identity_management_type"] = (
            aws_sdk_connect.types.directory_type.deserialize_json(
                data["IdentityManagementType"]
            )
        )
    else:
        raise DeserializationError(
            "CreateInstanceRequest.identity_management_type required"
        )
    if "InstanceAlias" in data:
        out["instance_alias"] = data["InstanceAlias"]
    if "DirectoryId" in data:
        out["directory_id"] = data["DirectoryId"]
    if "InboundCallsEnabled" in data:
        out["inbound_calls_enabled"] = data["InboundCallsEnabled"]
    else:
        raise DeserializationError(
            "CreateInstanceRequest.inbound_calls_enabled required"
        )
    if "OutboundCallsEnabled" in data:
        out["outbound_calls_enabled"] = data["OutboundCallsEnabled"]
    else:
        raise DeserializationError(
            "CreateInstanceRequest.outbound_calls_enabled required"
        )
    if "Tags" in data:
        import aws_sdk_connect.types.tag_map

        out["tags"] = aws_sdk_connect.types.tag_map.deserialize_json(data["Tags"])
    return out
