"""Generated from Smithy shape ``com.amazonaws.ram#PromotePermissionCreatedFromPolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ram.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ram.types.string


class PromotePermissionCreatedFromPolicyRequest(TypedDict):
    permission_arn: "aws_sdk_ram.types.string.String"
    """<p>Specifies the <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Name (ARN)</a> of the <code>CREATED_FROM_POLICY</code> permission that you want to promote. You can get this <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Name (ARN)</a> by calling the <a>ListResourceSharePermissions</a> operation.</p>"""
    name: "aws_sdk_ram.types.string.String"
    """<p>Specifies a name for the promoted customer managed permission.</p>"""
    client_token: NotRequired["aws_sdk_ram.types.string.String"]
    """<p>Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a <a href=\"https://wikipedia.org/wiki/Universally_unique_identifier\">UUID type of value.</a>.</p> <p>If you don't provide this value, then Amazon Web Services generates a random one for you.</p> <p>If you retry the operation with the same <code>ClientToken</code>, but with different parameters, the retry fails with an <code>IdempotentParameterMismatch</code> error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PromotePermissionCreatedFromPolicyRequest) -> dict:
    out: dict = {}
    out["permissionArn"] = value["permission_arn"]
    out["name"] = value["name"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> PromotePermissionCreatedFromPolicyRequest:
    out: PromotePermissionCreatedFromPolicyRequest = {}  # type: ignore[typeddict-item]
    if "permissionArn" in data:
        out["permission_arn"] = data["permissionArn"]
    else:
        raise DeserializationError(
            "PromotePermissionCreatedFromPolicyRequest.permission_arn required"
        )
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError(
            "PromotePermissionCreatedFromPolicyRequest.name required"
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
