"""Generated from Smithy shape ``com.amazonaws.cloudformation#ListImportsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.imports
    import aws_sdk_cloudformation.types.next_token


class ListImportsOutput(TypedDict):
    imports: NotRequired["aws_sdk_cloudformation.types.imports.Imports"]
    """<p>A list of stack names that are importing the specified exported output value.</p>"""
    next_token: NotRequired["aws_sdk_cloudformation.types.next_token.NextToken"]
    """<p>A string that identifies the next page of exports. If there is no additional page, this value is null.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListImportsOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "imports" in value:
        import aws_sdk_cloudformation.types.imports

        aws_sdk_cloudformation.types.imports.serialize_query(
            value["imports"], pairs, f"{prefix}.Imports"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> ListImportsOutput:
    out: ListImportsOutput = {}  # type: ignore[typeddict-item]
    child_imports = el.find("Imports")
    if child_imports is not None:
        import aws_sdk_cloudformation.types.imports

        out["imports"] = aws_sdk_cloudformation.types.imports.deserialize_query(
            child_imports
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
