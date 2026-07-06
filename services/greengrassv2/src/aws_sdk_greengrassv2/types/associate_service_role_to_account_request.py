"""Generated from Smithy shape ``com.amazonaws.greengrassv2#AssociateServiceRoleToAccountRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_greengrassv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_greengrassv2.types.string


class AssociateServiceRoleToAccountRequest(TypedDict, closed=True):
    role_arn: "aws_sdk_greengrassv2.types.string.String"
    """<p>The Amazon Resource Name (ARN) of the service role to associate with IoT Greengrass for your Amazon Web Services account in this Amazon Web Services Region.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateServiceRoleToAccountRequest) -> dict:
    out: dict = {}
    out["RoleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> AssociateServiceRoleToAccountRequest:
    out: AssociateServiceRoleToAccountRequest = {}  # type: ignore[typeddict-item]
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    else:
        raise DeserializationError(
            "AssociateServiceRoleToAccountRequest.role_arn required"
        )
    return out
