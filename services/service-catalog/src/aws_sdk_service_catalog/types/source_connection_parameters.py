"""Generated from Smithy shape ``com.amazonaws.servicecatalog#SourceConnectionParameters``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.code_star_parameters


class SourceConnectionParameters(TypedDict):
    code_star: NotRequired[
        "aws_sdk_service_catalog.types.code_star_parameters.CodeStarParameters"
    ]
    """<p>Provides <code>ConnectionType</code> details.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SourceConnectionParameters) -> dict:
    out: dict = {}
    if "code_star" in value:
        import aws_sdk_service_catalog.types.code_star_parameters

        out["CodeStar"] = (
            aws_sdk_service_catalog.types.code_star_parameters.serialize_aws_json_1_1(
                value["code_star"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SourceConnectionParameters:
    out: SourceConnectionParameters = {}  # type: ignore[typeddict-item]
    if "CodeStar" in data:
        import aws_sdk_service_catalog.types.code_star_parameters

        out["code_star"] = (
            aws_sdk_service_catalog.types.code_star_parameters.deserialize_aws_json_1_1(
                data["CodeStar"]
            )
        )
    return out
