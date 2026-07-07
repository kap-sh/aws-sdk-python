"""Generated from Smithy shape ``com.amazonaws.cloudformation#ListExportsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.exports
    import aws_sdk_cloudformation.types.next_token


class ListExportsOutput(TypedDict, closed=True):
    exports: NotRequired["aws_sdk_cloudformation.types.exports.Exports"]
    """<p>The output for the <a>ListExports</a> action.</p>"""
    next_token: NotRequired["aws_sdk_cloudformation.types.next_token.NextToken"]
    """<p>If the output exceeds 100 exported output values, a string that identifies the next page of exports. If there is no additional page, this value is null.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListExportsOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "exports" in value:
        import aws_sdk_cloudformation.types.exports

        aws_sdk_cloudformation.types.exports.serialize_query(
            value["exports"], pairs, f"{prefix}.Exports"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> ListExportsOutput:
    out: ListExportsOutput = {}  # type: ignore[typeddict-item]
    child_exports = el.find("Exports")
    if child_exports is not None:
        import aws_sdk_cloudformation.types.exports

        out["exports"] = aws_sdk_cloudformation.types.exports.deserialize_query(
            child_exports
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
