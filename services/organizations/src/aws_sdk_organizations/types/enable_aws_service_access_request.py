"""Generated from Smithy shape ``com.amazonaws.organizations#EnableAWSServiceAccessRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_organizations.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_organizations.types.service_principal


class EnableAWSServiceAccessRequest(TypedDict, closed=True):
    service_principal: "aws_sdk_organizations.types.service_principal.ServicePrincipal"
    """<p>The service principal name of the Amazon Web Services service for which you want to enable integration with your organization. This is typically in the form of a URL, such as <code> <i>service-abbreviation</i>.amazonaws.com</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EnableAWSServiceAccessRequest) -> dict:
    out: dict = {}
    out["ServicePrincipal"] = value["service_principal"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EnableAWSServiceAccessRequest:
    out: EnableAWSServiceAccessRequest = {}  # type: ignore[typeddict-item]
    if "ServicePrincipal" in data:
        out["service_principal"] = data["ServicePrincipal"]
    else:
        raise DeserializationError(
            "EnableAWSServiceAccessRequest.service_principal required"
        )
    return out
