"""Generated from Smithy shape ``com.amazonaws.evs#ConnectorsChecksList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_evs.types.connector_check

ConnectorsChecksList: TypeAlias = list["capo_evs.types.connector_check.ConnectorCheck"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ConnectorsChecksList) -> list:
    import capo_evs.types.connector_check

    out: list = []
    for item in value:
        out.append(capo_evs.types.connector_check.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> ConnectorsChecksList:
    import capo_evs.types.connector_check

    out: ConnectorsChecksList = []
    for item in data:
        out.append(capo_evs.types.connector_check.deserialize_aws_json_1_0(item))
    return out
