"""Generated from Smithy shape ``com.amazonaws.cloudformation#ListImportsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.export_name
    import capo_cloudformation.types.next_token


class ListImportsInput(TypedDict, closed=True):
    export_name: NotRequired["capo_cloudformation.types.export_name.ExportName"]
    """<p>The name of the exported output value. CloudFormation returns the stack names that are importing this value.</p>"""
    next_token: NotRequired["capo_cloudformation.types.next_token.NextToken"]
    """<p>The token for the next set of items to return. (You received this token from a previous call.)</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListImportsInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "export_name" in value:
        pairs.append((f"{prefix}.ExportName", str(value["export_name"])))
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> ListImportsInput:
    out: ListImportsInput = {}  # type: ignore[typeddict-item]
    child_export_name = el.find("ExportName")
    if child_export_name is not None:
        out["export_name"] = str(child_export_name.text or "")
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
