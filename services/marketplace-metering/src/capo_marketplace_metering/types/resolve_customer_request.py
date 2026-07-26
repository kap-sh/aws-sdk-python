"""Generated from Smithy shape ``com.amazonaws.marketplacemetering#ResolveCustomerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_marketplace_metering.errors import DeserializationError

if TYPE_CHECKING:
    import capo_marketplace_metering.types.non_empty_string


class ResolveCustomerRequest(TypedDict, closed=True):
    registration_token: (
        "capo_marketplace_metering.types.non_empty_string.NonEmptyString"
    )
    """<p>When a buyer visits your website during the registration process, the buyer submits a registration token through the browser. The registration token is resolved to obtain a <code>CustomerIdentifier</code> along with the <code>CustomerAWSAccountId</code>, <code>ProductCode</code>, and <code>LicenseArn</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResolveCustomerRequest) -> dict:
    out: dict = {}
    out["RegistrationToken"] = value["registration_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResolveCustomerRequest:
    out: ResolveCustomerRequest = {}  # type: ignore[typeddict-item]
    if "RegistrationToken" in data:
        out["registration_token"] = data["RegistrationToken"]
    else:
        raise DeserializationError("ResolveCustomerRequest.registration_token required")
    return out
