"""Generated from Smithy shape ``com.amazonaws.ssm#OpsItemParameterNamesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.string

OpsItemParameterNamesList: TypeAlias = list["capo_ssm.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpsItemParameterNamesList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> OpsItemParameterNamesList:
    return [item for item in data if item is not None]
