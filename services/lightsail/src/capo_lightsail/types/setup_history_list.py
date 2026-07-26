"""Generated from Smithy shape ``com.amazonaws.lightsail#setupHistoryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lightsail.types.setup_history

setupHistoryList: TypeAlias = list["capo_lightsail.types.setup_history.SetupHistory"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: setupHistoryList) -> list:
    import capo_lightsail.types.setup_history

    out: list = []
    for item in value:
        out.append(capo_lightsail.types.setup_history.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> setupHistoryList:
    import capo_lightsail.types.setup_history

    out: setupHistoryList = []
    for item in data:
        out.append(capo_lightsail.types.setup_history.deserialize_aws_json_1_1(item))
    return out
