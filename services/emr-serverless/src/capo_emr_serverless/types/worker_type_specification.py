"""Generated from Smithy shape ``com.amazonaws.emrserverless#WorkerTypeSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr_serverless.types.image_configuration


class WorkerTypeSpecification(TypedDict, closed=True):
    image_configuration: NotRequired[
        "capo_emr_serverless.types.image_configuration.ImageConfiguration"
    ]
    """<p>The image configuration for a worker type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WorkerTypeSpecification) -> dict:
    out: dict = {}
    if "image_configuration" in value:
        import capo_emr_serverless.types.image_configuration

        out["imageConfiguration"] = (
            capo_emr_serverless.types.image_configuration.serialize_json(
                value["image_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> WorkerTypeSpecification:
    out: WorkerTypeSpecification = {}  # type: ignore[typeddict-item]
    if "imageConfiguration" in data:
        import capo_emr_serverless.types.image_configuration

        out["image_configuration"] = (
            capo_emr_serverless.types.image_configuration.deserialize_json(
                data["imageConfiguration"]
            )
        )
    return out
