"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#ListAccessTokensOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_route53globalresolver.types.access_tokens


class ListAccessTokensOutput(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """<p>A pagination token used for large sets of results that can't be returned in a single response. Provide this token in the next call to get the results not returned in this call.</p>"""
    access_tokens: NotRequired[
        "aws_sdk_route53globalresolver.types.access_tokens.AccessTokens"
    ]
    """<p>List of the tokens.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAccessTokensOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "access_tokens" in value:
        import aws_sdk_route53globalresolver.types.access_tokens

        out["accessTokens"] = (
            aws_sdk_route53globalresolver.types.access_tokens.serialize_json(
                value["access_tokens"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListAccessTokensOutput:
    out: ListAccessTokensOutput = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "accessTokens" in data:
        import aws_sdk_route53globalresolver.types.access_tokens

        out["access_tokens"] = (
            aws_sdk_route53globalresolver.types.access_tokens.deserialize_json(
                data["accessTokens"]
            )
        )
    return out
