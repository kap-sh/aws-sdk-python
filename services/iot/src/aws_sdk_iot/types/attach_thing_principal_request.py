"""Generated from Smithy shape ``com.amazonaws.iot#AttachThingPrincipalRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.principal
    import aws_sdk_iot.types.thing_name
    import aws_sdk_iot.types.thing_principal_type


class AttachThingPrincipalRequest(TypedDict, closed=True):
    thing_name: "aws_sdk_iot.types.thing_name.ThingName"
    """<p>The name of the thing.</p>"""
    principal: "aws_sdk_iot.types.principal.Principal"
    """<p>The principal, which can be a certificate ARN (as returned from the CreateCertificate operation) or an Amazon Cognito ID.</p>"""
    thing_principal_type: NotRequired[
        "aws_sdk_iot.types.thing_principal_type.ThingPrincipalType"
    ]
    """<p>The type of the relation you want to specify when you attach a principal to a thing.</p> <ul> <li> <p> <code>EXCLUSIVE_THING</code> - Attaches the specified principal to the specified thing, exclusively. The thing will be the only thing that’s attached to the principal.</p> </li> </ul> <ul> <li> <p> <code>NON_EXCLUSIVE_THING</code> - Attaches the specified principal to the specified thing. Multiple things can be attached to the principal.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: AttachThingPrincipalRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> AttachThingPrincipalRequest:
    out: AttachThingPrincipalRequest = {}  # type: ignore[typeddict-item]
    return out
