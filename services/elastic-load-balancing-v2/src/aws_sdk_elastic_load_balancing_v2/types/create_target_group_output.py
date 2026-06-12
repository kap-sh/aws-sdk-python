"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#CreateTargetGroupOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing_v2.types.target_groups


class CreateTargetGroupOutput(TypedDict):
    target_groups: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.target_groups.TargetGroups"
    ]
    """<p>Information about the target group.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateTargetGroupOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "target_groups" in value:
        import aws_sdk_elastic_load_balancing_v2.types.target_groups

        aws_sdk_elastic_load_balancing_v2.types.target_groups.serialize_query(
            value["target_groups"], pairs, f"{prefix}.TargetGroups"
        )


def deserialize_query(el: Element) -> CreateTargetGroupOutput:
    out: CreateTargetGroupOutput = {}  # type: ignore[typeddict-item]
    child_target_groups = el.find("TargetGroups")
    if child_target_groups is not None:
        import aws_sdk_elastic_load_balancing_v2.types.target_groups

        out["target_groups"] = (
            aws_sdk_elastic_load_balancing_v2.types.target_groups.deserialize_query(
                child_target_groups
            )
        )
    return out
