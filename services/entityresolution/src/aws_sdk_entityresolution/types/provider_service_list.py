"""Generated from Smithy shape ``com.amazonaws.entityresolution#ProviderServiceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_entityresolution.types.provider_service_summary

ProviderServiceList: TypeAlias = list[
    "aws_sdk_entityresolution.types.provider_service_summary.ProviderServiceSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ProviderServiceList) -> list:
    import aws_sdk_entityresolution.types.provider_service_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_entityresolution.types.provider_service_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ProviderServiceList:
    import aws_sdk_entityresolution.types.provider_service_summary

    out: ProviderServiceList = []
    for item in data:
        out.append(
            aws_sdk_entityresolution.types.provider_service_summary.deserialize_json(
                item
            )
        )
    return out
