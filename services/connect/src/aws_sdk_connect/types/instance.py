"""Generated from Smithy shape ``com.amazonaws.connect#Instance``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.arn
    import aws_sdk_connect.types.directory_alias
    import aws_sdk_connect.types.directory_type
    import aws_sdk_connect.types.inbound_calls_enabled
    import aws_sdk_connect.types.instance_id
    import aws_sdk_connect.types.instance_status
    import aws_sdk_connect.types.instance_status_reason
    import aws_sdk_connect.types.outbound_calls_enabled
    import aws_sdk_connect.types.tag_map
    import aws_sdk_connect.types.timestamp
    import aws_sdk_connect.types.url


class Instance(TypedDict):
    id: NotRequired["aws_sdk_connect.types.instance_id.InstanceId"]
    r"""<p>The identifier of the Connect Customer instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    arn: NotRequired["aws_sdk_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the instance.</p>"""
    identity_management_type: NotRequired[
        "aws_sdk_connect.types.directory_type.DirectoryType"
    ]
    """<p>The identity management type.</p>"""
    instance_alias: NotRequired["aws_sdk_connect.types.directory_alias.DirectoryAlias"]
    """<p>The alias of instance.</p>"""
    created_time: NotRequired["aws_sdk_connect.types.timestamp.Timestamp"]
    """<p>When the instance was created.</p>"""
    service_role: NotRequired["aws_sdk_connect.types.arn.ARN"]
    """<p>The service role of the instance.</p>"""
    instance_status: NotRequired["aws_sdk_connect.types.instance_status.InstanceStatus"]
    """<p>The state of the instance.</p>"""
    status_reason: NotRequired[
        "aws_sdk_connect.types.instance_status_reason.InstanceStatusReason"
    ]
    """<p>Relevant details why the instance was not successfully created. </p>"""
    inbound_calls_enabled: NotRequired[
        "aws_sdk_connect.types.inbound_calls_enabled.InboundCallsEnabled"
    ]
    """<p>Whether inbound calls are enabled.</p>"""
    outbound_calls_enabled: NotRequired[
        "aws_sdk_connect.types.outbound_calls_enabled.OutboundCallsEnabled"
    ]
    """<p>Whether outbound calls are enabled.</p>"""
    instance_access_url: NotRequired["aws_sdk_connect.types.url.Url"]
    """<p>This URL allows contact center users to access the Connect Customer admin website.</p>"""
    tags: NotRequired["aws_sdk_connect.types.tag_map.TagMap"]
    """<p>The tags of an instance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Instance) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "identity_management_type" in value:
        import aws_sdk_connect.types.directory_type

        out["IdentityManagementType"] = (
            aws_sdk_connect.types.directory_type.serialize_json(
                value["identity_management_type"]
            )
        )
    if "instance_alias" in value:
        out["InstanceAlias"] = value["instance_alias"]
    if "created_time" in value:
        import aws_sdk_connect.types.timestamp

        out["CreatedTime"] = aws_sdk_connect.types.timestamp.serialize_json(
            value["created_time"]
        )
    if "service_role" in value:
        out["ServiceRole"] = value["service_role"]
    if "instance_status" in value:
        import aws_sdk_connect.types.instance_status

        out["InstanceStatus"] = aws_sdk_connect.types.instance_status.serialize_json(
            value["instance_status"]
        )
    if "status_reason" in value:
        import aws_sdk_connect.types.instance_status_reason

        out["StatusReason"] = (
            aws_sdk_connect.types.instance_status_reason.serialize_json(
                value["status_reason"]
            )
        )
    if "inbound_calls_enabled" in value:
        out["InboundCallsEnabled"] = value["inbound_calls_enabled"]
    if "outbound_calls_enabled" in value:
        out["OutboundCallsEnabled"] = value["outbound_calls_enabled"]
    if "instance_access_url" in value:
        out["InstanceAccessUrl"] = value["instance_access_url"]
    if "tags" in value:
        import aws_sdk_connect.types.tag_map

        out["Tags"] = aws_sdk_connect.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> Instance:
    out: Instance = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "IdentityManagementType" in data:
        import aws_sdk_connect.types.directory_type

        out["identity_management_type"] = (
            aws_sdk_connect.types.directory_type.deserialize_json(
                data["IdentityManagementType"]
            )
        )
    if "InstanceAlias" in data:
        out["instance_alias"] = data["InstanceAlias"]
    if "CreatedTime" in data:
        import aws_sdk_connect.types.timestamp

        out["created_time"] = aws_sdk_connect.types.timestamp.deserialize_json(
            data["CreatedTime"]
        )
    if "ServiceRole" in data:
        out["service_role"] = data["ServiceRole"]
    if "InstanceStatus" in data:
        import aws_sdk_connect.types.instance_status

        out["instance_status"] = aws_sdk_connect.types.instance_status.deserialize_json(
            data["InstanceStatus"]
        )
    if "StatusReason" in data:
        import aws_sdk_connect.types.instance_status_reason

        out["status_reason"] = (
            aws_sdk_connect.types.instance_status_reason.deserialize_json(
                data["StatusReason"]
            )
        )
    if "InboundCallsEnabled" in data:
        out["inbound_calls_enabled"] = data["InboundCallsEnabled"]
    if "OutboundCallsEnabled" in data:
        out["outbound_calls_enabled"] = data["OutboundCallsEnabled"]
    if "InstanceAccessUrl" in data:
        out["instance_access_url"] = data["InstanceAccessUrl"]
    if "Tags" in data:
        import aws_sdk_connect.types.tag_map

        out["tags"] = aws_sdk_connect.types.tag_map.deserialize_json(data["Tags"])
    return out
