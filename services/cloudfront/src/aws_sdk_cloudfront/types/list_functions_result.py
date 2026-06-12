"""Generated from Smithy shape ``com.amazonaws.cloudfront#ListFunctionsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.function_list


class ListFunctionsResult(TypedDict):
    function_list: NotRequired["aws_sdk_cloudfront.types.function_list.FunctionList"]
    """<p>A list of CloudFront functions.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: ListFunctionsResult, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "function_list" in value:
        import aws_sdk_cloudfront.types.function_list

        aws_sdk_cloudfront.types.function_list.serialize_xml(
            value["function_list"], el, "FunctionList"
        )


def deserialize_xml(el: Element) -> ListFunctionsResult:
    out: ListFunctionsResult = {}  # type: ignore[typeddict-item]
    child_function_list = el.find("FunctionList")
    if child_function_list is not None:
        import aws_sdk_cloudfront.types.function_list

        out["function_list"] = aws_sdk_cloudfront.types.function_list.deserialize_xml(
            child_function_list
        )
    return out
