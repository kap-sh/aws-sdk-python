"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsS3BucketBucketLifecycleConfigurationDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_s3_bucket_bucket_lifecycle_configuration_rules_list


class AwsS3BucketBucketLifecycleConfigurationDetails(TypedDict):
    rules: NotRequired[
        "aws_sdk_securityhub.types.aws_s3_bucket_bucket_lifecycle_configuration_rules_list.AwsS3BucketBucketLifecycleConfigurationRulesList"
    ]
    """<p>The lifecycle rules.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsS3BucketBucketLifecycleConfigurationDetails) -> dict:
    out: dict = {}
    if "rules" in value:
        import aws_sdk_securityhub.types.aws_s3_bucket_bucket_lifecycle_configuration_rules_list

        out["Rules"] = (
            aws_sdk_securityhub.types.aws_s3_bucket_bucket_lifecycle_configuration_rules_list.serialize_json(
                value["rules"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsS3BucketBucketLifecycleConfigurationDetails:
    out: AwsS3BucketBucketLifecycleConfigurationDetails = {}  # type: ignore[typeddict-item]
    if "Rules" in data:
        import aws_sdk_securityhub.types.aws_s3_bucket_bucket_lifecycle_configuration_rules_list

        out["rules"] = (
            aws_sdk_securityhub.types.aws_s3_bucket_bucket_lifecycle_configuration_rules_list.deserialize_json(
                data["Rules"]
            )
        )
    return out
