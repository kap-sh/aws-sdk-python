"""Generated from Smithy shape ``com.amazonaws.connect#ListSecurityKeysResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.next_token
    import aws_sdk_connect.types.security_keys_list


class ListSecurityKeysResponse(TypedDict, closed=True):
    security_keys: NotRequired[
        "aws_sdk_connect.types.security_keys_list.SecurityKeysList"
    ]
    """<p>The security keys.</p>"""
    next_token: NotRequired["aws_sdk_connect.types.next_token.NextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSecurityKeysResponse) -> dict:
    out: dict = {}
    if "security_keys" in value:
        import aws_sdk_connect.types.security_keys_list

        out["SecurityKeys"] = aws_sdk_connect.types.security_keys_list.serialize_json(
            value["security_keys"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSecurityKeysResponse:
    out: ListSecurityKeysResponse = {}  # type: ignore[typeddict-item]
    if "SecurityKeys" in data:
        import aws_sdk_connect.types.security_keys_list

        out["security_keys"] = (
            aws_sdk_connect.types.security_keys_list.deserialize_json(
                data["SecurityKeys"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
