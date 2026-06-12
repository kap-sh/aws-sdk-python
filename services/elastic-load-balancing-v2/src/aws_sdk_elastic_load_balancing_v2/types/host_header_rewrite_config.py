"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#HostHeaderRewriteConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing_v2.types.rewrite_config_list


class HostHeaderRewriteConfig(TypedDict):
    rewrites: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.rewrite_config_list.RewriteConfigList"
    ]
    """<p>The host header rewrite transform. Each transform consists of a regular expression to match and a replacement string.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: HostHeaderRewriteConfig, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "rewrites" in value:
        import aws_sdk_elastic_load_balancing_v2.types.rewrite_config_list

        aws_sdk_elastic_load_balancing_v2.types.rewrite_config_list.serialize_query(
            value["rewrites"], pairs, f"{prefix}.Rewrites"
        )


def deserialize_query(el: Element) -> HostHeaderRewriteConfig:
    out: HostHeaderRewriteConfig = {}  # type: ignore[typeddict-item]
    child_rewrites = el.find("Rewrites")
    if child_rewrites is not None:
        import aws_sdk_elastic_load_balancing_v2.types.rewrite_config_list

        out["rewrites"] = (
            aws_sdk_elastic_load_balancing_v2.types.rewrite_config_list.deserialize_query(
                child_rewrites
            )
        )
    return out
