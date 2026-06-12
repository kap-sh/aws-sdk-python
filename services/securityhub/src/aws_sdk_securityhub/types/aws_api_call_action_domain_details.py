"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsApiCallActionDomainDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsApiCallActionDomainDetails(TypedDict):
    domain: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the DNS domain that issued the API call.</p> <p>Length Constraints: 128.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsApiCallActionDomainDetails) -> dict:
    out: dict = {}
    if "domain" in value:
        out["Domain"] = value["domain"]
    return out


def deserialize_json(data: dict) -> AwsApiCallActionDomainDetails:
    out: AwsApiCallActionDomainDetails = {}  # type: ignore[typeddict-item]
    if "Domain" in data:
        out["domain"] = data["Domain"]
    return out
