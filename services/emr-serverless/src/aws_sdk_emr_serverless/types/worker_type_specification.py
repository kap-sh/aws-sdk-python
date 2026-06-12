"""Generated from Smithy shape ``com.amazonaws.emrserverless#WorkerTypeSpecification``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr_serverless.types.image_configuration


class WorkerTypeSpecification(TypedDict):
    image_configuration: NotRequired[
        "aws_sdk_emr_serverless.types.image_configuration.ImageConfiguration"
    ]
    """<p>The image configuration for a worker type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WorkerTypeSpecification) -> dict:
    out: dict = {}
    if "image_configuration" in value:
        import aws_sdk_emr_serverless.types.image_configuration

        out["imageConfiguration"] = (
            aws_sdk_emr_serverless.types.image_configuration.serialize_json(
                value["image_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> WorkerTypeSpecification:
    out: WorkerTypeSpecification = {}  # type: ignore[typeddict-item]
    if "imageConfiguration" in data:
        import aws_sdk_emr_serverless.types.image_configuration

        out["image_configuration"] = (
            aws_sdk_emr_serverless.types.image_configuration.deserialize_json(
                data["imageConfiguration"]
            )
        )
    return out
