"""Generated from Smithy shape ``com.amazonaws.emrserverless#WorkerTypeSpecificationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_emr_serverless.types.image_configuration_input


class WorkerTypeSpecificationInput(TypedDict, closed=True):
    image_configuration: NotRequired[
        "aws_sdk_emr_serverless.types.image_configuration_input.ImageConfigurationInput"
    ]
    """<p>The image configuration for a worker type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WorkerTypeSpecificationInput) -> dict:
    out: dict = {}
    if "image_configuration" in value:
        import aws_sdk_emr_serverless.types.image_configuration_input

        out["imageConfiguration"] = (
            aws_sdk_emr_serverless.types.image_configuration_input.serialize_json(
                value["image_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> WorkerTypeSpecificationInput:
    out: WorkerTypeSpecificationInput = {}  # type: ignore[typeddict-item]
    if "imageConfiguration" in data:
        import aws_sdk_emr_serverless.types.image_configuration_input

        out["image_configuration"] = (
            aws_sdk_emr_serverless.types.image_configuration_input.deserialize_json(
                data["imageConfiguration"]
            )
        )
    return out
