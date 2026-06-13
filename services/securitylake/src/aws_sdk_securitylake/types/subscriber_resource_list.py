"""Generated from Smithy shape ``com.amazonaws.securitylake#SubscriberResourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securitylake.types.subscriber_resource

SubscriberResourceList: TypeAlias = list[
    "aws_sdk_securitylake.types.subscriber_resource.SubscriberResource"
]


# --- restJson1 ser/de ---
def serialize_json(value: SubscriberResourceList) -> list:
    import aws_sdk_securitylake.types.subscriber_resource

    out: list = []
    for item in value:
        out.append(aws_sdk_securitylake.types.subscriber_resource.serialize_json(item))
    return out


def deserialize_json(data: list) -> SubscriberResourceList:
    import aws_sdk_securitylake.types.subscriber_resource

    out: SubscriberResourceList = []
    for item in data:
        out.append(
            aws_sdk_securitylake.types.subscriber_resource.deserialize_json(item)
        )
    return out
