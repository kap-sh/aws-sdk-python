"""Generated from Smithy shape ``com.amazonaws.imagebuilder#GetInfrastructureConfigurationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.infrastructure_configuration
    import aws_sdk_imagebuilder.types.non_empty_string


class GetInfrastructureConfigurationResponse(TypedDict):
    request_id: NotRequired[
        "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>The request ID that uniquely identifies this request.</p>"""
    infrastructure_configuration: NotRequired[
        "aws_sdk_imagebuilder.types.infrastructure_configuration.InfrastructureConfiguration"
    ]
    """<p>The infrastructure configuration object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetInfrastructureConfigurationResponse) -> dict:
    out: dict = {}
    if "request_id" in value:
        out["requestId"] = value["request_id"]
    if "infrastructure_configuration" in value:
        import aws_sdk_imagebuilder.types.infrastructure_configuration

        out["infrastructureConfiguration"] = (
            aws_sdk_imagebuilder.types.infrastructure_configuration.serialize_json(
                value["infrastructure_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetInfrastructureConfigurationResponse:
    out: GetInfrastructureConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "requestId" in data:
        out["request_id"] = data["requestId"]
    if "infrastructureConfiguration" in data:
        import aws_sdk_imagebuilder.types.infrastructure_configuration

        out["infrastructure_configuration"] = (
            aws_sdk_imagebuilder.types.infrastructure_configuration.deserialize_json(
                data["infrastructureConfiguration"]
            )
        )
    return out
