"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#AccessControlEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pca_connector_ad.types.access_control_entry_summary

AccessControlEntryList: TypeAlias = list[
    "aws_sdk_pca_connector_ad.types.access_control_entry_summary.AccessControlEntrySummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AccessControlEntryList) -> list:
    import aws_sdk_pca_connector_ad.types.access_control_entry_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_pca_connector_ad.types.access_control_entry_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AccessControlEntryList:
    import aws_sdk_pca_connector_ad.types.access_control_entry_summary

    out: AccessControlEntryList = []
    for item in data:
        out.append(
            aws_sdk_pca_connector_ad.types.access_control_entry_summary.deserialize_json(
                item
            )
        )
    return out
