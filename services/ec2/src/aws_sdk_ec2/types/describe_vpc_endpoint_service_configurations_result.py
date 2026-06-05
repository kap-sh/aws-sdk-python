"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeVpcEndpointServiceConfigurationsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.service_configuration_set
    import aws_sdk_ec2.types.string


class DescribeVpcEndpointServiceConfigurationsResult(TypedDict):
    service_configurations: NotRequired[
        "aws_sdk_ec2.types.service_configuration_set.ServiceConfigurationSet"
    ]
    """<p>Information about the services.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeVpcEndpointServiceConfigurationsResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "service_configurations" in value:
        import aws_sdk_ec2.types.service_configuration_set

        aws_sdk_ec2.types.service_configuration_set.serialize_ec2_query(
            value["service_configurations"], pairs, f"{prefix}.ServiceConfigurationSet"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(
    el: Element,
) -> DescribeVpcEndpointServiceConfigurationsResult:
    out: DescribeVpcEndpointServiceConfigurationsResult = {}  # type: ignore[typeddict-item]
    if el.find("ServiceConfigurationSet") is not None:
        import aws_sdk_ec2.types.service_configuration_set

        out["service_configurations"] = (
            aws_sdk_ec2.types.service_configuration_set.deserialize_ec2_query(
                el, "ServiceConfigurationSet"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
