"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#ServicePrincipalNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pca_connector_ad.types.service_principal_name_summary

ServicePrincipalNameList: TypeAlias = list[
    "aws_sdk_pca_connector_ad.types.service_principal_name_summary.ServicePrincipalNameSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ServicePrincipalNameList) -> list:
    import aws_sdk_pca_connector_ad.types.service_principal_name_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_pca_connector_ad.types.service_principal_name_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ServicePrincipalNameList:
    import aws_sdk_pca_connector_ad.types.service_principal_name_summary

    out: ServicePrincipalNameList = []
    for item in data:
        out.append(
            aws_sdk_pca_connector_ad.types.service_principal_name_summary.deserialize_json(
                item
            )
        )
    return out
