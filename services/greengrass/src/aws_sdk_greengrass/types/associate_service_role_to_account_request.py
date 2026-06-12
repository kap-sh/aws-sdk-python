"""Generated from Smithy shape ``com.amazonaws.greengrass#AssociateServiceRoleToAccountRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.__string


class AssociateServiceRoleToAccountRequest(TypedDict):
    role_arn: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """The ARN of the service role you wish to associate with your account."""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateServiceRoleToAccountRequest) -> dict:
    out: dict = {}
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> AssociateServiceRoleToAccountRequest:
    out: AssociateServiceRoleToAccountRequest = {}  # type: ignore[typeddict-item]
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    return out
