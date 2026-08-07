"""Generated from Smithy shape ``com.amazonaws.cloudformation#ListExportsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.exports
    import capo_cloudformation.types.next_token


class ListExportsOutput(TypedDict, closed=True):
    exports: NotRequired["capo_cloudformation.types.exports.Exports"]
    """<p>The output for the <a>ListExports</a> action.</p>"""
    next_token: NotRequired["capo_cloudformation.types.next_token.NextToken"]
    """<p>If the output exceeds 100 exported output values, a string that identifies the next page of exports. If there is no additional page, this value is null.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListExportsOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "exports" in value:
        import capo_cloudformation.types.exports

        capo_cloudformation.types.exports.serialize_query(
            value["exports"], pairs, f"{key_prefix}Exports"
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> ListExportsOutput:
    out: ListExportsOutput = {}  # type: ignore[typeddict-item]
    child_exports = el.find("Exports")
    if child_exports is not None:
        import capo_cloudformation.types.exports

        out["exports"] = capo_cloudformation.types.exports.deserialize_query(
            child_exports
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
