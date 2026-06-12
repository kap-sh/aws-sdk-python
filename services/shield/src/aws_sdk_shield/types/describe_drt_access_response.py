"""Generated from Smithy shape ``com.amazonaws.shield#DescribeDRTAccessResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_shield.types.log_bucket_list
    import aws_sdk_shield.types.role_arn


class DescribeDRTAccessResponse(TypedDict):
    role_arn: NotRequired["aws_sdk_shield.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of the role the SRT used to access your Amazon Web Services account.</p>"""
    log_bucket_list: NotRequired["aws_sdk_shield.types.log_bucket_list.LogBucketList"]
    """<p>The list of Amazon S3 buckets accessed by the SRT.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDRTAccessResponse) -> dict:
    out: dict = {}
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "log_bucket_list" in value:
        import aws_sdk_shield.types.log_bucket_list

        out["LogBucketList"] = (
            aws_sdk_shield.types.log_bucket_list.serialize_aws_json_1_1(
                value["log_bucket_list"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDRTAccessResponse:
    out: DescribeDRTAccessResponse = {}  # type: ignore[typeddict-item]
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    if "LogBucketList" in data:
        import aws_sdk_shield.types.log_bucket_list

        out["log_bucket_list"] = (
            aws_sdk_shield.types.log_bucket_list.deserialize_aws_json_1_1(
                data["LogBucketList"]
            )
        )
    return out
