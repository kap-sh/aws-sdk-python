"""Generated from Smithy shape ``com.amazonaws.inspector2#SearchVulnerabilitiesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.next_token
    import aws_sdk_inspector2.types.vulnerabilities


class SearchVulnerabilitiesResponse(TypedDict, closed=True):
    vulnerabilities: "aws_sdk_inspector2.types.vulnerabilities.Vulnerabilities"
    """<p>Details about the listed vulnerability.</p>"""
    next_token: NotRequired["aws_sdk_inspector2.types.next_token.NextToken"]
    """<p>The pagination parameter to be used on the next list operation to retrieve more items.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchVulnerabilitiesResponse) -> dict:
    out: dict = {}
    import aws_sdk_inspector2.types.vulnerabilities

    out["vulnerabilities"] = aws_sdk_inspector2.types.vulnerabilities.serialize_json(
        value["vulnerabilities"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> SearchVulnerabilitiesResponse:
    out: SearchVulnerabilitiesResponse = {}  # type: ignore[typeddict-item]
    if "vulnerabilities" in data:
        import aws_sdk_inspector2.types.vulnerabilities

        out["vulnerabilities"] = (
            aws_sdk_inspector2.types.vulnerabilities.deserialize_json(
                data["vulnerabilities"]
            )
        )
    else:
        raise DeserializationError(
            "SearchVulnerabilitiesResponse.vulnerabilities required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
