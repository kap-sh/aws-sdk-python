"""Generated from Smithy shape ``com.amazonaws.interconnect#CreateConnectionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_interconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_interconnect.types.attach_point
    import aws_sdk_interconnect.types.connection_bandwidth
    import aws_sdk_interconnect.types.connection_description
    import aws_sdk_interconnect.types.environment_id
    import aws_sdk_interconnect.types.remote_account_identifier
    import aws_sdk_interconnect.types.tag_map


class CreateConnectionRequest(TypedDict, closed=True):
    description: NotRequired[
        "aws_sdk_interconnect.types.connection_description.ConnectionDescription"
    ]
    """<p>A description to distinguish this <a>Connection</a>.</p>"""
    bandwidth: "aws_sdk_interconnect.types.connection_bandwidth.ConnectionBandwidth"
    """<p>The desired bandwidth of the requested <a>Connection</a> </p>"""
    attach_point: "aws_sdk_interconnect.types.attach_point.AttachPoint"
    r"""<p>The Attach Point to which the connection should be associated.\"</p>"""
    environment_id: "aws_sdk_interconnect.types.environment_id.EnvironmentId"
    """<p>The identifier of the <a>Environment</a> across which this <a>Connection</a> should be created.</p> <p>The available <a>Environment</a> objects can be determined using <a>ListEnvironments</a>.</p>"""
    remote_account: NotRequired[
        "aws_sdk_interconnect.types.remote_account_identifier.RemoteAccountIdentifier"
    ]
    """<p>Account and/or principal identifying information that can be verified by the partner of this specific Environment.</p>"""
    tags: NotRequired["aws_sdk_interconnect.types.tag_map.TagMap"]
    """<p>The tag to associate with the resulting <a>Connection</a>.</p>"""
    client_token: NotRequired["str"]
    """<p>Idempotency token used for the request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateConnectionRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    out["bandwidth"] = value["bandwidth"]
    import aws_sdk_interconnect.types.attach_point

    out["attachPoint"] = aws_sdk_interconnect.types.attach_point.serialize_aws_json_1_0(
        value["attach_point"]
    )
    out["environmentId"] = value["environment_id"]
    if "remote_account" in value:
        import aws_sdk_interconnect.types.remote_account_identifier

        out["remoteAccount"] = (
            aws_sdk_interconnect.types.remote_account_identifier.serialize_aws_json_1_0(
                value["remote_account"]
            )
        )
    if "tags" in value:
        import aws_sdk_interconnect.types.tag_map

        out["tags"] = aws_sdk_interconnect.types.tag_map.serialize_aws_json_1_0(
            value["tags"]
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateConnectionRequest:
    out: CreateConnectionRequest = {}  # type: ignore[typeddict-item]
    if "description" in data:
        out["description"] = data["description"]
    if "bandwidth" in data:
        out["bandwidth"] = data["bandwidth"]
    else:
        raise DeserializationError("CreateConnectionRequest.bandwidth required")
    if "attachPoint" in data:
        import aws_sdk_interconnect.types.attach_point

        out["attach_point"] = (
            aws_sdk_interconnect.types.attach_point.deserialize_aws_json_1_0(
                data["attachPoint"]
            )
        )
    else:
        raise DeserializationError("CreateConnectionRequest.attach_point required")
    if "environmentId" in data:
        out["environment_id"] = data["environmentId"]
    else:
        raise DeserializationError("CreateConnectionRequest.environment_id required")
    if "remoteAccount" in data:
        import aws_sdk_interconnect.types.remote_account_identifier

        out["remote_account"] = (
            aws_sdk_interconnect.types.remote_account_identifier.deserialize_aws_json_1_0(
                data["remoteAccount"]
            )
        )
    if "tags" in data:
        import aws_sdk_interconnect.types.tag_map

        out["tags"] = aws_sdk_interconnect.types.tag_map.deserialize_aws_json_1_0(
            data["tags"]
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
