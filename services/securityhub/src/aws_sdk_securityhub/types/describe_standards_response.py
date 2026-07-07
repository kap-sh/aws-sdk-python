"""Generated from Smithy shape ``com.amazonaws.securityhub#DescribeStandardsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.next_token
    import aws_sdk_securityhub.types.standards


class DescribeStandardsResponse(TypedDict, closed=True):
    standards: NotRequired["aws_sdk_securityhub.types.standards.Standards"]
    """<p>A list of available standards.</p>"""
    next_token: NotRequired["aws_sdk_securityhub.types.next_token.NextToken"]
    """<p>The pagination token to use to request the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeStandardsResponse) -> dict:
    out: dict = {}
    if "standards" in value:
        import aws_sdk_securityhub.types.standards

        out["Standards"] = aws_sdk_securityhub.types.standards.serialize_json(
            value["standards"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> DescribeStandardsResponse:
    out: DescribeStandardsResponse = {}  # type: ignore[typeddict-item]
    if "Standards" in data:
        import aws_sdk_securityhub.types.standards

        out["standards"] = aws_sdk_securityhub.types.standards.deserialize_json(
            data["Standards"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
