"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ImportComponentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.client_token
    import aws_sdk_imagebuilder.types.component_build_version_arn
    import aws_sdk_imagebuilder.types.non_empty_string


class ImportComponentResponse(TypedDict, closed=True):
    request_id: NotRequired[
        "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>The request ID that uniquely identifies this request.</p>"""
    client_token: NotRequired["aws_sdk_imagebuilder.types.client_token.ClientToken"]
    """<p>The client token that uniquely identifies the request.</p>"""
    component_build_version_arn: NotRequired[
        "aws_sdk_imagebuilder.types.component_build_version_arn.ComponentBuildVersionArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the imported component.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImportComponentResponse) -> dict:
    out: dict = {}
    if "request_id" in value:
        out["requestId"] = value["request_id"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "component_build_version_arn" in value:
        out["componentBuildVersionArn"] = value["component_build_version_arn"]
    return out


def deserialize_json(data: dict) -> ImportComponentResponse:
    out: ImportComponentResponse = {}  # type: ignore[typeddict-item]
    if "requestId" in data:
        out["request_id"] = data["requestId"]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "componentBuildVersionArn" in data:
        out["component_build_version_arn"] = data["componentBuildVersionArn"]
    return out
