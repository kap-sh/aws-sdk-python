"""Generated from Smithy shape ``com.amazonaws.servicediscovery#GetOperationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_servicediscovery.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_servicediscovery.types.aws_account_id
    import aws_sdk_servicediscovery.types.operation_id


class GetOperationRequest(TypedDict):
    operation_id: "aws_sdk_servicediscovery.types.operation_id.OperationId"
    """<p>The ID of the operation that you want to get more information about.</p>"""
    owner_account: NotRequired[
        "aws_sdk_servicediscovery.types.aws_account_id.AWSAccountId"
    ]
    """<p>The ID of the Amazon Web Services account that owns the namespace associated with the operation, as specified in the namespace <code>ResourceOwner</code> field. For operations associated with namespaces that are shared with your account, you must specify an <code>OwnerAccount</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetOperationRequest) -> dict:
    out: dict = {}
    out["OperationId"] = value["operation_id"]
    if "owner_account" in value:
        out["OwnerAccount"] = value["owner_account"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetOperationRequest:
    out: GetOperationRequest = {}  # type: ignore[typeddict-item]
    if "OperationId" in data:
        out["operation_id"] = data["OperationId"]
    else:
        raise DeserializationError("GetOperationRequest.operation_id required")
    if "OwnerAccount" in data:
        out["owner_account"] = data["OwnerAccount"]
    return out
