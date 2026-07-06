"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#AddTagsOutput``."""

from typing_extensions import TypedDict

from aws_sdk_elastic_load_balancing._protocol.xml import Element


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
