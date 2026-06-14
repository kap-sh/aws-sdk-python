"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#ParameterConstraints``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.__boolean


class ParameterConstraints(TypedDict):
    required: NotRequired["aws_sdk_apigatewayv2.types.__boolean.__boolean"]
    """<p>Whether or not the parameter is required.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ParameterConstraints) -> dict:
    out: dict = {}
    if "required" in value:
        out["required"] = value["required"]
    return out


def deserialize_json(data: dict) -> ParameterConstraints:
    out: ParameterConstraints = {}  # type: ignore[typeddict-item]
    if "required" in data:
        out["required"] = data["required"]
    return out
