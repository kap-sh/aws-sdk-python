"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#RevokeVpcEndpointAccessRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_elasticsearch_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.aws_account
    import aws_sdk_elasticsearch_service.types.domain_name


class RevokeVpcEndpointAccessRequest(TypedDict, closed=True):
    domain_name: "aws_sdk_elasticsearch_service.types.domain_name.DomainName"
    """<p>The name of the OpenSearch Service domain.</p>"""
    account: "aws_sdk_elasticsearch_service.types.aws_account.AWSAccount"
    """<p>The account ID to revoke access from.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RevokeVpcEndpointAccessRequest) -> dict:
    out: dict = {}
    out["Account"] = value["account"]
    return out


def deserialize_json(data: dict) -> RevokeVpcEndpointAccessRequest:
    out: RevokeVpcEndpointAccessRequest = {}  # type: ignore[typeddict-item]
    if "Account" in data:
        out["account"] = data["Account"]
    else:
        raise DeserializationError("RevokeVpcEndpointAccessRequest.account required")
    return out
