"""Generated from Smithy shape ``com.amazonaws.connect#AssociateSecurityKeyRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.client_token
    import aws_sdk_connect.types.instance_id
    import aws_sdk_connect.types.pem


class AssociateSecurityKeyRequest(TypedDict):
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    r"""<p>The identifier of the Connect Customer instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    key: "aws_sdk_connect.types.pem.PEM"
    """<p>A valid security key in PEM format as a String.</p>"""
    client_token: NotRequired["aws_sdk_connect.types.client_token.ClientToken"]
    r"""<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href=\"https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/\">Making retries safe with idempotent APIs</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateSecurityKeyRequest) -> dict:
    out: dict = {}
    out["Key"] = value["key"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> AssociateSecurityKeyRequest:
    out: AssociateSecurityKeyRequest = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        out["key"] = data["Key"]
    else:
        raise DeserializationError("AssociateSecurityKeyRequest.key required")
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    return out
