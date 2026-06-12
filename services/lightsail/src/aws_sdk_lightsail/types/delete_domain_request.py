"""Generated from Smithy shape ``com.amazonaws.lightsail#DeleteDomainRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_lightsail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.domain_name


class DeleteDomainRequest(TypedDict):
    domain_name: "aws_sdk_lightsail.types.domain_name.DomainName"
    """<p>The specific domain name to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteDomainRequest) -> dict:
    out: dict = {}
    out["domainName"] = value["domain_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteDomainRequest:
    out: DeleteDomainRequest = {}  # type: ignore[typeddict-item]
    if "domainName" in data:
        out["domain_name"] = data["domainName"]
    else:
        raise DeserializationError("DeleteDomainRequest.domain_name required")
    return out
