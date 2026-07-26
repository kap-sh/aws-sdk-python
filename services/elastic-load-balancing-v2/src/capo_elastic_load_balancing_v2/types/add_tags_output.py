"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#AddTagsOutput``."""

from typing_extensions import TypedDict

from capo_elastic_load_balancing_v2._protocol.xml import Element


class AddTagsOutput(TypedDict, closed=True):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: AddTagsOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> AddTagsOutput:
    out: AddTagsOutput = {}  # type: ignore[typeddict-item]
    return out
