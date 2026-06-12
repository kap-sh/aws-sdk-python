"""Generated from Smithy shape ``com.amazonaws.sagemaker#AuthorizedUrlConfigs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.authorized_url

AuthorizedUrlConfigs: TypeAlias = list[
    "aws_sdk_sagemaker.types.authorized_url.AuthorizedUrl"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AuthorizedUrlConfigs) -> list:
    import aws_sdk_sagemaker.types.authorized_url

    out: list = []
    for item in value:
        out.append(aws_sdk_sagemaker.types.authorized_url.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> AuthorizedUrlConfigs:
    import aws_sdk_sagemaker.types.authorized_url

    out: AuthorizedUrlConfigs = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.authorized_url.deserialize_aws_json_1_1(item)
        )
    return out
