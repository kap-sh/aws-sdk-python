"""Generated from Smithy shape ``com.amazonaws.workspacesweb#ListIdentityProvidersResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.identity_provider_list
    import aws_sdk_workspaces_web.types.pagination_token


class ListIdentityProvidersResponse(TypedDict):
    next_token: NotRequired[
        "aws_sdk_workspaces_web.types.pagination_token.PaginationToken"
    ]
    """<p>The pagination token used to retrieve the next page of results for this operation.</p>"""
    identity_providers: NotRequired[
        "aws_sdk_workspaces_web.types.identity_provider_list.IdentityProviderList"
    ]
    """<p>The identity providers.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListIdentityProvidersResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "identity_providers" in value:
        import aws_sdk_workspaces_web.types.identity_provider_list

        out["identityProviders"] = (
            aws_sdk_workspaces_web.types.identity_provider_list.serialize_json(
                value["identity_providers"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListIdentityProvidersResponse:
    out: ListIdentityProvidersResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "identityProviders" in data:
        import aws_sdk_workspaces_web.types.identity_provider_list

        out["identity_providers"] = (
            aws_sdk_workspaces_web.types.identity_provider_list.deserialize_json(
                data["identityProviders"]
            )
        )
    return out
