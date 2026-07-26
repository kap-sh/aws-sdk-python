"""Generated from Smithy shape ``com.amazonaws.wellarchitected#DeleteLensShareInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.client_request_token
    import capo_wellarchitected.types.lens_alias
    import capo_wellarchitected.types.share_id


class DeleteLensShareInput(TypedDict, closed=True):
    share_id: "capo_wellarchitected.types.share_id.ShareId"
    lens_alias: "capo_wellarchitected.types.lens_alias.LensAlias"
    client_request_token: NotRequired[
        "capo_wellarchitected.types.client_request_token.ClientRequestToken"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: DeleteLensShareInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteLensShareInput:
    out: DeleteLensShareInput = {}  # type: ignore[typeddict-item]
    return out
