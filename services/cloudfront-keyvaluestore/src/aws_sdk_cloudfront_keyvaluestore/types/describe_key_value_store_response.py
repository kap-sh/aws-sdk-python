"""Generated from Smithy shape ``com.amazonaws.cloudfrontkeyvaluestore#DescribeKeyValueStoreResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudfront_keyvaluestore.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_cloudfront_keyvaluestore.types.etag
    import aws_sdk_cloudfront_keyvaluestore.types.kvs_arn


class DescribeKeyValueStoreResponse(TypedDict, closed=True):
    item_count: "int"
    """<p>Number of key value pairs in the Key Value Store.</p>"""
    total_size_in_bytes: "int"
    """<p>Total size of the Key Value Store in bytes.</p>"""
    kvs_arn: "aws_sdk_cloudfront_keyvaluestore.types.kvs_arn.KvsARN"
    """<p>The Amazon Resource Name (ARN) of the Key Value Store.</p>"""
    created: "datetime.datetime"
    """<p>Date and time when the Key Value Store was created.</p>"""
    e_tag: "aws_sdk_cloudfront_keyvaluestore.types.etag.Etag"
    """<p>The version identifier for the current version of the Key Value Store.</p>"""
    last_modified: NotRequired["datetime.datetime"]
    """<p>Date and time when the key value pairs in the Key Value Store was last modified.</p>"""
    status: NotRequired["str"]
    """<p>The current status of the Key Value Store.</p>"""
    failure_reason: NotRequired["str"]
    """<p>The reason for Key Value Store creation failure.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeKeyValueStoreResponse) -> dict:
    out: dict = {}
    out["ItemCount"] = value["item_count"]
    out["TotalSizeInBytes"] = value["total_size_in_bytes"]
    out["KvsARN"] = value["kvs_arn"]
    import aws_sdk_cloudfront_keyvaluestore.types._prelude.timestamp

    out["Created"] = (
        aws_sdk_cloudfront_keyvaluestore.types._prelude.timestamp.serialize_json(
            value["created"]
        )
    )
    if "last_modified" in value:
        import aws_sdk_cloudfront_keyvaluestore.types._prelude.timestamp

        out["LastModified"] = (
            aws_sdk_cloudfront_keyvaluestore.types._prelude.timestamp.serialize_json(
                value["last_modified"]
            )
        )
    if "status" in value:
        out["Status"] = value["status"]
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    return out


def deserialize_json(data: dict) -> DescribeKeyValueStoreResponse:
    out: DescribeKeyValueStoreResponse = {}  # type: ignore[typeddict-item]
    if "ItemCount" in data:
        out["item_count"] = data["ItemCount"]
    else:
        raise DeserializationError("DescribeKeyValueStoreResponse.item_count required")
    if "TotalSizeInBytes" in data:
        out["total_size_in_bytes"] = data["TotalSizeInBytes"]
    else:
        raise DeserializationError(
            "DescribeKeyValueStoreResponse.total_size_in_bytes required"
        )
    if "KvsARN" in data:
        out["kvs_arn"] = data["KvsARN"]
    else:
        raise DeserializationError("DescribeKeyValueStoreResponse.kvs_arn required")
    if "Created" in data:
        import aws_sdk_cloudfront_keyvaluestore.types._prelude.timestamp

        out["created"] = (
            aws_sdk_cloudfront_keyvaluestore.types._prelude.timestamp.deserialize_json(
                data["Created"]
            )
        )
    else:
        raise DeserializationError("DescribeKeyValueStoreResponse.created required")
    if "LastModified" in data:
        import aws_sdk_cloudfront_keyvaluestore.types._prelude.timestamp

        out["last_modified"] = (
            aws_sdk_cloudfront_keyvaluestore.types._prelude.timestamp.deserialize_json(
                data["LastModified"]
            )
        )
    if "Status" in data:
        out["status"] = data["Status"]
    if "FailureReason" in data:
        out["failure_reason"] = data["FailureReason"]
    return out
