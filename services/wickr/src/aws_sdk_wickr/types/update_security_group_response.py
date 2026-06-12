"""Generated from Smithy shape ``com.amazonaws.wickr#UpdateSecurityGroupResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_wickr.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_wickr.types.security_group


class UpdateSecurityGroupResponse(TypedDict):
    security_group: "aws_sdk_wickr.types.security_group.SecurityGroup"
    """<p>The updated security group details, including the new settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSecurityGroupResponse) -> dict:
    out: dict = {}
    import aws_sdk_wickr.types.security_group

    out["securityGroup"] = aws_sdk_wickr.types.security_group.serialize_json(
        value["security_group"]
    )
    return out


def deserialize_json(data: dict) -> UpdateSecurityGroupResponse:
    out: UpdateSecurityGroupResponse = {}  # type: ignore[typeddict-item]
    if "securityGroup" in data:
        import aws_sdk_wickr.types.security_group

        out["security_group"] = aws_sdk_wickr.types.security_group.deserialize_json(
            data["securityGroup"]
        )
    else:
        raise DeserializationError(
            "UpdateSecurityGroupResponse.security_group required"
        )
    return out
