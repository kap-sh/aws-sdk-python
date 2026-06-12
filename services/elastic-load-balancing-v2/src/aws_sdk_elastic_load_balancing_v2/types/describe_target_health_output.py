"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#DescribeTargetHealthOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing_v2.types.target_health_descriptions


class DescribeTargetHealthOutput(TypedDict):
    target_health_descriptions: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.target_health_descriptions.TargetHealthDescriptions"
    ]
    """<p>Information about the health of the targets.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeTargetHealthOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "target_health_descriptions" in value:
        import aws_sdk_elastic_load_balancing_v2.types.target_health_descriptions

        aws_sdk_elastic_load_balancing_v2.types.target_health_descriptions.serialize_query(
            value["target_health_descriptions"],
            pairs,
            f"{prefix}.TargetHealthDescriptions",
        )


def deserialize_query(el: Element) -> DescribeTargetHealthOutput:
    out: DescribeTargetHealthOutput = {}  # type: ignore[typeddict-item]
    child_target_health_descriptions = el.find("TargetHealthDescriptions")
    if child_target_health_descriptions is not None:
        import aws_sdk_elastic_load_balancing_v2.types.target_health_descriptions

        out["target_health_descriptions"] = (
            aws_sdk_elastic_load_balancing_v2.types.target_health_descriptions.deserialize_query(
                child_target_health_descriptions
            )
        )
    return out
