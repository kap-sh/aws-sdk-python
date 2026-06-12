"""Generated from Smithy shape ``com.amazonaws.lightsail#CreateBucketAccessKeyResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.access_key
    import aws_sdk_lightsail.types.operation_list


class CreateBucketAccessKeyResult(TypedDict):
    access_key: NotRequired["aws_sdk_lightsail.types.access_key.AccessKey"]
    """<p>An object that describes the access key that is created.</p>"""
    operations: NotRequired["aws_sdk_lightsail.types.operation_list.OperationList"]
    """<p>An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateBucketAccessKeyResult) -> dict:
    out: dict = {}
    if "access_key" in value:
        import aws_sdk_lightsail.types.access_key

        out["accessKey"] = aws_sdk_lightsail.types.access_key.serialize_aws_json_1_1(
            value["access_key"]
        )
    if "operations" in value:
        import aws_sdk_lightsail.types.operation_list

        out["operations"] = (
            aws_sdk_lightsail.types.operation_list.serialize_aws_json_1_1(
                value["operations"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateBucketAccessKeyResult:
    out: CreateBucketAccessKeyResult = {}  # type: ignore[typeddict-item]
    if "accessKey" in data:
        import aws_sdk_lightsail.types.access_key

        out["access_key"] = aws_sdk_lightsail.types.access_key.deserialize_aws_json_1_1(
            data["accessKey"]
        )
    if "operations" in data:
        import aws_sdk_lightsail.types.operation_list

        out["operations"] = (
            aws_sdk_lightsail.types.operation_list.deserialize_aws_json_1_1(
                data["operations"]
            )
        )
    return out
