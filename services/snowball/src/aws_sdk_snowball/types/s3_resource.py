"""Generated from Smithy shape ``com.amazonaws.snowball#S3Resource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_snowball.types.key_range
    import aws_sdk_snowball.types.resource_arn
    import aws_sdk_snowball.types.target_on_device_service_list


class S3Resource(TypedDict, closed=True):
    bucket_arn: NotRequired["aws_sdk_snowball.types.resource_arn.ResourceARN"]
    """<p>The Amazon Resource Name (ARN) of an Amazon S3 bucket.</p>"""
    key_range: NotRequired["aws_sdk_snowball.types.key_range.KeyRange"]
    """<p>For export jobs, you can provide an optional <code>KeyRange</code> within a specific Amazon S3 bucket. The length of the range is defined at job creation, and has either an inclusive <code>BeginMarker</code>, an inclusive <code>EndMarker</code>, or both. Ranges are UTF-8 binary sorted.</p>"""
    target_on_device_services: NotRequired[
        "aws_sdk_snowball.types.target_on_device_service_list.TargetOnDeviceServiceList"
    ]
    """<p>Specifies the service or services on the Snow Family device that your transferred data will be exported from or imported into. Amazon Web Services Snow Family supports Amazon S3 and NFS (Network File System).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3Resource) -> dict:
    out: dict = {}
    if "bucket_arn" in value:
        out["BucketArn"] = value["bucket_arn"]
    if "key_range" in value:
        import aws_sdk_snowball.types.key_range

        out["KeyRange"] = aws_sdk_snowball.types.key_range.serialize_aws_json_1_1(
            value["key_range"]
        )
    if "target_on_device_services" in value:
        import aws_sdk_snowball.types.target_on_device_service_list

        out["TargetOnDeviceServices"] = (
            aws_sdk_snowball.types.target_on_device_service_list.serialize_aws_json_1_1(
                value["target_on_device_services"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> S3Resource:
    out: S3Resource = {}  # type: ignore[typeddict-item]
    if "BucketArn" in data:
        out["bucket_arn"] = data["BucketArn"]
    if "KeyRange" in data:
        import aws_sdk_snowball.types.key_range

        out["key_range"] = aws_sdk_snowball.types.key_range.deserialize_aws_json_1_1(
            data["KeyRange"]
        )
    if "TargetOnDeviceServices" in data:
        import aws_sdk_snowball.types.target_on_device_service_list

        out["target_on_device_services"] = (
            aws_sdk_snowball.types.target_on_device_service_list.deserialize_aws_json_1_1(
                data["TargetOnDeviceServices"]
            )
        )
    return out
