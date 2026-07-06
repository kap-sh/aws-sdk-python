"""Generated from Smithy shape ``com.amazonaws.sns#ListPhoneNumbersOptedOutInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_sns._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_sns.types.string


class ListPhoneNumbersOptedOutInput(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_sns.types.string.String"]
    """<p>A <code>NextToken</code> string is used when you call the <code>ListPhoneNumbersOptedOut</code> action to retrieve additional records that are available after the first page of results.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListPhoneNumbersOptedOutInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "next_token" in value:
        pairs.append((f"{prefix}.nextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> ListPhoneNumbersOptedOutInput:
    out: ListPhoneNumbersOptedOutInput = {}  # type: ignore[typeddict-item]
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
