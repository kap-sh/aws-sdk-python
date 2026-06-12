"""Generated from Smithy shape ``com.amazonaws.mpa#ListIdentitySourcesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mpa.types.identity_sources
    import aws_sdk_mpa.types.token


class ListIdentitySourcesResponse(TypedDict):
    next_token: NotRequired["aws_sdk_mpa.types.token.Token"]
    """<p>If present, indicates that more output is available than is included in the current response. Use this value in the <code>NextToken</code> request parameter in a next call to the operation to get more output. You can repeat this until the <code>NextToken</code> response element returns <code>null</code>.</p>"""
    identity_sources: NotRequired["aws_sdk_mpa.types.identity_sources.IdentitySources"]
    """<p>A <code>IdentitySources</code>. Contains details for identity sources.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListIdentitySourcesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "identity_sources" in value:
        import aws_sdk_mpa.types.identity_sources

        out["IdentitySources"] = aws_sdk_mpa.types.identity_sources.serialize_json(
            value["identity_sources"]
        )
    return out


def deserialize_json(data: dict) -> ListIdentitySourcesResponse:
    out: ListIdentitySourcesResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "IdentitySources" in data:
        import aws_sdk_mpa.types.identity_sources

        out["identity_sources"] = aws_sdk_mpa.types.identity_sources.deserialize_json(
            data["IdentitySources"]
        )
    return out
