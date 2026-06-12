"""Generated from Smithy shape ``com.amazonaws.iot#DetachThingPrincipalRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.principal
    import aws_sdk_iot.types.thing_name


class DetachThingPrincipalRequest(TypedDict):
    thing_name: "aws_sdk_iot.types.thing_name.ThingName"
    """<p>The name of the thing.</p>"""
    principal: "aws_sdk_iot.types.principal.Principal"
    """<p>If the principal is a certificate, this value must be ARN of the certificate. If the principal is an Amazon Cognito identity, this value must be the ID of the Amazon Cognito identity.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DetachThingPrincipalRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DetachThingPrincipalRequest:
    out: DetachThingPrincipalRequest = {}  # type: ignore[typeddict-item]
    return out
