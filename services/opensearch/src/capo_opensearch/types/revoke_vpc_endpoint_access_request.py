"""Generated from Smithy shape ``com.amazonaws.opensearch#RevokeVpcEndpointAccessRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.aws_account
    import capo_opensearch.types.aws_service_principal
    import capo_opensearch.types.domain_name
    import capo_opensearch.types.service_options


class RevokeVpcEndpointAccessRequest(TypedDict, closed=True):
    domain_name: "capo_opensearch.types.domain_name.DomainName"
    """<p>The name of the OpenSearch Service domain.</p>"""
    account: NotRequired["capo_opensearch.types.aws_account.AWSAccount"]
    """<p>The account ID to revoke access from.</p>"""
    service: NotRequired[
        "capo_opensearch.types.aws_service_principal.AWSServicePrincipal"
    ]
    """<p>The service SP to revoke access from.</p>"""
    service_options: NotRequired["capo_opensearch.types.service_options.ServiceOptions"]
    """<p>The options for the service, including the supported Regions for the endpoint access.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RevokeVpcEndpointAccessRequest) -> dict:
    out: dict = {}
    if "account" in value:
        out["Account"] = value["account"]
    if "service" in value:
        import capo_opensearch.types.aws_service_principal

        out["Service"] = capo_opensearch.types.aws_service_principal.serialize_json(
            value["service"]
        )
    if "service_options" in value:
        import capo_opensearch.types.service_options

        out["ServiceOptions"] = capo_opensearch.types.service_options.serialize_json(
            value["service_options"]
        )
    return out


def deserialize_json(data: dict) -> RevokeVpcEndpointAccessRequest:
    out: RevokeVpcEndpointAccessRequest = {}  # type: ignore[typeddict-item]
    if "Account" in data:
        out["account"] = data["Account"]
    if "Service" in data:
        import capo_opensearch.types.aws_service_principal

        out["service"] = capo_opensearch.types.aws_service_principal.deserialize_json(
            data["Service"]
        )
    if "ServiceOptions" in data:
        import capo_opensearch.types.service_options

        out["service_options"] = capo_opensearch.types.service_options.deserialize_json(
            data["ServiceOptions"]
        )
    return out
