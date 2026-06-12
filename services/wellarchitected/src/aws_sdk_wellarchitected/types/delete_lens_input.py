"""Generated from Smithy shape ``com.amazonaws.wellarchitected#DeleteLensInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.client_request_token
    import aws_sdk_wellarchitected.types.lens_alias
    import aws_sdk_wellarchitected.types.lens_status_type


class DeleteLensInput(TypedDict):
    lens_alias: "aws_sdk_wellarchitected.types.lens_alias.LensAlias"
    client_request_token: NotRequired[
        "aws_sdk_wellarchitected.types.client_request_token.ClientRequestToken"
    ]
    lens_status: NotRequired[
        "aws_sdk_wellarchitected.types.lens_status_type.LensStatusType"
    ]
    """<p>The status of the lens to be deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteLensInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteLensInput:
    out: DeleteLensInput = {}  # type: ignore[typeddict-item]
    return out
