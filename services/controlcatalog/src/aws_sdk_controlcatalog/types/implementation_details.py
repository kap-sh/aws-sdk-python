"""Generated from Smithy shape ``com.amazonaws.controlcatalog#ImplementationDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_controlcatalog.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_controlcatalog.types.implementation_identifier
    import aws_sdk_controlcatalog.types.implementation_type


class ImplementationDetails(TypedDict):
    type: "aws_sdk_controlcatalog.types.implementation_type.ImplementationType"
    """<p>A string that describes a control's implementation type.</p>"""
    identifier: NotRequired[
        "aws_sdk_controlcatalog.types.implementation_identifier.ImplementationIdentifier"
    ]
    """<p>A service-specific identifier for the control, assigned by the service that implemented the control. For example, this identifier could be an Amazon Web Services Config Rule ID or a Security Hub Control ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImplementationDetails) -> dict:
    out: dict = {}
    out["Type"] = value["type"]
    if "identifier" in value:
        out["Identifier"] = value["identifier"]
    return out


def deserialize_json(data: dict) -> ImplementationDetails:
    out: ImplementationDetails = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        out["type"] = data["Type"]
    else:
        raise DeserializationError("ImplementationDetails.type required")
    if "Identifier" in data:
        out["identifier"] = data["Identifier"]
    return out
