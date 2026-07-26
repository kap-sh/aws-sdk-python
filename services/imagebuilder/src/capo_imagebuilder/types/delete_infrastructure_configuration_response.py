"""Generated from Smithy shape ``com.amazonaws.imagebuilder#DeleteInfrastructureConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.infrastructure_configuration_arn
    import capo_imagebuilder.types.non_empty_string


class DeleteInfrastructureConfigurationResponse(TypedDict, closed=True):
    request_id: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The request ID that uniquely identifies this request.</p>"""
    infrastructure_configuration_arn: NotRequired[
        "capo_imagebuilder.types.infrastructure_configuration_arn.InfrastructureConfigurationArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the infrastructure configuration that was deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteInfrastructureConfigurationResponse) -> dict:
    out: dict = {}
    if "request_id" in value:
        out["requestId"] = value["request_id"]
    if "infrastructure_configuration_arn" in value:
        out["infrastructureConfigurationArn"] = value[
            "infrastructure_configuration_arn"
        ]
    return out


def deserialize_json(data: dict) -> DeleteInfrastructureConfigurationResponse:
    out: DeleteInfrastructureConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "requestId" in data:
        out["request_id"] = data["requestId"]
    if "infrastructureConfigurationArn" in data:
        out["infrastructure_configuration_arn"] = data["infrastructureConfigurationArn"]
    return out
