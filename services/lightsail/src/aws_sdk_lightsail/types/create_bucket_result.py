"""Generated from Smithy shape ``com.amazonaws.lightsail#CreateBucketResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.bucket
    import aws_sdk_lightsail.types.operation_list


class CreateBucketResult(TypedDict, closed=True):
    bucket: NotRequired["aws_sdk_lightsail.types.bucket.Bucket"]
    """<p>An object that describes the bucket that is created.</p>"""
    operations: NotRequired["aws_sdk_lightsail.types.operation_list.OperationList"]
    """<p>An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateBucketResult) -> dict:
    out: dict = {}
    if "bucket" in value:
        import aws_sdk_lightsail.types.bucket

        out["bucket"] = aws_sdk_lightsail.types.bucket.serialize_aws_json_1_1(
            value["bucket"]
        )
    if "operations" in value:
        import aws_sdk_lightsail.types.operation_list

        out["operations"] = (
            aws_sdk_lightsail.types.operation_list.serialize_aws_json_1_1(
                value["operations"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateBucketResult:
    out: CreateBucketResult = {}  # type: ignore[typeddict-item]
    if "bucket" in data:
        import aws_sdk_lightsail.types.bucket

        out["bucket"] = aws_sdk_lightsail.types.bucket.deserialize_aws_json_1_1(
            data["bucket"]
        )
    if "operations" in data:
        import aws_sdk_lightsail.types.operation_list

        out["operations"] = (
            aws_sdk_lightsail.types.operation_list.deserialize_aws_json_1_1(
                data["operations"]
            )
        )
    return out
