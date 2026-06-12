"""Generated from Smithy shape ``com.amazonaws.wellarchitected#CreateLensShareInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.client_request_token
    import aws_sdk_wellarchitected.types.lens_alias
    import aws_sdk_wellarchitected.types.shared_with


class CreateLensShareInput(TypedDict):
    lens_alias: "aws_sdk_wellarchitected.types.lens_alias.LensAlias"
    shared_with: NotRequired["aws_sdk_wellarchitected.types.shared_with.SharedWith"]
    client_request_token: NotRequired[
        "aws_sdk_wellarchitected.types.client_request_token.ClientRequestToken"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: CreateLensShareInput) -> dict:
    out: dict = {}
    if "shared_with" in value:
        out["SharedWith"] = value["shared_with"]
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    return out


def deserialize_json(data: dict) -> CreateLensShareInput:
    out: CreateLensShareInput = {}  # type: ignore[typeddict-item]
    if "SharedWith" in data:
        out["shared_with"] = data["SharedWith"]
    if "ClientRequestToken" in data:
        out["client_request_token"] = data["ClientRequestToken"]
    return out
