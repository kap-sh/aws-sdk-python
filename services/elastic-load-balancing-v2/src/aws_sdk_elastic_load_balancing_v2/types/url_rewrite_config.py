"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#UrlRewriteConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing_v2.types.rewrite_config_list


class UrlRewriteConfig(TypedDict, closed=True):
    rewrites: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.rewrite_config_list.RewriteConfigList"
    ]
    """<p>The URL rewrite transform to apply to the request. The transform consists of a regular expression to match and a replacement string.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: UrlRewriteConfig, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "rewrites" in value:
        import aws_sdk_elastic_load_balancing_v2.types.rewrite_config_list

        aws_sdk_elastic_load_balancing_v2.types.rewrite_config_list.serialize_query(
            value["rewrites"], pairs, f"{prefix}.Rewrites"
        )


def deserialize_query(el: Element) -> UrlRewriteConfig:
    out: UrlRewriteConfig = {}  # type: ignore[typeddict-item]
    child_rewrites = el.find("Rewrites")
    if child_rewrites is not None:
        import aws_sdk_elastic_load_balancing_v2.types.rewrite_config_list

        out["rewrites"] = (
            aws_sdk_elastic_load_balancing_v2.types.rewrite_config_list.deserialize_query(
                child_rewrites
            )
        )
    return out
