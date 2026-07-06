"""Generated from Smithy shape ``com.amazonaws.cloudformation#DescribeStacksOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.next_token
    import aws_sdk_cloudformation.types.stacks


class DescribeStacksOutput(TypedDict, closed=True):
    stacks: NotRequired["aws_sdk_cloudformation.types.stacks.Stacks"]
    """<p>A list of stack structures.</p>"""
    next_token: NotRequired["aws_sdk_cloudformation.types.next_token.NextToken"]
    """<p>If the output exceeds 1 MB in size, a string that identifies the next page of stacks. If no additional page exists, this value is null.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeStacksOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "stacks" in value:
        import aws_sdk_cloudformation.types.stacks

        aws_sdk_cloudformation.types.stacks.serialize_query(
            value["stacks"], pairs, f"{prefix}.Stacks"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> DescribeStacksOutput:
    out: DescribeStacksOutput = {}  # type: ignore[typeddict-item]
    child_stacks = el.find("Stacks")
    if child_stacks is not None:
        import aws_sdk_cloudformation.types.stacks

        out["stacks"] = aws_sdk_cloudformation.types.stacks.deserialize_query(
            child_stacks
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
