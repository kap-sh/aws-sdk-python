"""Generated from Smithy shape ``com.amazonaws.ses#ListCustomVerificationEmailTemplatesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ses._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ses.types.max_results
    import aws_sdk_ses.types.next_token


class ListCustomVerificationEmailTemplatesRequest(TypedDict):
    next_token: NotRequired["aws_sdk_ses.types.next_token.NextToken"]
    """<p>An array the contains the name and creation time stamp for each template in your Amazon SES account.</p>"""
    max_results: NotRequired["aws_sdk_ses.types.max_results.MaxResults"]
    """<p>The maximum number of custom verification email templates to return. This value must be at least 1 and less than or equal to 50. If you do not specify a value, or if you specify a value less than 1 or greater than 50, the operation returns up to 50 results.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListCustomVerificationEmailTemplatesRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))
    if "max_results" in value:
        pairs.append((f"{prefix}.MaxResults", str(value["max_results"])))


def deserialize_query(el: Element) -> ListCustomVerificationEmailTemplatesRequest:
    out: ListCustomVerificationEmailTemplatesRequest = {}  # type: ignore[typeddict-item]
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    return out
