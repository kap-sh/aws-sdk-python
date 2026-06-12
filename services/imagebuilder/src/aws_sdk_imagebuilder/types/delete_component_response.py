"""Generated from Smithy shape ``com.amazonaws.imagebuilder#DeleteComponentResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.component_build_version_arn
    import aws_sdk_imagebuilder.types.non_empty_string


class DeleteComponentResponse(TypedDict):
    request_id: NotRequired[
        "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>The request ID that uniquely identifies this request.</p>"""
    component_build_version_arn: NotRequired[
        "aws_sdk_imagebuilder.types.component_build_version_arn.ComponentBuildVersionArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the component build version that this request deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteComponentResponse) -> dict:
    out: dict = {}
    if "request_id" in value:
        out["requestId"] = value["request_id"]
    if "component_build_version_arn" in value:
        out["componentBuildVersionArn"] = value["component_build_version_arn"]
    return out


def deserialize_json(data: dict) -> DeleteComponentResponse:
    out: DeleteComponentResponse = {}  # type: ignore[typeddict-item]
    if "requestId" in data:
        out["request_id"] = data["requestId"]
    if "componentBuildVersionArn" in data:
        out["component_build_version_arn"] = data["componentBuildVersionArn"]
    return out
