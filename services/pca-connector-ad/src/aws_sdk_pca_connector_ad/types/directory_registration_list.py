"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#DirectoryRegistrationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pca_connector_ad.types.directory_registration_summary

DirectoryRegistrationList: TypeAlias = list[
    "aws_sdk_pca_connector_ad.types.directory_registration_summary.DirectoryRegistrationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: DirectoryRegistrationList) -> list:
    import aws_sdk_pca_connector_ad.types.directory_registration_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_pca_connector_ad.types.directory_registration_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> DirectoryRegistrationList:
    import aws_sdk_pca_connector_ad.types.directory_registration_summary

    out: DirectoryRegistrationList = []
    for item in data:
        out.append(
            aws_sdk_pca_connector_ad.types.directory_registration_summary.deserialize_json(
                item
            )
        )
    return out
