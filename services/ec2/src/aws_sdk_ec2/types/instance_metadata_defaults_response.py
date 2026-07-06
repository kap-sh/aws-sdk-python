"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceMetadataDefaultsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boxed_integer
    import aws_sdk_ec2.types.http_tokens_enforced_state
    import aws_sdk_ec2.types.http_tokens_state
    import aws_sdk_ec2.types.instance_metadata_endpoint_state
    import aws_sdk_ec2.types.instance_metadata_tags_state
    import aws_sdk_ec2.types.managed_by
    import aws_sdk_ec2.types.string


class InstanceMetadataDefaultsResponse(TypedDict, closed=True):
    http_tokens: NotRequired["aws_sdk_ec2.types.http_tokens_state.HttpTokensState"]
    """<p>Indicates whether IMDSv2 is required.</p> <ul> <li> <p> <code>optional</code> – IMDSv2 is optional, which means that you can use either IMDSv2 or IMDSv1.</p> </li> <li> <p> <code>required</code> – IMDSv2 is required, which means that IMDSv1 is disabled, and you must use IMDSv2.</p> </li> </ul>"""
    http_put_response_hop_limit: NotRequired[
        "aws_sdk_ec2.types.boxed_integer.BoxedInteger"
    ]
    """<p>The maximum number of hops that the metadata token can travel.</p>"""
    http_endpoint: NotRequired[
        "aws_sdk_ec2.types.instance_metadata_endpoint_state.InstanceMetadataEndpointState"
    ]
    """<p>Indicates whether the IMDS endpoint for an instance is enabled or disabled. When disabled, the instance metadata can't be accessed.</p>"""
    instance_metadata_tags: NotRequired[
        "aws_sdk_ec2.types.instance_metadata_tags_state.InstanceMetadataTagsState"
    ]
    r"""<p>Indicates whether access to instance tags from the instance metadata is enabled or disabled. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/work-with-tags-in-IMDS.html\">View tags for your EC2 instances using instance metadata</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    managed_by: NotRequired["aws_sdk_ec2.types.managed_by.ManagedBy"]
    """<p>The entity that manages the IMDS default settings. Possible values include:</p> <ul> <li> <p> <code>account</code> - The IMDS default settings are managed by the account.</p> </li> <li> <p> <code>declarative-policy</code> - The IMDS default settings are managed by a declarative policy and can't be modified by the account.</p> </li> </ul>"""
    managed_exception_message: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The customized exception message that is specified in the declarative policy.</p>"""
    http_tokens_enforced: NotRequired[
        "aws_sdk_ec2.types.http_tokens_enforced_state.HttpTokensEnforcedState"
    ]
    """<p>Indicates whether to enforce the requirement of IMDSv2 on an instance at the time of launch. When enforcement is enabled, the instance can't launch unless IMDSv2 (<code>HttpTokens</code>) is set to <code>required</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InstanceMetadataDefaultsResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "http_tokens" in value:
        import aws_sdk_ec2.types.http_tokens_state

        aws_sdk_ec2.types.http_tokens_state.serialize_ec2_query(
            value["http_tokens"], pairs, f"{prefix}.HttpTokens"
        )
    if "http_put_response_hop_limit" in value:
        pairs.append(
            (
                f"{prefix}.HttpPutResponseHopLimit",
                str(value["http_put_response_hop_limit"]),
            )
        )
    if "http_endpoint" in value:
        import aws_sdk_ec2.types.instance_metadata_endpoint_state

        aws_sdk_ec2.types.instance_metadata_endpoint_state.serialize_ec2_query(
            value["http_endpoint"], pairs, f"{prefix}.HttpEndpoint"
        )
    if "instance_metadata_tags" in value:
        import aws_sdk_ec2.types.instance_metadata_tags_state

        aws_sdk_ec2.types.instance_metadata_tags_state.serialize_ec2_query(
            value["instance_metadata_tags"], pairs, f"{prefix}.InstanceMetadataTags"
        )
    if "managed_by" in value:
        import aws_sdk_ec2.types.managed_by

        aws_sdk_ec2.types.managed_by.serialize_ec2_query(
            value["managed_by"], pairs, f"{prefix}.ManagedBy"
        )
    if "managed_exception_message" in value:
        pairs.append(
            (
                f"{prefix}.ManagedExceptionMessage",
                str(value["managed_exception_message"]),
            )
        )
    if "http_tokens_enforced" in value:
        import aws_sdk_ec2.types.http_tokens_enforced_state

        aws_sdk_ec2.types.http_tokens_enforced_state.serialize_ec2_query(
            value["http_tokens_enforced"], pairs, f"{prefix}.HttpTokensEnforced"
        )


def deserialize_ec2_query(el: Element) -> InstanceMetadataDefaultsResponse:
    out: InstanceMetadataDefaultsResponse = {}  # type: ignore[typeddict-item]
    child_http_tokens = el.find("HttpTokens")
    if child_http_tokens is not None:
        import aws_sdk_ec2.types.http_tokens_state

        out["http_tokens"] = aws_sdk_ec2.types.http_tokens_state.deserialize_ec2_query(
            child_http_tokens
        )
    child_http_put_response_hop_limit = el.find("HttpPutResponseHopLimit")
    if child_http_put_response_hop_limit is not None:
        out["http_put_response_hop_limit"] = int(
            child_http_put_response_hop_limit.text or ""
        )
    child_http_endpoint = el.find("HttpEndpoint")
    if child_http_endpoint is not None:
        import aws_sdk_ec2.types.instance_metadata_endpoint_state

        out["http_endpoint"] = (
            aws_sdk_ec2.types.instance_metadata_endpoint_state.deserialize_ec2_query(
                child_http_endpoint
            )
        )
    child_instance_metadata_tags = el.find("InstanceMetadataTags")
    if child_instance_metadata_tags is not None:
        import aws_sdk_ec2.types.instance_metadata_tags_state

        out["instance_metadata_tags"] = (
            aws_sdk_ec2.types.instance_metadata_tags_state.deserialize_ec2_query(
                child_instance_metadata_tags
            )
        )
    child_managed_by = el.find("ManagedBy")
    if child_managed_by is not None:
        import aws_sdk_ec2.types.managed_by

        out["managed_by"] = aws_sdk_ec2.types.managed_by.deserialize_ec2_query(
            child_managed_by
        )
    child_managed_exception_message = el.find("ManagedExceptionMessage")
    if child_managed_exception_message is not None:
        out["managed_exception_message"] = str(
            child_managed_exception_message.text or ""
        )
    child_http_tokens_enforced = el.find("HttpTokensEnforced")
    if child_http_tokens_enforced is not None:
        import aws_sdk_ec2.types.http_tokens_enforced_state

        out["http_tokens_enforced"] = (
            aws_sdk_ec2.types.http_tokens_enforced_state.deserialize_ec2_query(
                child_http_tokens_enforced
            )
        )
    return out
