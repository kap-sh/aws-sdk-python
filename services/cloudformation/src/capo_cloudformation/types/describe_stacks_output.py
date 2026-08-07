"""Generated from Smithy shape ``com.amazonaws.cloudformation#DescribeStacksOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.next_token
    import capo_cloudformation.types.stacks


class DescribeStacksOutput(TypedDict, closed=True):
    stacks: NotRequired["capo_cloudformation.types.stacks.Stacks"]
    """<p>A list of stack structures.</p>"""
    next_token: NotRequired["capo_cloudformation.types.next_token.NextToken"]
    """<p>If the output exceeds 1 MB in size, a string that identifies the next page of stacks. If no additional page exists, this value is null.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeStacksOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "stacks" in value:
        import capo_cloudformation.types.stacks

        capo_cloudformation.types.stacks.serialize_query(
            value["stacks"], pairs, f"{key_prefix}Stacks"
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> DescribeStacksOutput:
    out: DescribeStacksOutput = {}  # type: ignore[typeddict-item]
    child_stacks = el.find("Stacks")
    if child_stacks is not None:
        import capo_cloudformation.types.stacks

        out["stacks"] = capo_cloudformation.types.stacks.deserialize_query(child_stacks)
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
