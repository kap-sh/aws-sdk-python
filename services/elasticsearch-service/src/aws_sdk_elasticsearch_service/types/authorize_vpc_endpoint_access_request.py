"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#AuthorizeVpcEndpointAccessRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_elasticsearch_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.aws_account
    import aws_sdk_elasticsearch_service.types.domain_name


class AuthorizeVpcEndpointAccessRequest(TypedDict):
    domain_name: "aws_sdk_elasticsearch_service.types.domain_name.DomainName"
    """<p>The name of the OpenSearch Service domain to provide access to.</p>"""
    account: "aws_sdk_elasticsearch_service.types.aws_account.AWSAccount"
    """<p>The account ID to grant access to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AuthorizeVpcEndpointAccessRequest) -> dict:
    out: dict = {}
    out["Account"] = value["account"]
    return out


def deserialize_json(data: dict) -> AuthorizeVpcEndpointAccessRequest:
    out: AuthorizeVpcEndpointAccessRequest = {}  # type: ignore[typeddict-item]
    if "Account" in data:
        out["account"] = data["Account"]
    else:
        raise DeserializationError("AuthorizeVpcEndpointAccessRequest.account required")
    return out
