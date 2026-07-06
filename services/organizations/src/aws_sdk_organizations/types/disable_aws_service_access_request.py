"""Generated from Smithy shape ``com.amazonaws.organizations#DisableAWSServiceAccessRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_organizations.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_organizations.types.service_principal


class DisableAWSServiceAccessRequest(TypedDict, closed=True):
    service_principal: "aws_sdk_organizations.types.service_principal.ServicePrincipal"
    """<p>The service principal name of the Amazon Web Services service for which you want to disable integration with your organization. This is typically in the form of a URL, such as <code> <i>service-abbreviation</i>.amazonaws.com</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisableAWSServiceAccessRequest) -> dict:
    out: dict = {}
    out["ServicePrincipal"] = value["service_principal"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DisableAWSServiceAccessRequest:
    out: DisableAWSServiceAccessRequest = {}  # type: ignore[typeddict-item]
    if "ServicePrincipal" in data:
        out["service_principal"] = data["ServicePrincipal"]
    else:
        raise DeserializationError(
            "DisableAWSServiceAccessRequest.service_principal required"
        )
    return out
