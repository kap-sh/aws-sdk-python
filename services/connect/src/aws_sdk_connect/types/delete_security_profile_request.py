"""Generated from Smithy shape ``com.amazonaws.connect#DeleteSecurityProfileRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.instance_id
    import aws_sdk_connect.types.security_profile_id


class DeleteSecurityProfileRequest(TypedDict):
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    r"""<p>The identifier of the Connect Customer instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    security_profile_id: "aws_sdk_connect.types.security_profile_id.SecurityProfileId"
    """<p>The identifier for the security profle.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteSecurityProfileRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteSecurityProfileRequest:
    out: DeleteSecurityProfileRequest = {}  # type: ignore[typeddict-item]
    return out
