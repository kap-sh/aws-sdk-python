"""Generated from Smithy shape ``com.amazonaws.securityhub#GetSecurityControlDefinitionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.security_control_definition


class GetSecurityControlDefinitionResponse(TypedDict, closed=True):
    security_control_definition: NotRequired[
        "capo_securityhub.types.security_control_definition.SecurityControlDefinition"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: GetSecurityControlDefinitionResponse) -> dict:
    out: dict = {}
    if "security_control_definition" in value:
        import capo_securityhub.types.security_control_definition

        out["SecurityControlDefinition"] = (
            capo_securityhub.types.security_control_definition.serialize_json(
                value["security_control_definition"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetSecurityControlDefinitionResponse:
    out: GetSecurityControlDefinitionResponse = {}  # type: ignore[typeddict-item]
    if "SecurityControlDefinition" in data:
        import capo_securityhub.types.security_control_definition

        out["security_control_definition"] = (
            capo_securityhub.types.security_control_definition.deserialize_json(
                data["SecurityControlDefinition"]
            )
        )
    return out
