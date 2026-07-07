"""Generated from Smithy shape ``com.amazonaws.mgn#StartImportRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_mgn.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mgn.types.client_idempotency_token
    import aws_sdk_mgn.types.s3_bucket_source
    import aws_sdk_mgn.types.tags_map


class StartImportRequest(TypedDict, closed=True):
    client_token: NotRequired[
        "aws_sdk_mgn.types.client_idempotency_token.ClientIdempotencyToken"
    ]
    """<p>Start import request client token.</p>"""
    s3_bucket_source: "aws_sdk_mgn.types.s3_bucket_source.S3BucketSource"
    """<p>Start import request s3 bucket source.</p>"""
    tags: NotRequired["aws_sdk_mgn.types.tags_map.TagsMap"]
    """<p>Start import request tags.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartImportRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    import aws_sdk_mgn.types.s3_bucket_source

    out["s3BucketSource"] = aws_sdk_mgn.types.s3_bucket_source.serialize_json(
        value["s3_bucket_source"]
    )
    if "tags" in value:
        import aws_sdk_mgn.types.tags_map

        out["tags"] = aws_sdk_mgn.types.tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> StartImportRequest:
    out: StartImportRequest = {}  # type: ignore[typeddict-item]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "s3BucketSource" in data:
        import aws_sdk_mgn.types.s3_bucket_source

        out["s3_bucket_source"] = aws_sdk_mgn.types.s3_bucket_source.deserialize_json(
            data["s3BucketSource"]
        )
    else:
        raise DeserializationError("StartImportRequest.s3_bucket_source required")
    if "tags" in data:
        import aws_sdk_mgn.types.tags_map

        out["tags"] = aws_sdk_mgn.types.tags_map.deserialize_json(data["tags"])
    return out
