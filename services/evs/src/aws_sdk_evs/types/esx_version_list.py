"""Generated from Smithy shape ``com.amazonaws.evs#EsxVersionList``."""

from typing import TypeAlias

EsxVersionList: TypeAlias = list["str"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EsxVersionList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> EsxVersionList:
    return list(data)
