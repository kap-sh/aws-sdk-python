"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#RemoveTagsOutput``."""

from typing import TypedDict

from aws_sdk_elastic_load_balancing._protocol.xml import Element


class RemoveTagsOutput(TypedDict):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: RemoveTagsOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> RemoveTagsOutput:
    out: RemoveTagsOutput = {}  # type: ignore[typeddict-item]
    return out
