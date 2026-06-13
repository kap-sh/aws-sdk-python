"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#OutputResolutionStackInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker_geospatial.types.predefined_resolution
    import aws_sdk_sagemaker_geospatial.types.user_defined


class OutputResolutionStackInput(TypedDict):
    predefined: NotRequired[
        "aws_sdk_sagemaker_geospatial.types.predefined_resolution.PredefinedResolution"
    ]
    """<p>A string value representing Predefined Output Resolution for a stacking operation. Allowed values are <code>HIGHEST</code>, <code>LOWEST</code>, and <code>AVERAGE</code>.</p>"""
    user_defined: NotRequired[
        "aws_sdk_sagemaker_geospatial.types.user_defined.UserDefined"
    ]
    """<p>The structure representing User Output Resolution for a Stacking operation defined as a value and unit.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OutputResolutionStackInput) -> dict:
    out: dict = {}
    if "predefined" in value:
        out["Predefined"] = value["predefined"]
    if "user_defined" in value:
        import aws_sdk_sagemaker_geospatial.types.user_defined

        out["UserDefined"] = (
            aws_sdk_sagemaker_geospatial.types.user_defined.serialize_json(
                value["user_defined"]
            )
        )
    return out


def deserialize_json(data: dict) -> OutputResolutionStackInput:
    out: OutputResolutionStackInput = {}  # type: ignore[typeddict-item]
    if "Predefined" in data:
        out["predefined"] = data["Predefined"]
    if "UserDefined" in data:
        import aws_sdk_sagemaker_geospatial.types.user_defined

        out["user_defined"] = (
            aws_sdk_sagemaker_geospatial.types.user_defined.deserialize_json(
                data["UserDefined"]
            )
        )
    return out
