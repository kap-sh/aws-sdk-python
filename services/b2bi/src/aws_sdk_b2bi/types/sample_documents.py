"""Generated from Smithy shape ``com.amazonaws.b2bi#SampleDocuments``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_b2bi.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_b2bi.types.bucket_name
    import aws_sdk_b2bi.types.key_list


class SampleDocuments(TypedDict, closed=True):
    bucket_name: "aws_sdk_b2bi.types.bucket_name.BucketName"
    """<p>Contains the Amazon S3 bucket that is used to hold your sample documents.</p>"""
    keys: "aws_sdk_b2bi.types.key_list.KeyList"
    """<p>Contains an array of the Amazon S3 keys used to identify the location for your sample documents.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SampleDocuments) -> dict:
    out: dict = {}
    out["bucketName"] = value["bucket_name"]
    import aws_sdk_b2bi.types.key_list

    out["keys"] = aws_sdk_b2bi.types.key_list.serialize_aws_json_1_0(value["keys"])
    return out


def deserialize_aws_json_1_0(data: dict) -> SampleDocuments:
    out: SampleDocuments = {}  # type: ignore[typeddict-item]
    if "bucketName" in data:
        out["bucket_name"] = data["bucketName"]
    else:
        raise DeserializationError("SampleDocuments.bucket_name required")
    if "keys" in data:
        import aws_sdk_b2bi.types.key_list

        out["keys"] = aws_sdk_b2bi.types.key_list.deserialize_aws_json_1_0(data["keys"])
    else:
        raise DeserializationError("SampleDocuments.keys required")
    return out
