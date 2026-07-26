"""Generated from Smithy shape ``com.amazonaws.transfer#ListedHostKeys``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_transfer.types.listed_host_key

ListedHostKeys: TypeAlias = list["capo_transfer.types.listed_host_key.ListedHostKey"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListedHostKeys) -> list:
    import capo_transfer.types.listed_host_key

    out: list = []
    for item in value:
        out.append(capo_transfer.types.listed_host_key.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ListedHostKeys:
    import capo_transfer.types.listed_host_key

    out: ListedHostKeys = []
    for item in data:
        out.append(capo_transfer.types.listed_host_key.deserialize_aws_json_1_1(item))
    return out
