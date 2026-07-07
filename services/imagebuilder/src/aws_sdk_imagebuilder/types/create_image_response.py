"""Generated from Smithy shape ``com.amazonaws.imagebuilder#CreateImageResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.client_token
    import aws_sdk_imagebuilder.types.image_build_version_arn
    import aws_sdk_imagebuilder.types.latest_version_references
    import aws_sdk_imagebuilder.types.non_empty_string


class CreateImageResponse(TypedDict, closed=True):
    request_id: NotRequired[
        "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>The request ID that uniquely identifies this request.</p>"""
    client_token: NotRequired["aws_sdk_imagebuilder.types.client_token.ClientToken"]
    """<p>The client token that uniquely identifies the request.</p>"""
    image_build_version_arn: NotRequired[
        "aws_sdk_imagebuilder.types.image_build_version_arn.ImageBuildVersionArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the image that the request created.</p>"""
    latest_version_references: NotRequired[
        "aws_sdk_imagebuilder.types.latest_version_references.LatestVersionReferences"
    ]
    """<p>The resource ARNs with different wildcard variations of semantic versioning.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateImageResponse) -> dict:
    out: dict = {}
    if "request_id" in value:
        out["requestId"] = value["request_id"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "image_build_version_arn" in value:
        out["imageBuildVersionArn"] = value["image_build_version_arn"]
    if "latest_version_references" in value:
        import aws_sdk_imagebuilder.types.latest_version_references

        out["latestVersionReferences"] = (
            aws_sdk_imagebuilder.types.latest_version_references.serialize_json(
                value["latest_version_references"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateImageResponse:
    out: CreateImageResponse = {}  # type: ignore[typeddict-item]
    if "requestId" in data:
        out["request_id"] = data["requestId"]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "imageBuildVersionArn" in data:
        out["image_build_version_arn"] = data["imageBuildVersionArn"]
    if "latestVersionReferences" in data:
        import aws_sdk_imagebuilder.types.latest_version_references

        out["latest_version_references"] = (
            aws_sdk_imagebuilder.types.latest_version_references.deserialize_json(
                data["latestVersionReferences"]
            )
        )
    return out
