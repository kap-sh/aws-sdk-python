"""Generated from Smithy shape ``com.amazonaws.qbusiness#EligibleDataSources``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.eligible_data_source

EligibleDataSources: TypeAlias = list[
    "aws_sdk_qbusiness.types.eligible_data_source.EligibleDataSource"
]


# --- restJson1 ser/de ---
def serialize_json(value: EligibleDataSources) -> list:
    import aws_sdk_qbusiness.types.eligible_data_source

    out: list = []
    for item in value:
        out.append(aws_sdk_qbusiness.types.eligible_data_source.serialize_json(item))
    return out


def deserialize_json(data: list) -> EligibleDataSources:
    import aws_sdk_qbusiness.types.eligible_data_source

    out: EligibleDataSources = []
    for item in data:
        out.append(aws_sdk_qbusiness.types.eligible_data_source.deserialize_json(item))
    return out
