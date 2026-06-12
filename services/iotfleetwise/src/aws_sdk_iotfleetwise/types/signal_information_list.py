"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#SignalInformationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.signal_information

SignalInformationList: TypeAlias = list[
    "aws_sdk_iotfleetwise.types.signal_information.SignalInformation"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SignalInformationList) -> list:
    import aws_sdk_iotfleetwise.types.signal_information

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iotfleetwise.types.signal_information.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> SignalInformationList:
    import aws_sdk_iotfleetwise.types.signal_information

    out: SignalInformationList = []
    for item in data:
        out.append(
            aws_sdk_iotfleetwise.types.signal_information.deserialize_aws_json_1_0(item)
        )
    return out
