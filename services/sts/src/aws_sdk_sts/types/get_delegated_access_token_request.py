"""Generated from Smithy shape ``com.amazonaws.sts#GetDelegatedAccessTokenRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_sts._protocol.xml import Element
from aws_sdk_sts.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sts.types.trade_in_token_type


class GetDelegatedAccessTokenRequest(TypedDict, closed=True):
    trade_in_token: "aws_sdk_sts.types.trade_in_token_type.tradeInTokenType"
    """<p>The token to exchange for temporary Amazon Web Services credentials. This token must be valid and unexpired at the time of the request.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetDelegatedAccessTokenRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.TradeInToken", str(value["trade_in_token"])))


def deserialize_query(el: Element) -> GetDelegatedAccessTokenRequest:
    out: GetDelegatedAccessTokenRequest = {}  # type: ignore[typeddict-item]
    child_trade_in_token = el.find("TradeInToken")
    if child_trade_in_token is not None:
        out["trade_in_token"] = str(child_trade_in_token.text or "")
    else:
        raise DeserializationError(
            "GetDelegatedAccessTokenRequest.trade_in_token required"
        )
    return out
