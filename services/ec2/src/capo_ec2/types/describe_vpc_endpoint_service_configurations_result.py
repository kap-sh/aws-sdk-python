"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeVpcEndpointServiceConfigurationsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.service_configuration_set
    import capo_ec2.types.string


class DescribeVpcEndpointServiceConfigurationsResult(TypedDict, closed=True):
    service_configurations: NotRequired[
        "capo_ec2.types.service_configuration_set.ServiceConfigurationSet"
    ]
    """<p>Information about the services.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeVpcEndpointServiceConfigurationsResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "service_configurations" in value:
        import capo_ec2.types.service_configuration_set

        capo_ec2.types.service_configuration_set.serialize_ec2_query(
            value["service_configurations"],
            pairs,
            f"{key_prefix}ServiceConfigurationSet",
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_ec2_query(
    el: Element,
) -> DescribeVpcEndpointServiceConfigurationsResult:
    out: DescribeVpcEndpointServiceConfigurationsResult = {}  # type: ignore[typeddict-item]
    if el.find("ServiceConfigurationSet") is not None:
        import capo_ec2.types.service_configuration_set

        out["service_configurations"] = (
            capo_ec2.types.service_configuration_set.deserialize_ec2_query(
                el, "ServiceConfigurationSet"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
