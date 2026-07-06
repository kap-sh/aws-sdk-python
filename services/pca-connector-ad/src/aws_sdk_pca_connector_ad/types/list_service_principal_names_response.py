"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#ListServicePrincipalNamesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pca_connector_ad.types.next_token
    import aws_sdk_pca_connector_ad.types.service_principal_name_list


class ListServicePrincipalNamesResponse(TypedDict, closed=True):
    service_principal_names: NotRequired[
        "aws_sdk_pca_connector_ad.types.service_principal_name_list.ServicePrincipalNameList"
    ]
    """<p>The service principal name, if any, that the connector uses to authenticate with Active Directory.</p>"""
    next_token: NotRequired["aws_sdk_pca_connector_ad.types.next_token.NextToken"]
    """<p>Use this parameter when paginating results in a subsequent request after you receive a response with truncated results. Set it to the value of the <code>NextToken</code> parameter from the response you just received.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListServicePrincipalNamesResponse) -> dict:
    out: dict = {}
    if "service_principal_names" in value:
        import aws_sdk_pca_connector_ad.types.service_principal_name_list

        out["ServicePrincipalNames"] = (
            aws_sdk_pca_connector_ad.types.service_principal_name_list.serialize_json(
                value["service_principal_names"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListServicePrincipalNamesResponse:
    out: ListServicePrincipalNamesResponse = {}  # type: ignore[typeddict-item]
    if "ServicePrincipalNames" in data:
        import aws_sdk_pca_connector_ad.types.service_principal_name_list

        out["service_principal_names"] = (
            aws_sdk_pca_connector_ad.types.service_principal_name_list.deserialize_json(
                data["ServicePrincipalNames"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
