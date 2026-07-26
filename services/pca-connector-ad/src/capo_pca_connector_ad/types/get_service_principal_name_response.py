"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#GetServicePrincipalNameResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pca_connector_ad.types.service_principal_name


class GetServicePrincipalNameResponse(TypedDict, closed=True):
    service_principal_name: NotRequired[
        "capo_pca_connector_ad.types.service_principal_name.ServicePrincipalName"
    ]
    """<p>The service principal name that the connector uses to authenticate with Active Directory.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetServicePrincipalNameResponse) -> dict:
    out: dict = {}
    if "service_principal_name" in value:
        import capo_pca_connector_ad.types.service_principal_name

        out["ServicePrincipalName"] = (
            capo_pca_connector_ad.types.service_principal_name.serialize_json(
                value["service_principal_name"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetServicePrincipalNameResponse:
    out: GetServicePrincipalNameResponse = {}  # type: ignore[typeddict-item]
    if "ServicePrincipalName" in data:
        import capo_pca_connector_ad.types.service_principal_name

        out["service_principal_name"] = (
            capo_pca_connector_ad.types.service_principal_name.deserialize_json(
                data["ServicePrincipalName"]
            )
        )
    return out
