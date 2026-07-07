"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#DescribeEndPointStateOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elastic_load_balancing._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing.types.instance_states


class DescribeEndPointStateOutput(TypedDict, closed=True):
    instance_states: NotRequired[
        "aws_sdk_elastic_load_balancing.types.instance_states.InstanceStates"
    ]
    """<p>Information about the health of the instances.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeEndPointStateOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "instance_states" in value:
        import aws_sdk_elastic_load_balancing.types.instance_states

        aws_sdk_elastic_load_balancing.types.instance_states.serialize_query(
            value["instance_states"], pairs, f"{prefix}.InstanceStates"
        )


def deserialize_query(el: Element) -> DescribeEndPointStateOutput:
    out: DescribeEndPointStateOutput = {}  # type: ignore[typeddict-item]
    child_instance_states = el.find("InstanceStates")
    if child_instance_states is not None:
        import aws_sdk_elastic_load_balancing.types.instance_states

        out["instance_states"] = (
            aws_sdk_elastic_load_balancing.types.instance_states.deserialize_query(
                child_instance_states
            )
        )
    return out
