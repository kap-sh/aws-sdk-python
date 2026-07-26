"""Generated from Smithy shape ``com.amazonaws.imagebuilder#TargetContainerRepository``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_imagebuilder.errors import DeserializationError

if TYPE_CHECKING:
    import capo_imagebuilder.types.container_repository_service
    import capo_imagebuilder.types.non_empty_string


class TargetContainerRepository(TypedDict, closed=True):
    service: "capo_imagebuilder.types.container_repository_service.ContainerRepositoryService"
    """<p>Specifies the service in which this image was registered.</p>"""
    repository_name: "capo_imagebuilder.types.non_empty_string.NonEmptyString"
    """<p>The name of the container repository where the output container image is stored. This name is prefixed by the repository location. For example, <code><repository location url>/repository_name</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TargetContainerRepository) -> dict:
    out: dict = {}
    import capo_imagebuilder.types.container_repository_service

    out["service"] = (
        capo_imagebuilder.types.container_repository_service.serialize_json(
            value["service"]
        )
    )
    out["repositoryName"] = value["repository_name"]
    return out


def deserialize_json(data: dict) -> TargetContainerRepository:
    out: TargetContainerRepository = {}  # type: ignore[typeddict-item]
    if "service" in data:
        import capo_imagebuilder.types.container_repository_service

        out["service"] = (
            capo_imagebuilder.types.container_repository_service.deserialize_json(
                data["service"]
            )
        )
    else:
        raise DeserializationError("TargetContainerRepository.service required")
    if "repositoryName" in data:
        out["repository_name"] = data["repositoryName"]
    else:
        raise DeserializationError("TargetContainerRepository.repository_name required")
    return out
