"""Generated from Smithy shape ``com.amazonaws.vpclattice#ListResourceConfigurationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.domain_verification_identifier
    import aws_sdk_vpc_lattice.types.max_results
    import aws_sdk_vpc_lattice.types.next_token
    import aws_sdk_vpc_lattice.types.resource_configuration_identifier
    import aws_sdk_vpc_lattice.types.resource_gateway_identifier


class ListResourceConfigurationsRequest(TypedDict, closed=True):
    resource_gateway_identifier: NotRequired[
        "aws_sdk_vpc_lattice.types.resource_gateway_identifier.ResourceGatewayIdentifier"
    ]
    """<p>The ID of the resource gateway for the resource configuration.</p>"""
    resource_configuration_group_identifier: NotRequired[
        "aws_sdk_vpc_lattice.types.resource_configuration_identifier.ResourceConfigurationIdentifier"
    ]
    """<p>The ID of the resource configuration of type <code>Group</code>.</p>"""
    domain_verification_identifier: NotRequired[
        "aws_sdk_vpc_lattice.types.domain_verification_identifier.DomainVerificationIdentifier"
    ]
    """<p> The domain verification ID. </p>"""
    max_results: NotRequired["aws_sdk_vpc_lattice.types.max_results.MaxResults"]
    """<p>The maximum page size.</p>"""
    next_token: NotRequired["aws_sdk_vpc_lattice.types.next_token.NextToken"]
    """<p>A pagination token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListResourceConfigurationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListResourceConfigurationsRequest:
    out: ListResourceConfigurationsRequest = {}  # type: ignore[typeddict-item]
    return out
