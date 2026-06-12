"""Generated from Smithy shape ``com.amazonaws.imagebuilder#DeleteComponentRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.component_build_version_arn


class DeleteComponentRequest(TypedDict):
    component_build_version_arn: "aws_sdk_imagebuilder.types.component_build_version_arn.ComponentBuildVersionArn"
    """<p>The Amazon Resource Name (ARN) of the component build version to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteComponentRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteComponentRequest:
    out: DeleteComponentRequest = {}  # type: ignore[typeddict-item]
    return out
