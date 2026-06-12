"""Generated from Smithy shape ``com.amazonaws.connect#DisassociateInstanceStorageConfigRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.association_id
    import aws_sdk_connect.types.client_token
    import aws_sdk_connect.types.instance_id
    import aws_sdk_connect.types.instance_storage_resource_type


class DisassociateInstanceStorageConfigRequest(TypedDict):
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    association_id: "aws_sdk_connect.types.association_id.AssociationId"
    """<p>The existing association identifier that uniquely identifies the resource type and storage config for the given instance ID.</p>"""
    resource_type: "aws_sdk_connect.types.instance_storage_resource_type.InstanceStorageResourceType"
    """<p>A valid resource type.</p>"""
    client_token: NotRequired["aws_sdk_connect.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href=\"https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/\">Making retries safe with idempotent APIs</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateInstanceStorageConfigRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DisassociateInstanceStorageConfigRequest:
    out: DisassociateInstanceStorageConfigRequest = {}  # type: ignore[typeddict-item]
    return out
