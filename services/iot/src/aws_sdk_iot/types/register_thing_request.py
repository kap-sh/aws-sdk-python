"""Generated from Smithy shape ``com.amazonaws.iot#RegisterThingRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot.types.parameters
    import aws_sdk_iot.types.template_body


class RegisterThingRequest(TypedDict):
    template_body: "aws_sdk_iot.types.template_body.TemplateBody"
    """<p>The provisioning template. See <a href=\"https://docs.aws.amazon.com/iot/latest/developerguide/provision-w-cert.html\">Provisioning Devices That Have Device Certificates</a> for more information.</p>"""
    parameters: NotRequired["aws_sdk_iot.types.parameters.Parameters"]
    """<p>The parameters for provisioning a thing. See <a href=\"https://docs.aws.amazon.com/iot/latest/developerguide/provision-template.html\">Provisioning Templates</a> for more information.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisterThingRequest) -> dict:
    out: dict = {}
    out["templateBody"] = value["template_body"]
    if "parameters" in value:
        import aws_sdk_iot.types.parameters

        out["parameters"] = aws_sdk_iot.types.parameters.serialize_json(
            value["parameters"]
        )
    return out


def deserialize_json(data: dict) -> RegisterThingRequest:
    out: RegisterThingRequest = {}  # type: ignore[typeddict-item]
    if "templateBody" in data:
        out["template_body"] = data["templateBody"]
    else:
        raise DeserializationError("RegisterThingRequest.template_body required")
    if "parameters" in data:
        import aws_sdk_iot.types.parameters

        out["parameters"] = aws_sdk_iot.types.parameters.deserialize_json(
            data["parameters"]
        )
    return out
