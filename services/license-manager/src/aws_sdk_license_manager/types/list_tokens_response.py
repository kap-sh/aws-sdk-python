"""Generated from Smithy shape ``com.amazonaws.licensemanager#ListTokensResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.string
    import aws_sdk_license_manager.types.token_list


class ListTokensResponse(TypedDict, closed=True):
    tokens: NotRequired["aws_sdk_license_manager.types.token_list.TokenList"]
    """<p>Received token details.</p>"""
    next_token: NotRequired["aws_sdk_license_manager.types.string.String"]
    """<p>Token for the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTokensResponse) -> dict:
    out: dict = {}
    if "tokens" in value:
        import aws_sdk_license_manager.types.token_list

        out["Tokens"] = aws_sdk_license_manager.types.token_list.serialize_aws_json_1_1(
            value["tokens"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTokensResponse:
    out: ListTokensResponse = {}  # type: ignore[typeddict-item]
    if "Tokens" in data:
        import aws_sdk_license_manager.types.token_list

        out["tokens"] = (
            aws_sdk_license_manager.types.token_list.deserialize_aws_json_1_1(
                data["Tokens"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
