"""Generated from Smithy shape ``com.amazonaws.imagebuilder#GetComponentRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.component_version_arn_or_build_version_arn


class GetComponentRequest(TypedDict):
    component_build_version_arn: "aws_sdk_imagebuilder.types.component_version_arn_or_build_version_arn.ComponentVersionArnOrBuildVersionArn"
    r"""<p>The Amazon Resource Name (ARN) of the component that you want to get. Regex requires the suffix <code>/\d+$</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetComponentRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetComponentRequest:
    out: GetComponentRequest = {}  # type: ignore[typeddict-item]
    return out
