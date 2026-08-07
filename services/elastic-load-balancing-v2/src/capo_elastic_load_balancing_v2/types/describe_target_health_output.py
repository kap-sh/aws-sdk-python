"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#DescribeTargetHealthOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing_v2.types.target_health_descriptions


class DescribeTargetHealthOutput(TypedDict, closed=True):
    target_health_descriptions: NotRequired[
        "capo_elastic_load_balancing_v2.types.target_health_descriptions.TargetHealthDescriptions"
    ]
    """<p>Information about the health of the targets.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeTargetHealthOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "target_health_descriptions" in value:
        import capo_elastic_load_balancing_v2.types.target_health_descriptions

        capo_elastic_load_balancing_v2.types.target_health_descriptions.serialize_query(
            value["target_health_descriptions"],
            pairs,
            f"{key_prefix}TargetHealthDescriptions",
        )


def deserialize_query(el: Element) -> DescribeTargetHealthOutput:
    out: DescribeTargetHealthOutput = {}  # type: ignore[typeddict-item]
    child_target_health_descriptions = el.find("TargetHealthDescriptions")
    if child_target_health_descriptions is not None:
        import capo_elastic_load_balancing_v2.types.target_health_descriptions

        out["target_health_descriptions"] = (
            capo_elastic_load_balancing_v2.types.target_health_descriptions.deserialize_query(
                child_target_health_descriptions
            )
        )
    return out
