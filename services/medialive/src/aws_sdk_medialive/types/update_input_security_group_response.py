"""Generated from Smithy shape ``com.amazonaws.medialive#UpdateInputSecurityGroupResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.input_security_group


class UpdateInputSecurityGroupResponse(TypedDict):
    security_group: NotRequired[
        "aws_sdk_medialive.types.input_security_group.InputSecurityGroup"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateInputSecurityGroupResponse) -> dict:
    out: dict = {}
    if "security_group" in value:
        import aws_sdk_medialive.types.input_security_group

        out["securityGroup"] = (
            aws_sdk_medialive.types.input_security_group.serialize_json(
                value["security_group"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateInputSecurityGroupResponse:
    out: UpdateInputSecurityGroupResponse = {}  # type: ignore[typeddict-item]
    if "securityGroup" in data:
        import aws_sdk_medialive.types.input_security_group

        out["security_group"] = (
            aws_sdk_medialive.types.input_security_group.deserialize_json(
                data["securityGroup"]
            )
        )
    return out
