"""Generated from Smithy shape ``com.amazonaws.connect#ReplicateInstanceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.aws_region
    import aws_sdk_connect.types.client_token
    import aws_sdk_connect.types.directory_alias
    import aws_sdk_connect.types.instance_id_or_arn


class ReplicateInstanceRequest(TypedDict, closed=True):
    instance_id: "aws_sdk_connect.types.instance_id_or_arn.InstanceIdOrArn"
    r"""<p>The identifier of the Connect Customer instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance. You can provide the <code>InstanceId</code>, or the entire ARN.</p>"""
    replica_region: "aws_sdk_connect.types.aws_region.AwsRegion"
    """<p>The Amazon Web Services Region where to replicate the Connect Customer instance.</p>"""
    client_token: NotRequired["aws_sdk_connect.types.client_token.ClientToken"]
    r"""<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href=\"https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/\">Making retries safe with idempotent APIs</a>.</p>"""
    replica_alias: "aws_sdk_connect.types.directory_alias.DirectoryAlias"
    """<p>The alias for the replicated instance. The <code>ReplicaAlias</code> must be unique.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReplicateInstanceRequest) -> dict:
    out: dict = {}
    out["ReplicaRegion"] = value["replica_region"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    out["ReplicaAlias"] = value["replica_alias"]
    return out


def deserialize_json(data: dict) -> ReplicateInstanceRequest:
    out: ReplicateInstanceRequest = {}  # type: ignore[typeddict-item]
    if "ReplicaRegion" in data:
        out["replica_region"] = data["ReplicaRegion"]
    else:
        raise DeserializationError("ReplicateInstanceRequest.replica_region required")
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    if "ReplicaAlias" in data:
        out["replica_alias"] = data["ReplicaAlias"]
    else:
        raise DeserializationError("ReplicateInstanceRequest.replica_alias required")
    return out
