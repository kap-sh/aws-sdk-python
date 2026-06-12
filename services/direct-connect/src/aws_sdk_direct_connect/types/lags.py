"""Generated from Smithy shape ``com.amazonaws.directconnect#Lags``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_direct_connect.types.lag_list
    import aws_sdk_direct_connect.types.pagination_token


class Lags(TypedDict):
    lags: NotRequired["aws_sdk_direct_connect.types.lag_list.LagList"]
    """<p>The LAGs.</p>"""
    next_token: NotRequired[
        "aws_sdk_direct_connect.types.pagination_token.PaginationToken"
    ]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Lags) -> dict:
    out: dict = {}
    if "lags" in value:
        import aws_sdk_direct_connect.types.lag_list

        out["lags"] = aws_sdk_direct_connect.types.lag_list.serialize_aws_json_1_1(
            value["lags"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Lags:
    out: Lags = {}  # type: ignore[typeddict-item]
    if "lags" in data:
        import aws_sdk_direct_connect.types.lag_list

        out["lags"] = aws_sdk_direct_connect.types.lag_list.deserialize_aws_json_1_1(
            data["lags"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
