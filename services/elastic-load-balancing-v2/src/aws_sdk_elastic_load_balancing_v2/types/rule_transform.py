"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#RuleTransform``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing_v2.types.host_header_rewrite_config
    import aws_sdk_elastic_load_balancing_v2.types.transform_type_enum
    import aws_sdk_elastic_load_balancing_v2.types.url_rewrite_config


class RuleTransform(TypedDict):
    type: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.transform_type_enum.TransformTypeEnum"
    ]
    """<p>The type of transform. </p> <ul> <li> <p> <code>host-header-rewrite</code> - Rewrite the host header.</p> </li> <li> <p> <code>url-rewrite</code> - Rewrite the request URL.</p> </li> </ul>"""
    host_header_rewrite_config: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.host_header_rewrite_config.HostHeaderRewriteConfig"
    ]
    """<p>Information about a host header rewrite transform. This transform modifies the host header in an HTTP request. Specify only when <code>Type</code> is <code>host-header-rewrite</code>.</p>"""
    url_rewrite_config: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.url_rewrite_config.UrlRewriteConfig"
    ]
    """<p>Information about a URL rewrite transform. This transform modifies the request URL. Specify only when <code>Type</code> is <code>url-rewrite</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: RuleTransform, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "type" in value:
        import aws_sdk_elastic_load_balancing_v2.types.transform_type_enum

        aws_sdk_elastic_load_balancing_v2.types.transform_type_enum.serialize_query(
            value["type"], pairs, f"{prefix}.Type"
        )
    if "host_header_rewrite_config" in value:
        import aws_sdk_elastic_load_balancing_v2.types.host_header_rewrite_config

        aws_sdk_elastic_load_balancing_v2.types.host_header_rewrite_config.serialize_query(
            value["host_header_rewrite_config"],
            pairs,
            f"{prefix}.HostHeaderRewriteConfig",
        )
    if "url_rewrite_config" in value:
        import aws_sdk_elastic_load_balancing_v2.types.url_rewrite_config

        aws_sdk_elastic_load_balancing_v2.types.url_rewrite_config.serialize_query(
            value["url_rewrite_config"], pairs, f"{prefix}.UrlRewriteConfig"
        )


def deserialize_query(el: Element) -> RuleTransform:
    out: RuleTransform = {}  # type: ignore[typeddict-item]
    child_type = el.find("Type")
    if child_type is not None:
        import aws_sdk_elastic_load_balancing_v2.types.transform_type_enum

        out["type"] = (
            aws_sdk_elastic_load_balancing_v2.types.transform_type_enum.deserialize_query(
                child_type
            )
        )
    child_host_header_rewrite_config = el.find("HostHeaderRewriteConfig")
    if child_host_header_rewrite_config is not None:
        import aws_sdk_elastic_load_balancing_v2.types.host_header_rewrite_config

        out["host_header_rewrite_config"] = (
            aws_sdk_elastic_load_balancing_v2.types.host_header_rewrite_config.deserialize_query(
                child_host_header_rewrite_config
            )
        )
    child_url_rewrite_config = el.find("UrlRewriteConfig")
    if child_url_rewrite_config is not None:
        import aws_sdk_elastic_load_balancing_v2.types.url_rewrite_config

        out["url_rewrite_config"] = (
            aws_sdk_elastic_load_balancing_v2.types.url_rewrite_config.deserialize_query(
                child_url_rewrite_config
            )
        )
    return out
