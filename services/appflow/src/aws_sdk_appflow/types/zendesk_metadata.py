"""Generated from Smithy shape ``com.amazonaws.appflow#ZendeskMetadata``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appflow.types.o_auth_scope_list


class ZendeskMetadata(TypedDict):
    o_auth_scopes: NotRequired["aws_sdk_appflow.types.o_auth_scope_list.OAuthScopeList"]
    """<p> The desired authorization scope for the Zendesk account. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ZendeskMetadata) -> dict:
    out: dict = {}
    if "o_auth_scopes" in value:
        import aws_sdk_appflow.types.o_auth_scope_list

        out["oAuthScopes"] = aws_sdk_appflow.types.o_auth_scope_list.serialize_json(
            value["o_auth_scopes"]
        )
    return out


def deserialize_json(data: dict) -> ZendeskMetadata:
    out: ZendeskMetadata = {}  # type: ignore[typeddict-item]
    if "oAuthScopes" in data:
        import aws_sdk_appflow.types.o_auth_scope_list

        out["o_auth_scopes"] = aws_sdk_appflow.types.o_auth_scope_list.deserialize_json(
            data["oAuthScopes"]
        )
    return out
