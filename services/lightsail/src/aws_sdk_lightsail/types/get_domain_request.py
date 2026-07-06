"""Generated from Smithy shape ``com.amazonaws.lightsail#GetDomainRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_lightsail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.domain_name


class GetDomainRequest(TypedDict, closed=True):
    domain_name: "aws_sdk_lightsail.types.domain_name.DomainName"
    """<p>The domain name for which your want to return information about.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDomainRequest) -> dict:
    out: dict = {}
    out["domainName"] = value["domain_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDomainRequest:
    out: GetDomainRequest = {}  # type: ignore[typeddict-item]
    if "domainName" in data:
        out["domain_name"] = data["domainName"]
    else:
        raise DeserializationError("GetDomainRequest.domain_name required")
    return out
