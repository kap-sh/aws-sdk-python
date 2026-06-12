"""Generated from Smithy shape ``com.amazonaws.synthetics#Dependency``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_synthetics.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_synthetics.types.dependency_type
    import aws_sdk_synthetics.types.string


class Dependency(TypedDict):
    type: NotRequired["aws_sdk_synthetics.types.dependency_type.DependencyType"]
    """<p>The type of dependency. Valid value is <code>LambdaLayer</code>.</p>"""
    reference: "aws_sdk_synthetics.types.string.String"
    """<p>The dependency reference. For Lambda layers, this is the ARN of the Lambda layer. For more information about Lambda ARN format, see <a href=\"https://docs.aws.amazon.com/lambda/latest/api/API_Layer.html\">Lambda</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Dependency) -> dict:
    out: dict = {}
    if "type" in value:
        import aws_sdk_synthetics.types.dependency_type

        out["Type"] = aws_sdk_synthetics.types.dependency_type.serialize_json(
            value["type"]
        )
    out["Reference"] = value["reference"]
    return out


def deserialize_json(data: dict) -> Dependency:
    out: Dependency = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import aws_sdk_synthetics.types.dependency_type

        out["type"] = aws_sdk_synthetics.types.dependency_type.deserialize_json(
            data["Type"]
        )
    if "Reference" in data:
        out["reference"] = data["Reference"]
    else:
        raise DeserializationError("Dependency.reference required")
    return out
