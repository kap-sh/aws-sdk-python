"""Generated from Smithy shape ``com.amazonaws.codegurusecurity#CreateUploadUrlResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_codeguru_security.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codeguru_security.types.request_header_map
    import aws_sdk_codeguru_security.types.s3_url
    import aws_sdk_codeguru_security.types.uuid


class CreateUploadUrlResponse(TypedDict):
    s3_url: "aws_sdk_codeguru_security.types.s3_url.S3Url"
    """<p>A pre-signed S3 URL. You can upload the code file you want to scan with the required <code>requestHeaders</code> using any HTTP client.</p>"""
    request_headers: (
        "aws_sdk_codeguru_security.types.request_header_map.RequestHeaderMap"
    )
    """<p>A set of key-value pairs that contain the required headers when uploading your resource.</p>"""
    code_artifact_id: "aws_sdk_codeguru_security.types.uuid.Uuid"
    """<p>The identifier for the uploaded code resource. Pass this to <code>CreateScan</code> to use the uploaded resources.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateUploadUrlResponse) -> dict:
    out: dict = {}
    out["s3Url"] = value["s3_url"]
    import aws_sdk_codeguru_security.types.request_header_map

    out["requestHeaders"] = (
        aws_sdk_codeguru_security.types.request_header_map.serialize_json(
            value["request_headers"]
        )
    )
    out["codeArtifactId"] = value["code_artifact_id"]
    return out


def deserialize_json(data: dict) -> CreateUploadUrlResponse:
    out: CreateUploadUrlResponse = {}  # type: ignore[typeddict-item]
    if "s3Url" in data:
        out["s3_url"] = data["s3Url"]
    else:
        raise DeserializationError("CreateUploadUrlResponse.s3_url required")
    if "requestHeaders" in data:
        import aws_sdk_codeguru_security.types.request_header_map

        out["request_headers"] = (
            aws_sdk_codeguru_security.types.request_header_map.deserialize_json(
                data["requestHeaders"]
            )
        )
    else:
        raise DeserializationError("CreateUploadUrlResponse.request_headers required")
    if "codeArtifactId" in data:
        out["code_artifact_id"] = data["codeArtifactId"]
    else:
        raise DeserializationError("CreateUploadUrlResponse.code_artifact_id required")
    return out
