"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#DeliveryMediumType``."""

from typing import Literal, TypeAlias, cast

DeliveryMediumType: TypeAlias = Literal[
    "SMS",
    "EMAIL",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeliveryMediumType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DeliveryMediumType:
    return cast(DeliveryMediumType, data)
