"""Generated from Smithy shape ``com.amazonaws.cloudfront#ListConflictingAliasesResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.conflicting_aliases_list


class ListConflictingAliasesResult(TypedDict):
    conflicting_aliases_list: NotRequired[
        "aws_sdk_cloudfront.types.conflicting_aliases_list.ConflictingAliasesList"
    ]
    """<p>A list of conflicting aliases.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ListConflictingAliasesResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "conflicting_aliases_list" in value:
        import aws_sdk_cloudfront.types.conflicting_aliases_list

        aws_sdk_cloudfront.types.conflicting_aliases_list.serialize_xml(
            value["conflicting_aliases_list"], el, "ConflictingAliasesList"
        )


def deserialize_xml(el: Element) -> ListConflictingAliasesResult:
    out: ListConflictingAliasesResult = {}  # type: ignore[typeddict-item]
    child_conflicting_aliases_list = el.find("ConflictingAliasesList")
    if child_conflicting_aliases_list is not None:
        import aws_sdk_cloudfront.types.conflicting_aliases_list

        out["conflicting_aliases_list"] = (
            aws_sdk_cloudfront.types.conflicting_aliases_list.deserialize_xml(
                child_conflicting_aliases_list
            )
        )
    return out
