"""Generated from Smithy shape ``com.amazonaws.wickr#GetSecurityGroupResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_wickr.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_wickr.types.security_group


class GetSecurityGroupResponse(TypedDict):
    security_group: "aws_sdk_wickr.types.security_group.SecurityGroup"
    """<p>The detailed information about the security group, including all its settings and member counts.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSecurityGroupResponse) -> dict:
    out: dict = {}
    import aws_sdk_wickr.types.security_group

    out["securityGroup"] = aws_sdk_wickr.types.security_group.serialize_json(
        value["security_group"]
    )
    return out


def deserialize_json(data: dict) -> GetSecurityGroupResponse:
    out: GetSecurityGroupResponse = {}  # type: ignore[typeddict-item]
    if "securityGroup" in data:
        import aws_sdk_wickr.types.security_group

        out["security_group"] = aws_sdk_wickr.types.security_group.deserialize_json(
            data["securityGroup"]
        )
    else:
        raise DeserializationError("GetSecurityGroupResponse.security_group required")
    return out
