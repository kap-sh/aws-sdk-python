"""Generated from Smithy shape ``com.amazonaws.cloudfrontkeyvaluestore#UpdateKeysRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudfront_keyvaluestore.types.delete_key_requests_list
    import aws_sdk_cloudfront_keyvaluestore.types.etag
    import aws_sdk_cloudfront_keyvaluestore.types.kvs_arn
    import aws_sdk_cloudfront_keyvaluestore.types.put_key_requests_list


class UpdateKeysRequest(TypedDict):
    kvs_arn: "aws_sdk_cloudfront_keyvaluestore.types.kvs_arn.KvsARN"
    """<p>The Amazon Resource Name (ARN) of the Key Value Store.</p>"""
    if_match: "aws_sdk_cloudfront_keyvaluestore.types.etag.Etag"
    """<p>The current version (ETag) of the Key Value Store that you are updating keys of, which you can get using DescribeKeyValueStore.</p>"""
    puts: NotRequired[
        "aws_sdk_cloudfront_keyvaluestore.types.put_key_requests_list.PutKeyRequestsList"
    ]
    """<p>List of key value pairs to put.</p>"""
    deletes: NotRequired[
        "aws_sdk_cloudfront_keyvaluestore.types.delete_key_requests_list.DeleteKeyRequestsList"
    ]
    """<p>List of keys to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateKeysRequest) -> dict:
    out: dict = {}
    if "puts" in value:
        import aws_sdk_cloudfront_keyvaluestore.types.put_key_requests_list

        out["Puts"] = (
            aws_sdk_cloudfront_keyvaluestore.types.put_key_requests_list.serialize_json(
                value["puts"]
            )
        )
    if "deletes" in value:
        import aws_sdk_cloudfront_keyvaluestore.types.delete_key_requests_list

        out["Deletes"] = (
            aws_sdk_cloudfront_keyvaluestore.types.delete_key_requests_list.serialize_json(
                value["deletes"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateKeysRequest:
    out: UpdateKeysRequest = {}  # type: ignore[typeddict-item]
    if "Puts" in data:
        import aws_sdk_cloudfront_keyvaluestore.types.put_key_requests_list

        out["puts"] = (
            aws_sdk_cloudfront_keyvaluestore.types.put_key_requests_list.deserialize_json(
                data["Puts"]
            )
        )
    if "Deletes" in data:
        import aws_sdk_cloudfront_keyvaluestore.types.delete_key_requests_list

        out["deletes"] = (
            aws_sdk_cloudfront_keyvaluestore.types.delete_key_requests_list.deserialize_json(
                data["Deletes"]
            )
        )
    return out
