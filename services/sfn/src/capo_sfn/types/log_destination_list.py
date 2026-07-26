"""Generated from Smithy shape ``com.amazonaws.sfn#LogDestinationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sfn.types.log_destination

LogDestinationList: TypeAlias = list["capo_sfn.types.log_destination.LogDestination"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LogDestinationList) -> list:
    import capo_sfn.types.log_destination

    out: list = []
    for item in value:
        out.append(capo_sfn.types.log_destination.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> LogDestinationList:
    import capo_sfn.types.log_destination

    out: LogDestinationList = []
    for item in data:
        out.append(capo_sfn.types.log_destination.deserialize_aws_json_1_0(item))
    return out
