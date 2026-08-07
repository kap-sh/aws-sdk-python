"""Generated from Smithy shape ``com.amazonaws.cloudformation#ListImportsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.imports
    import capo_cloudformation.types.next_token


class ListImportsOutput(TypedDict, closed=True):
    imports: NotRequired["capo_cloudformation.types.imports.Imports"]
    """<p>A list of stack names that are importing the specified exported output value.</p>"""
    next_token: NotRequired["capo_cloudformation.types.next_token.NextToken"]
    """<p>A string that identifies the next page of exports. If there is no additional page, this value is null.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListImportsOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "imports" in value:
        import capo_cloudformation.types.imports

        capo_cloudformation.types.imports.serialize_query(
            value["imports"], pairs, f"{key_prefix}Imports"
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> ListImportsOutput:
    out: ListImportsOutput = {}  # type: ignore[typeddict-item]
    child_imports = el.find("Imports")
    if child_imports is not None:
        import capo_cloudformation.types.imports

        out["imports"] = capo_cloudformation.types.imports.deserialize_query(
            child_imports
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
