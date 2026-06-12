"""Generated from Smithy shape ``com.amazonaws.synthetics#DescribeCanariesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_synthetics.types.canaries
    import aws_sdk_synthetics.types.token


class DescribeCanariesResponse(TypedDict):
    canaries: NotRequired["aws_sdk_synthetics.types.canaries.Canaries"]
    """<p>Returns an array. Each item in the array contains the full information about one canary.</p>"""
    next_token: NotRequired["aws_sdk_synthetics.types.token.Token"]
    """<p>A token that indicates that there is more data available. You can use this token in a subsequent <code>DescribeCanaries</code> operation to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeCanariesResponse) -> dict:
    out: dict = {}
    if "canaries" in value:
        import aws_sdk_synthetics.types.canaries

        out["Canaries"] = aws_sdk_synthetics.types.canaries.serialize_json(
            value["canaries"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> DescribeCanariesResponse:
    out: DescribeCanariesResponse = {}  # type: ignore[typeddict-item]
    if "Canaries" in data:
        import aws_sdk_synthetics.types.canaries

        out["canaries"] = aws_sdk_synthetics.types.canaries.deserialize_json(
            data["Canaries"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
