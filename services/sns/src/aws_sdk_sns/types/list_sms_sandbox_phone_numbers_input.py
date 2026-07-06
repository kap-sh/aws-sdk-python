"""Generated from Smithy shape ``com.amazonaws.sns#ListSMSSandboxPhoneNumbersInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_sns._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_sns.types.max_items
    import aws_sdk_sns.types.next_token


class ListSMSSandboxPhoneNumbersInput(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_sns.types.next_token.nextToken"]
    """<p>Token that the previous <code>ListSMSSandboxPhoneNumbersInput</code> request returns.</p>"""
    max_results: NotRequired["aws_sdk_sns.types.max_items.MaxItems"]
    """<p>The maximum number of phone numbers to return.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListSMSSandboxPhoneNumbersInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))
    if "max_results" in value:
        pairs.append((f"{prefix}.MaxResults", str(value["max_results"])))


def deserialize_query(el: Element) -> ListSMSSandboxPhoneNumbersInput:
    out: ListSMSSandboxPhoneNumbersInput = {}  # type: ignore[typeddict-item]
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    return out
