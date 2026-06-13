"""Generated from Smithy shape ``com.amazonaws.omics#ContainerRegistryMap``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_omics.types.image_mappings_list
    import aws_sdk_omics.types.registry_mappings_list


class ContainerRegistryMap(TypedDict):
    registry_mappings: NotRequired[
        "aws_sdk_omics.types.registry_mappings_list.RegistryMappingsList"
    ]
    """<p>Mapping that provides the ECR repository path where upstream container images are pulled and synchronized.</p>"""
    image_mappings: NotRequired[
        "aws_sdk_omics.types.image_mappings_list.ImageMappingsList"
    ]
    """<p>Image mappings specify path mappings between the ECR private repository and their corresponding external repositories.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContainerRegistryMap) -> dict:
    out: dict = {}
    if "registry_mappings" in value:
        import aws_sdk_omics.types.registry_mappings_list

        out["registryMappings"] = (
            aws_sdk_omics.types.registry_mappings_list.serialize_json(
                value["registry_mappings"]
            )
        )
    if "image_mappings" in value:
        import aws_sdk_omics.types.image_mappings_list

        out["imageMappings"] = aws_sdk_omics.types.image_mappings_list.serialize_json(
            value["image_mappings"]
        )
    return out


def deserialize_json(data: dict) -> ContainerRegistryMap:
    out: ContainerRegistryMap = {}  # type: ignore[typeddict-item]
    if "registryMappings" in data:
        import aws_sdk_omics.types.registry_mappings_list

        out["registry_mappings"] = (
            aws_sdk_omics.types.registry_mappings_list.deserialize_json(
                data["registryMappings"]
            )
        )
    if "imageMappings" in data:
        import aws_sdk_omics.types.image_mappings_list

        out["image_mappings"] = (
            aws_sdk_omics.types.image_mappings_list.deserialize_json(
                data["imageMappings"]
            )
        )
    return out
