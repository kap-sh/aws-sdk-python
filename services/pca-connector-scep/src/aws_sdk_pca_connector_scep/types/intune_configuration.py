"""Generated from Smithy shape ``com.amazonaws.pcaconnectorscep#IntuneConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_pca_connector_scep.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pca_connector_scep.types.azure_application_id
    import aws_sdk_pca_connector_scep.types.azure_domain


class IntuneConfiguration(TypedDict):
    azure_application_id: (
        "aws_sdk_pca_connector_scep.types.azure_application_id.AzureApplicationId"
    )
    """<p>The directory (tenant) ID from your Microsoft Entra ID app registration.</p>"""
    domain: "aws_sdk_pca_connector_scep.types.azure_domain.AzureDomain"
    """<p>The primary domain from your Microsoft Entra ID app registration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IntuneConfiguration) -> dict:
    out: dict = {}
    out["AzureApplicationId"] = value["azure_application_id"]
    out["Domain"] = value["domain"]
    return out


def deserialize_json(data: dict) -> IntuneConfiguration:
    out: IntuneConfiguration = {}  # type: ignore[typeddict-item]
    if "AzureApplicationId" in data:
        out["azure_application_id"] = data["AzureApplicationId"]
    else:
        raise DeserializationError("IntuneConfiguration.azure_application_id required")
    if "Domain" in data:
        out["domain"] = data["Domain"]
    else:
        raise DeserializationError("IntuneConfiguration.domain required")
    return out
