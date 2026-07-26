"""Generated from Smithy shape ``com.amazonaws.cloudhsm#ClientList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudhsm.types.client_arn

ClientList: TypeAlias = list["capo_cloudhsm.types.client_arn.ClientArn"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClientList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ClientList:
    return list(data)
