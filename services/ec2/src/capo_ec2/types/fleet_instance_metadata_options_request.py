"""Generated from Smithy shape ``com.amazonaws.ec2#FleetInstanceMetadataOptionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.fleet_http_tokens_state
    import capo_ec2.types.fleet_instance_metadata_endpoint_state
    import capo_ec2.types.integer


class FleetInstanceMetadataOptionsRequest(TypedDict, closed=True):
    http_tokens: NotRequired[
        "capo_ec2.types.fleet_http_tokens_state.FleetHttpTokensState"
    ]
    """<p>Indicates whether IMDSv2 is required.</p> <ul> <li> <p> <code>optional</code> - IMDSv2 is optional, which means that you can use either IMDSv2 or IMDSv1.</p> </li> <li> <p> <code>required</code> - IMDSv2 is required, which means that IMDSv1 is disabled, and you must use IMDSv2.</p> </li> </ul>"""
    http_put_response_hop_limit: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The desired HTTP PUT response hop limit for instance metadata requests. The larger the number, the further instance metadata requests can travel.</p> <p>Default: <code>1</code> </p> <p>Possible values: Integers from 1 to 64</p>"""
    http_endpoint: NotRequired[
        "capo_ec2.types.fleet_instance_metadata_endpoint_state.FleetInstanceMetadataEndpointState"
    ]
    """<p>Enables or disables the HTTP metadata endpoint on your instances.</p> <ul> <li> <p> <code>enabled</code> - The HTTP metadata endpoint is enabled.</p> </li> <li> <p> <code>disabled</code> - The HTTP metadata endpoint is disabled.</p> </li> </ul>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: FleetInstanceMetadataOptionsRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "http_tokens" in value:
        import capo_ec2.types.fleet_http_tokens_state

        capo_ec2.types.fleet_http_tokens_state.serialize_ec2_query(
            value["http_tokens"], pairs, f"{key_prefix}HttpTokens"
        )
    if "http_put_response_hop_limit" in value:
        pairs.append(
            (
                f"{key_prefix}HttpPutResponseHopLimit",
                str(value["http_put_response_hop_limit"]),
            )
        )
    if "http_endpoint" in value:
        import capo_ec2.types.fleet_instance_metadata_endpoint_state

        capo_ec2.types.fleet_instance_metadata_endpoint_state.serialize_ec2_query(
            value["http_endpoint"], pairs, f"{key_prefix}HttpEndpoint"
        )


def deserialize_ec2_query(el: Element) -> FleetInstanceMetadataOptionsRequest:
    out: FleetInstanceMetadataOptionsRequest = {}  # type: ignore[typeddict-item]
    child_http_tokens = el.find("HttpTokens")
    if child_http_tokens is not None:
        import capo_ec2.types.fleet_http_tokens_state

        out["http_tokens"] = (
            capo_ec2.types.fleet_http_tokens_state.deserialize_ec2_query(
                child_http_tokens
            )
        )
    child_http_put_response_hop_limit = el.find("HttpPutResponseHopLimit")
    if child_http_put_response_hop_limit is not None:
        out["http_put_response_hop_limit"] = int(
            child_http_put_response_hop_limit.text or ""
        )
    child_http_endpoint = el.find("HttpEndpoint")
    if child_http_endpoint is not None:
        import capo_ec2.types.fleet_instance_metadata_endpoint_state

        out["http_endpoint"] = (
            capo_ec2.types.fleet_instance_metadata_endpoint_state.deserialize_ec2_query(
                child_http_endpoint
            )
        )
    return out
