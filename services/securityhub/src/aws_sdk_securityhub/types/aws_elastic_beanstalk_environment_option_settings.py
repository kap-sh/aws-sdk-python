"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsElasticBeanstalkEnvironmentOptionSettings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_elastic_beanstalk_environment_option_setting

AwsElasticBeanstalkEnvironmentOptionSettings: TypeAlias = list[
    "aws_sdk_securityhub.types.aws_elastic_beanstalk_environment_option_setting.AwsElasticBeanstalkEnvironmentOptionSetting"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsElasticBeanstalkEnvironmentOptionSettings) -> list:
    import aws_sdk_securityhub.types.aws_elastic_beanstalk_environment_option_setting

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.aws_elastic_beanstalk_environment_option_setting.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsElasticBeanstalkEnvironmentOptionSettings:
    import aws_sdk_securityhub.types.aws_elastic_beanstalk_environment_option_setting

    out: AwsElasticBeanstalkEnvironmentOptionSettings = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.aws_elastic_beanstalk_environment_option_setting.deserialize_json(
                item
            )
        )
    return out
