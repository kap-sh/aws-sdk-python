"""Generated from Smithy shape ``com.amazonaws.ses#ListTemplatesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ses._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ses.types.max_items
    import aws_sdk_ses.types.next_token


class ListTemplatesRequest(TypedDict):
    next_token: NotRequired["aws_sdk_ses.types.next_token.NextToken"]
    """<p>A token returned from a previous call to <code>ListTemplates</code> to indicate the position in the list of email templates.</p>"""
    max_items: NotRequired["aws_sdk_ses.types.max_items.MaxItems"]
    """<p>The maximum number of templates to return. This value must be at least 1 and less than or equal to 100. If more than 100 items are requested, the page size will automatically set to 100. If you do not specify a value, 10 is the default page size. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListTemplatesRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))
    if "max_items" in value:
        pairs.append((f"{prefix}.MaxItems", str(value["max_items"])))


def deserialize_query(el: Element) -> ListTemplatesRequest:
    out: ListTemplatesRequest = {}  # type: ignore[typeddict-item]
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_max_items = el.find("MaxItems")
    if child_max_items is not None:
        out["max_items"] = int(child_max_items.text or "")
    return out
