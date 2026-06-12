"""Generated from Smithy shape ``com.amazonaws.securityhub#ListSecurityControlDefinitionsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.next_token
    import aws_sdk_securityhub.types.security_control_definitions


class ListSecurityControlDefinitionsResponse(TypedDict):
    security_control_definitions: NotRequired[
        "aws_sdk_securityhub.types.security_control_definitions.SecurityControlDefinitions"
    ]
    """<p> An array of controls that apply to the specified standard. </p>"""
    next_token: NotRequired["aws_sdk_securityhub.types.next_token.NextToken"]
    """<p> A pagination parameter that's included in the response only if it was included in the request. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSecurityControlDefinitionsResponse) -> dict:
    out: dict = {}
    if "security_control_definitions" in value:
        import aws_sdk_securityhub.types.security_control_definitions

        out["SecurityControlDefinitions"] = (
            aws_sdk_securityhub.types.security_control_definitions.serialize_json(
                value["security_control_definitions"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSecurityControlDefinitionsResponse:
    out: ListSecurityControlDefinitionsResponse = {}  # type: ignore[typeddict-item]
    if "SecurityControlDefinitions" in data:
        import aws_sdk_securityhub.types.security_control_definitions

        out["security_control_definitions"] = (
            aws_sdk_securityhub.types.security_control_definitions.deserialize_json(
                data["SecurityControlDefinitions"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
