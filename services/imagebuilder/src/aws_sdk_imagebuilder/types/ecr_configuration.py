"""Generated from Smithy shape ``com.amazonaws.imagebuilder#EcrConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.non_empty_string
    import aws_sdk_imagebuilder.types.string_list


class EcrConfiguration(TypedDict):
    repository_name: NotRequired[
        "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name of the container repository that Amazon Inspector scans to identify findings for your container images. The name includes the path for the repository location. If you don’t provide this information, Image Builder creates a repository in your account named <code>image-builder-image-scanning-repository</code> for vulnerability scans of your output container images.</p>"""
    container_tags: NotRequired["aws_sdk_imagebuilder.types.string_list.StringList"]
    """<p>Tags for Image Builder to apply to the output container image that Amazon Inspector scans. Tags can help you identify and manage your scanned images.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EcrConfiguration) -> dict:
    out: dict = {}
    if "repository_name" in value:
        out["repositoryName"] = value["repository_name"]
    if "container_tags" in value:
        import aws_sdk_imagebuilder.types.string_list

        out["containerTags"] = aws_sdk_imagebuilder.types.string_list.serialize_json(
            value["container_tags"]
        )
    return out


def deserialize_json(data: dict) -> EcrConfiguration:
    out: EcrConfiguration = {}  # type: ignore[typeddict-item]
    if "repositoryName" in data:
        out["repository_name"] = data["repositoryName"]
    if "containerTags" in data:
        import aws_sdk_imagebuilder.types.string_list

        out["container_tags"] = aws_sdk_imagebuilder.types.string_list.deserialize_json(
            data["containerTags"]
        )
    return out
