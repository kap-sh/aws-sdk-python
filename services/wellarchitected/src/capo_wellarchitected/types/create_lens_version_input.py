"""Generated from Smithy shape ``com.amazonaws.wellarchitected#CreateLensVersionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.client_request_token
    import capo_wellarchitected.types.is_major_version
    import capo_wellarchitected.types.lens_alias
    import capo_wellarchitected.types.lens_version


class CreateLensVersionInput(TypedDict, closed=True):
    lens_alias: "capo_wellarchitected.types.lens_alias.LensAlias"
    lens_version: NotRequired["capo_wellarchitected.types.lens_version.LensVersion"]
    """<p>The version of the lens being created.</p>"""
    is_major_version: NotRequired[
        "capo_wellarchitected.types.is_major_version.IsMajorVersion"
    ]
    """<p>Set to true if this new major lens version.</p>"""
    client_request_token: NotRequired[
        "capo_wellarchitected.types.client_request_token.ClientRequestToken"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: CreateLensVersionInput) -> dict:
    out: dict = {}
    if "lens_version" in value:
        out["LensVersion"] = value["lens_version"]
    if "is_major_version" in value:
        out["IsMajorVersion"] = value["is_major_version"]
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    return out


def deserialize_json(data: dict) -> CreateLensVersionInput:
    out: CreateLensVersionInput = {}  # type: ignore[typeddict-item]
    if "LensVersion" in data:
        out["lens_version"] = data["LensVersion"]
    if "IsMajorVersion" in data:
        out["is_major_version"] = data["IsMajorVersion"]
    if "ClientRequestToken" in data:
        out["client_request_token"] = data["ClientRequestToken"]
    return out
