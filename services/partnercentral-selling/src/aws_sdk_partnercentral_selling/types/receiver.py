"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#Receiver``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_partnercentral_selling.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import aws_sdk_partnercentral_selling.types.account_receiver


class _Receiver_Account(TypedDict):
    Account: "aws_sdk_partnercentral_selling.types.account_receiver.AccountReceiver"


Receiver: TypeAlias = _Receiver_Account


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Receiver) -> dict:
    if "Account" in value:
        import aws_sdk_partnercentral_selling.types.account_receiver

        return {
            "Account": aws_sdk_partnercentral_selling.types.account_receiver.serialize_aws_json_1_0(
                value["Account"]
            )
        }
    else:
        raise SerializationError("Receiver: no variant present")


def deserialize_aws_json_1_0(data: dict) -> Receiver:
    if "Account" in data:
        import aws_sdk_partnercentral_selling.types.account_receiver

        return {
            "Account": aws_sdk_partnercentral_selling.types.account_receiver.deserialize_aws_json_1_0(
                data["Account"]
            )
        }
    else:
        raise DeserializationError("Receiver: no recognized variant key")
