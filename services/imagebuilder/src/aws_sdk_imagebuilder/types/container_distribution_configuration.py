"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ContainerDistributionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_imagebuilder.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.non_empty_string
    import aws_sdk_imagebuilder.types.string_list
    import aws_sdk_imagebuilder.types.target_container_repository


class ContainerDistributionConfiguration(TypedDict, closed=True):
    description: NotRequired[
        "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>The description of the container distribution configuration.</p>"""
    container_tags: NotRequired["aws_sdk_imagebuilder.types.string_list.StringList"]
    """<p>Tags that are attached to the container distribution configuration.</p>"""
    target_repository: "aws_sdk_imagebuilder.types.target_container_repository.TargetContainerRepository"
    """<p>The destination repository for the container distribution configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContainerDistributionConfiguration) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    if "container_tags" in value:
        import aws_sdk_imagebuilder.types.string_list

        out["containerTags"] = aws_sdk_imagebuilder.types.string_list.serialize_json(
            value["container_tags"]
        )
    import aws_sdk_imagebuilder.types.target_container_repository

    out["targetRepository"] = (
        aws_sdk_imagebuilder.types.target_container_repository.serialize_json(
            value["target_repository"]
        )
    )
    return out


def deserialize_json(data: dict) -> ContainerDistributionConfiguration:
    out: ContainerDistributionConfiguration = {}  # type: ignore[typeddict-item]
    if "description" in data:
        out["description"] = data["description"]
    if "containerTags" in data:
        import aws_sdk_imagebuilder.types.string_list

        out["container_tags"] = aws_sdk_imagebuilder.types.string_list.deserialize_json(
            data["containerTags"]
        )
    if "targetRepository" in data:
        import aws_sdk_imagebuilder.types.target_container_repository

        out["target_repository"] = (
            aws_sdk_imagebuilder.types.target_container_repository.deserialize_json(
                data["targetRepository"]
            )
        )
    else:
        raise DeserializationError(
            "ContainerDistributionConfiguration.target_repository required"
        )
    return out
