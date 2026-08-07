"""Generated from Smithy shape ``com.amazonaws.autoscaling#InstanceMetadataOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.instance_metadata_endpoint_state
    import capo_auto_scaling.types.instance_metadata_http_put_response_hop_limit
    import capo_auto_scaling.types.instance_metadata_http_tokens_state


class InstanceMetadataOptions(TypedDict, closed=True):
    http_tokens: NotRequired[
        "capo_auto_scaling.types.instance_metadata_http_tokens_state.InstanceMetadataHttpTokensState"
    ]
    """<p>The state of token usage for your instance metadata requests. If the parameter is not specified in the request, the default state is <code>optional</code>.</p> <p>If the state is <code>optional</code>, you can choose to retrieve instance metadata with or without a signed token header on your request. If you retrieve the IAM role credentials without a token, the version 1.0 role credentials are returned. If you retrieve the IAM role credentials using a valid signed token, the version 2.0 role credentials are returned.</p> <p>If the state is <code>required</code>, you must send a signed token header with any instance metadata retrieval requests. In this state, retrieving the IAM role credentials always returns the version 2.0 credentials; the version 1.0 credentials are not available.</p>"""
    http_put_response_hop_limit: NotRequired[
        "capo_auto_scaling.types.instance_metadata_http_put_response_hop_limit.InstanceMetadataHttpPutResponseHopLimit"
    ]
    """<p>The desired HTTP PUT response hop limit for instance metadata requests. The larger the number, the further instance metadata requests can travel.</p> <p>Default: 1</p>"""
    http_endpoint: NotRequired[
        "capo_auto_scaling.types.instance_metadata_endpoint_state.InstanceMetadataEndpointState"
    ]
    """<p>This parameter enables or disables the HTTP metadata endpoint on your instances. If the parameter is not specified, the default state is <code>enabled</code>.</p> <note> <p>If you specify a value of <code>disabled</code>, you will not be able to access your instance metadata. </p> </note>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: InstanceMetadataOptions, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "http_tokens" in value:
        import capo_auto_scaling.types.instance_metadata_http_tokens_state

        capo_auto_scaling.types.instance_metadata_http_tokens_state.serialize_query(
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
        import capo_auto_scaling.types.instance_metadata_endpoint_state

        capo_auto_scaling.types.instance_metadata_endpoint_state.serialize_query(
            value["http_endpoint"], pairs, f"{key_prefix}HttpEndpoint"
        )


def deserialize_query(el: Element) -> InstanceMetadataOptions:
    out: InstanceMetadataOptions = {}  # type: ignore[typeddict-item]
    child_http_tokens = el.find("HttpTokens")
    if child_http_tokens is not None:
        import capo_auto_scaling.types.instance_metadata_http_tokens_state

        out["http_tokens"] = (
            capo_auto_scaling.types.instance_metadata_http_tokens_state.deserialize_query(
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
        import capo_auto_scaling.types.instance_metadata_endpoint_state

        out["http_endpoint"] = (
            capo_auto_scaling.types.instance_metadata_endpoint_state.deserialize_query(
                child_http_endpoint
            )
        )
    return out
