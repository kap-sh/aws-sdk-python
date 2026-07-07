"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#OutputResolutionResamplingInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_sagemaker_geospatial.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sagemaker_geospatial.types.user_defined


class OutputResolutionResamplingInput(TypedDict, closed=True):
    user_defined: "aws_sdk_sagemaker_geospatial.types.user_defined.UserDefined"
    """<p>User Defined Resolution for the output of Resampling operation defined by value and unit.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OutputResolutionResamplingInput) -> dict:
    out: dict = {}
    import aws_sdk_sagemaker_geospatial.types.user_defined

    out["UserDefined"] = aws_sdk_sagemaker_geospatial.types.user_defined.serialize_json(
        value["user_defined"]
    )
    return out


def deserialize_json(data: dict) -> OutputResolutionResamplingInput:
    out: OutputResolutionResamplingInput = {}  # type: ignore[typeddict-item]
    if "UserDefined" in data:
        import aws_sdk_sagemaker_geospatial.types.user_defined

        out["user_defined"] = (
            aws_sdk_sagemaker_geospatial.types.user_defined.deserialize_json(
                data["UserDefined"]
            )
        )
    else:
        raise DeserializationError(
            "OutputResolutionResamplingInput.user_defined required"
        )
    return out
