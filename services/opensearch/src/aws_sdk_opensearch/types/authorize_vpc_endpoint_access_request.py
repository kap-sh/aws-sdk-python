"""Generated from Smithy shape ``com.amazonaws.opensearch#AuthorizeVpcEndpointAccessRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.aws_account
    import aws_sdk_opensearch.types.aws_service_principal
    import aws_sdk_opensearch.types.domain_name
    import aws_sdk_opensearch.types.service_options


class AuthorizeVpcEndpointAccessRequest(TypedDict):
    domain_name: "aws_sdk_opensearch.types.domain_name.DomainName"
    """<p>The name of the OpenSearch Service domain to provide access to.</p>"""
    account: NotRequired["aws_sdk_opensearch.types.aws_account.AWSAccount"]
    """<p>The Amazon Web Services account ID to grant access to.</p>"""
    service: NotRequired[
        "aws_sdk_opensearch.types.aws_service_principal.AWSServicePrincipal"
    ]
    """<p>The Amazon Web Services service SP to grant access to.</p>"""
    service_options: NotRequired[
        "aws_sdk_opensearch.types.service_options.ServiceOptions"
    ]
    """<p>The options for the service, including the supported Regions for the endpoint access.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AuthorizeVpcEndpointAccessRequest) -> dict:
    out: dict = {}
    if "account" in value:
        out["Account"] = value["account"]
    if "service" in value:
        import aws_sdk_opensearch.types.aws_service_principal

        out["Service"] = aws_sdk_opensearch.types.aws_service_principal.serialize_json(
            value["service"]
        )
    if "service_options" in value:
        import aws_sdk_opensearch.types.service_options

        out["ServiceOptions"] = aws_sdk_opensearch.types.service_options.serialize_json(
            value["service_options"]
        )
    return out


def deserialize_json(data: dict) -> AuthorizeVpcEndpointAccessRequest:
    out: AuthorizeVpcEndpointAccessRequest = {}  # type: ignore[typeddict-item]
    if "Account" in data:
        out["account"] = data["Account"]
    if "Service" in data:
        import aws_sdk_opensearch.types.aws_service_principal

        out["service"] = (
            aws_sdk_opensearch.types.aws_service_principal.deserialize_json(
                data["Service"]
            )
        )
    if "ServiceOptions" in data:
        import aws_sdk_opensearch.types.service_options

        out["service_options"] = (
            aws_sdk_opensearch.types.service_options.deserialize_json(
                data["ServiceOptions"]
            )
        )
    return out
