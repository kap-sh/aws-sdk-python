"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsAmazonMqBrokerUsersList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_amazon_mq_broker_users_details

AwsAmazonMqBrokerUsersList: TypeAlias = list[
    "aws_sdk_securityhub.types.aws_amazon_mq_broker_users_details.AwsAmazonMqBrokerUsersDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsAmazonMqBrokerUsersList) -> list:
    import aws_sdk_securityhub.types.aws_amazon_mq_broker_users_details

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.aws_amazon_mq_broker_users_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsAmazonMqBrokerUsersList:
    import aws_sdk_securityhub.types.aws_amazon_mq_broker_users_details

    out: AwsAmazonMqBrokerUsersList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.aws_amazon_mq_broker_users_details.deserialize_json(
                item
            )
        )
    return out
