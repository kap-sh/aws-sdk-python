"""Generated from Smithy shape ``com.amazonaws.autoscaling#DescribeWarmPoolAnswer``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_auto_scaling.types.instances
    import aws_sdk_auto_scaling.types.warm_pool_configuration
    import aws_sdk_auto_scaling.types.xml_string


class DescribeWarmPoolAnswer(TypedDict):
    warm_pool_configuration: NotRequired[
        "aws_sdk_auto_scaling.types.warm_pool_configuration.WarmPoolConfiguration"
    ]
    """<p>The warm pool configuration details. </p>"""
    instances: NotRequired["aws_sdk_auto_scaling.types.instances.Instances"]
    """<p>The instances that are currently in the warm pool.</p>"""
    next_token: NotRequired["aws_sdk_auto_scaling.types.xml_string.XmlString"]
    """<p>This string indicates that the response contains more items than can be returned in a single response. To receive additional items, specify this string for the <code>NextToken</code> value when requesting the next set of items. This value is null when there are no more items to return.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeWarmPoolAnswer, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "warm_pool_configuration" in value:
        import aws_sdk_auto_scaling.types.warm_pool_configuration

        aws_sdk_auto_scaling.types.warm_pool_configuration.serialize_query(
            value["warm_pool_configuration"], pairs, f"{prefix}.WarmPoolConfiguration"
        )
    if "instances" in value:
        import aws_sdk_auto_scaling.types.instances

        aws_sdk_auto_scaling.types.instances.serialize_query(
            value["instances"], pairs, f"{prefix}.Instances"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> DescribeWarmPoolAnswer:
    out: DescribeWarmPoolAnswer = {}  # type: ignore[typeddict-item]
    child_warm_pool_configuration = el.find("WarmPoolConfiguration")
    if child_warm_pool_configuration is not None:
        import aws_sdk_auto_scaling.types.warm_pool_configuration

        out["warm_pool_configuration"] = (
            aws_sdk_auto_scaling.types.warm_pool_configuration.deserialize_query(
                child_warm_pool_configuration
            )
        )
    child_instances = el.find("Instances")
    if child_instances is not None:
        import aws_sdk_auto_scaling.types.instances

        out["instances"] = aws_sdk_auto_scaling.types.instances.deserialize_query(
            child_instances
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
