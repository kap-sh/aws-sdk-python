"""Generated from Smithy shape ``com.amazonaws.wickr#CreateSecurityGroupResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_wickr.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_wickr.types.security_group


class CreateSecurityGroupResponse(TypedDict):
    security_group: "aws_sdk_wickr.types.security_group.SecurityGroup"
    """<p>The details of the newly created security group, including its ID, name, and settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSecurityGroupResponse) -> dict:
    out: dict = {}
    import aws_sdk_wickr.types.security_group

    out["securityGroup"] = aws_sdk_wickr.types.security_group.serialize_json(
        value["security_group"]
    )
    return out


def deserialize_json(data: dict) -> CreateSecurityGroupResponse:
    out: CreateSecurityGroupResponse = {}  # type: ignore[typeddict-item]
    if "securityGroup" in data:
        import aws_sdk_wickr.types.security_group

        out["security_group"] = aws_sdk_wickr.types.security_group.deserialize_json(
            data["securityGroup"]
        )
    else:
        raise DeserializationError(
            "CreateSecurityGroupResponse.security_group required"
        )
    return out
