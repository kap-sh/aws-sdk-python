"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#DescribeTagsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing_v2.types.resource_arns


class DescribeTagsInput(TypedDict):
    resource_arns: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.resource_arns.ResourceArns"
    ]
    """<p>The Amazon Resource Names (ARN) of the resources. You can specify up to 20 resources in a single call.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeTagsInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "resource_arns" in value:
        import aws_sdk_elastic_load_balancing_v2.types.resource_arns

        aws_sdk_elastic_load_balancing_v2.types.resource_arns.serialize_query(
            value["resource_arns"], pairs, f"{prefix}.ResourceArns"
        )


def deserialize_query(el: Element) -> DescribeTagsInput:
    out: DescribeTagsInput = {}  # type: ignore[typeddict-item]
    child_resource_arns = el.find("ResourceArns")
    if child_resource_arns is not None:
        import aws_sdk_elastic_load_balancing_v2.types.resource_arns

        out["resource_arns"] = (
            aws_sdk_elastic_load_balancing_v2.types.resource_arns.deserialize_query(
                child_resource_arns
            )
        )
    return out
