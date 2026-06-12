"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#SignalFetchInformationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.signal_fetch_information

SignalFetchInformationList: TypeAlias = list[
    "aws_sdk_iotfleetwise.types.signal_fetch_information.SignalFetchInformation"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SignalFetchInformationList) -> list:
    import aws_sdk_iotfleetwise.types.signal_fetch_information

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iotfleetwise.types.signal_fetch_information.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> SignalFetchInformationList:
    import aws_sdk_iotfleetwise.types.signal_fetch_information

    out: SignalFetchInformationList = []
    for item in data:
        out.append(
            aws_sdk_iotfleetwise.types.signal_fetch_information.deserialize_aws_json_1_0(
                item
            )
        )
    return out
