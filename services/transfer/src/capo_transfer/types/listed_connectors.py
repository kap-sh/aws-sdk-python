"""Generated from Smithy shape ``com.amazonaws.transfer#ListedConnectors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_transfer.types.listed_connector

ListedConnectors: TypeAlias = list[
    "capo_transfer.types.listed_connector.ListedConnector"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListedConnectors) -> list:
    import capo_transfer.types.listed_connector

    out: list = []
    for item in value:
        out.append(capo_transfer.types.listed_connector.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ListedConnectors:
    import capo_transfer.types.listed_connector

    out: ListedConnectors = []
    for item in data:
        out.append(capo_transfer.types.listed_connector.deserialize_aws_json_1_1(item))
    return out
