"""Generated from Smithy shape ``com.amazonaws.controlcatalog#ImplementationSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_controlcatalog.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_controlcatalog.types.implementation_identifier
    import aws_sdk_controlcatalog.types.implementation_type


class ImplementationSummary(TypedDict):
    type: "aws_sdk_controlcatalog.types.implementation_type.ImplementationType"
    """<p>A string that represents the Amazon Web Services service that implements this control. For example, a value of <code>AWS::Config::ConfigRule</code> indicates that the control is implemented by Amazon Web Services Config, and <code>AWS::SecurityHub::SecurityControl</code> indicates implementation by Amazon Web Services Security Hub.</p>"""
    identifier: NotRequired[
        "aws_sdk_controlcatalog.types.implementation_identifier.ImplementationIdentifier"
    ]
    """<p>The identifier originally assigned by the Amazon Web Services service that implements the control. For example, <code>CODEPIPELINE_DEPLOYMENT_COUNT_CHECK</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImplementationSummary) -> dict:
    out: dict = {}
    out["Type"] = value["type"]
    if "identifier" in value:
        out["Identifier"] = value["identifier"]
    return out


def deserialize_json(data: dict) -> ImplementationSummary:
    out: ImplementationSummary = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        out["type"] = data["Type"]
    else:
        raise DeserializationError("ImplementationSummary.type required")
    if "Identifier" in data:
        out["identifier"] = data["Identifier"]
    return out
