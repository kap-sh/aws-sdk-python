"""Generated from Smithy shape ``com.amazonaws.appconfig#ExtensionAssociationSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_appconfig.types.extension_association_summary

ExtensionAssociationSummaries: TypeAlias = list[
    "aws_sdk_appconfig.types.extension_association_summary.ExtensionAssociationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ExtensionAssociationSummaries) -> list:
    import aws_sdk_appconfig.types.extension_association_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_appconfig.types.extension_association_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ExtensionAssociationSummaries:
    import aws_sdk_appconfig.types.extension_association_summary

    out: ExtensionAssociationSummaries = []
    for item in data:
        out.append(
            aws_sdk_appconfig.types.extension_association_summary.deserialize_json(item)
        )
    return out
