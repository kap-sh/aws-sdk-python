"""Generated from Smithy shape ``com.amazonaws.medialive#UpdateInputSecurityGroupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.input_security_group


class UpdateInputSecurityGroupResponse(TypedDict, closed=True):
    security_group: NotRequired[
        "capo_medialive.types.input_security_group.InputSecurityGroup"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateInputSecurityGroupResponse) -> dict:
    out: dict = {}
    if "security_group" in value:
        import capo_medialive.types.input_security_group

        out["securityGroup"] = capo_medialive.types.input_security_group.serialize_json(
            value["security_group"]
        )
    return out


def deserialize_json(data: dict) -> UpdateInputSecurityGroupResponse:
    out: UpdateInputSecurityGroupResponse = {}  # type: ignore[typeddict-item]
    if "securityGroup" in data:
        import capo_medialive.types.input_security_group

        out["security_group"] = (
            capo_medialive.types.input_security_group.deserialize_json(
                data["securityGroup"]
            )
        )
    return out
