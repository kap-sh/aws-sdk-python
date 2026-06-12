"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsElasticBeanstalkEnvironmentEnvironmentLinks``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_elastic_beanstalk_environment_environment_link

AwsElasticBeanstalkEnvironmentEnvironmentLinks: TypeAlias = list[
    "aws_sdk_securityhub.types.aws_elastic_beanstalk_environment_environment_link.AwsElasticBeanstalkEnvironmentEnvironmentLink"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsElasticBeanstalkEnvironmentEnvironmentLinks) -> list:
    import aws_sdk_securityhub.types.aws_elastic_beanstalk_environment_environment_link

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.aws_elastic_beanstalk_environment_environment_link.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsElasticBeanstalkEnvironmentEnvironmentLinks:
    import aws_sdk_securityhub.types.aws_elastic_beanstalk_environment_environment_link

    out: AwsElasticBeanstalkEnvironmentEnvironmentLinks = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.aws_elastic_beanstalk_environment_environment_link.deserialize_json(
                item
            )
        )
    return out
