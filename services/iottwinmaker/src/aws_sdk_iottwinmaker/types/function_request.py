"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#FunctionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.data_connector
    import aws_sdk_iottwinmaker.types.required_properties
    import aws_sdk_iottwinmaker.types.scope


class FunctionRequest(TypedDict, closed=True):
    required_properties: NotRequired[
        "aws_sdk_iottwinmaker.types.required_properties.RequiredProperties"
    ]
    """<p>The required properties of the function.</p>"""
    scope: NotRequired["aws_sdk_iottwinmaker.types.scope.Scope"]
    """<p>The scope of the function.</p>"""
    implemented_by: NotRequired[
        "aws_sdk_iottwinmaker.types.data_connector.DataConnector"
    ]
    """<p>The data connector.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FunctionRequest) -> dict:
    out: dict = {}
    if "required_properties" in value:
        import aws_sdk_iottwinmaker.types.required_properties

        out["requiredProperties"] = (
            aws_sdk_iottwinmaker.types.required_properties.serialize_json(
                value["required_properties"]
            )
        )
    if "scope" in value:
        out["scope"] = value["scope"]
    if "implemented_by" in value:
        import aws_sdk_iottwinmaker.types.data_connector

        out["implementedBy"] = aws_sdk_iottwinmaker.types.data_connector.serialize_json(
            value["implemented_by"]
        )
    return out


def deserialize_json(data: dict) -> FunctionRequest:
    out: FunctionRequest = {}  # type: ignore[typeddict-item]
    if "requiredProperties" in data:
        import aws_sdk_iottwinmaker.types.required_properties

        out["required_properties"] = (
            aws_sdk_iottwinmaker.types.required_properties.deserialize_json(
                data["requiredProperties"]
            )
        )
    if "scope" in data:
        out["scope"] = data["scope"]
    if "implementedBy" in data:
        import aws_sdk_iottwinmaker.types.data_connector

        out["implemented_by"] = (
            aws_sdk_iottwinmaker.types.data_connector.deserialize_json(
                data["implementedBy"]
            )
        )
    return out
