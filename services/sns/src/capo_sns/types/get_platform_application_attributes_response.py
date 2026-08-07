"""Generated from Smithy shape ``com.amazonaws.sns#GetPlatformApplicationAttributesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sns._protocol.xml import Element

if TYPE_CHECKING:
    import capo_sns.types.map_string_to_string


class GetPlatformApplicationAttributesResponse(TypedDict, closed=True):
    attributes: NotRequired["capo_sns.types.map_string_to_string.MapStringToString"]
    """<p>Attributes include the following:</p> <ul> <li> <p> <code>AppleCertificateExpiryDate</code> – The expiry date of the SSL certificate used to configure certificate-based authentication.</p> </li> <li> <p> <code>ApplePlatformTeamID</code> – The Apple developer account ID used to configure token-based authentication.</p> </li> <li> <p> <code>ApplePlatformBundleID</code> – The app identifier used to configure token-based authentication.</p> </li> <li> <p> <code>AuthenticationMethod</code> – Returns the credential type used when sending push notifications from application to APNS/APNS_Sandbox, or application to GCM.</p> <ul> <li> <p>APNS – Returns the token or certificate.</p> </li> <li> <p>GCM – Returns the token or key.</p> </li> </ul> </li> <li> <p> <code>EventEndpointCreated</code> – Topic ARN to which EndpointCreated event notifications should be sent.</p> </li> <li> <p> <code>EventEndpointDeleted</code> – Topic ARN to which EndpointDeleted event notifications should be sent.</p> </li> <li> <p> <code>EventEndpointUpdated</code> – Topic ARN to which EndpointUpdate event notifications should be sent.</p> </li> <li> <p> <code>EventDeliveryFailure</code> – Topic ARN to which DeliveryFailure event notifications should be sent upon Direct Publish delivery failure (permanent) to one of the application's endpoints.</p> </li> </ul>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetPlatformApplicationAttributesResponse,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "attributes" in value:
        import capo_sns.types.map_string_to_string

        capo_sns.types.map_string_to_string.serialize_query(
            value["attributes"], pairs, f"{key_prefix}Attributes"
        )


def deserialize_query(el: Element) -> GetPlatformApplicationAttributesResponse:
    out: GetPlatformApplicationAttributesResponse = {}  # type: ignore[typeddict-item]
    child_attributes = el.find("Attributes")
    if child_attributes is not None:
        import capo_sns.types.map_string_to_string

        out["attributes"] = capo_sns.types.map_string_to_string.deserialize_query(
            child_attributes
        )
    return out
