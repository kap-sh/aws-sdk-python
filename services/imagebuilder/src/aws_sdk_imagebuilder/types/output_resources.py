"""Generated from Smithy shape ``com.amazonaws.imagebuilder#OutputResources``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.ami_list
    import aws_sdk_imagebuilder.types.container_list


class OutputResources(TypedDict, closed=True):
    amis: NotRequired["aws_sdk_imagebuilder.types.ami_list.AmiList"]
    """<p>The Amazon EC2 AMIs created by this image.</p>"""
    containers: NotRequired["aws_sdk_imagebuilder.types.container_list.ContainerList"]
    """<p>Container images that the pipeline has generated and stored in the output repository.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OutputResources) -> dict:
    out: dict = {}
    if "amis" in value:
        import aws_sdk_imagebuilder.types.ami_list

        out["amis"] = aws_sdk_imagebuilder.types.ami_list.serialize_json(value["amis"])
    if "containers" in value:
        import aws_sdk_imagebuilder.types.container_list

        out["containers"] = aws_sdk_imagebuilder.types.container_list.serialize_json(
            value["containers"]
        )
    return out


def deserialize_json(data: dict) -> OutputResources:
    out: OutputResources = {}  # type: ignore[typeddict-item]
    if "amis" in data:
        import aws_sdk_imagebuilder.types.ami_list

        out["amis"] = aws_sdk_imagebuilder.types.ami_list.deserialize_json(data["amis"])
    if "containers" in data:
        import aws_sdk_imagebuilder.types.container_list

        out["containers"] = aws_sdk_imagebuilder.types.container_list.deserialize_json(
            data["containers"]
        )
    return out
