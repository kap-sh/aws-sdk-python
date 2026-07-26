"""Generated from Smithy shape ``com.amazonaws.cloudfront#ListFunctionsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.function_list


class ListFunctionsResult(TypedDict, closed=True):
    function_list: NotRequired["capo_cloudfront.types.function_list.FunctionList"]
    """<p>A list of CloudFront functions.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: ListFunctionsResult, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "function_list" in value:
        import capo_cloudfront.types.function_list

        capo_cloudfront.types.function_list.serialize_xml(
            value["function_list"], el, "FunctionList"
        )


def deserialize_xml(el: Element) -> ListFunctionsResult:
    out: ListFunctionsResult = {}  # type: ignore[typeddict-item]
    child_function_list = el.find("FunctionList")
    if child_function_list is not None:
        import capo_cloudfront.types.function_list

        out["function_list"] = capo_cloudfront.types.function_list.deserialize_xml(
            child_function_list
        )
    return out
