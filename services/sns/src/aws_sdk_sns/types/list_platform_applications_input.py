"""Generated from Smithy shape ``com.amazonaws.sns#ListPlatformApplicationsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_sns._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_sns.types.string


class ListPlatformApplicationsInput(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_sns.types.string.String"]
    """<p> <code>NextToken</code> string is used when calling <code>ListPlatformApplications</code> action to retrieve additional records that are available after the first page results.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListPlatformApplicationsInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> ListPlatformApplicationsInput:
    out: ListPlatformApplicationsInput = {}  # type: ignore[typeddict-item]
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
