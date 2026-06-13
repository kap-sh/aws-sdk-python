"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AnalysisParameter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.parameter_name
    import aws_sdk_cleanrooms.types.parameter_type
    import aws_sdk_cleanrooms.types.parameter_value


class AnalysisParameter(TypedDict):
    name: "aws_sdk_cleanrooms.types.parameter_name.ParameterName"
    """<p>The name of the parameter. The name must use only alphanumeric or underscore (_) characters.</p>"""
    type: "aws_sdk_cleanrooms.types.parameter_type.ParameterType"
    """<p>The type of parameter.</p>"""
    default_value: NotRequired[
        "aws_sdk_cleanrooms.types.parameter_value.ParameterValue"
    ]
    """<p>Optional. The default value that is applied in the analysis template. The member who can query can override this value in the query editor.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnalysisParameter) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import aws_sdk_cleanrooms.types.parameter_type

    out["type"] = aws_sdk_cleanrooms.types.parameter_type.serialize_json(value["type"])
    if "default_value" in value:
        out["defaultValue"] = value["default_value"]
    return out


def deserialize_json(data: dict) -> AnalysisParameter:
    out: AnalysisParameter = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("AnalysisParameter.name required")
    if "type" in data:
        import aws_sdk_cleanrooms.types.parameter_type

        out["type"] = aws_sdk_cleanrooms.types.parameter_type.deserialize_json(
            data["type"]
        )
    else:
        raise DeserializationError("AnalysisParameter.type required")
    if "defaultValue" in data:
        out["default_value"] = data["defaultValue"]
    return out
