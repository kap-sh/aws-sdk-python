"""Generated from Smithy shape ``com.amazonaws.appintegrations#DataIntegrationAssociationsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_appintegrations.types.data_integration_association_summary

DataIntegrationAssociationsList: TypeAlias = list[
    "aws_sdk_appintegrations.types.data_integration_association_summary.DataIntegrationAssociationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataIntegrationAssociationsList) -> list:
    import aws_sdk_appintegrations.types.data_integration_association_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_appintegrations.types.data_integration_association_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> DataIntegrationAssociationsList:
    import aws_sdk_appintegrations.types.data_integration_association_summary

    out: DataIntegrationAssociationsList = []
    for item in data:
        out.append(
            aws_sdk_appintegrations.types.data_integration_association_summary.deserialize_json(
                item
            )
        )
    return out
