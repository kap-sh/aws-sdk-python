"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ImportLensInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.client_request_token
    import aws_sdk_wellarchitected.types.lens_alias
    import aws_sdk_wellarchitected.types.lens_json
    import aws_sdk_wellarchitected.types.tag_map


class ImportLensInput(TypedDict):
    lens_alias: NotRequired["aws_sdk_wellarchitected.types.lens_alias.LensAlias"]
    json_string: NotRequired["aws_sdk_wellarchitected.types.lens_json.LensJSON"]
    """<p>The JSON representation of a lens.</p>"""
    client_request_token: NotRequired[
        "aws_sdk_wellarchitected.types.client_request_token.ClientRequestToken"
    ]
    tags: NotRequired["aws_sdk_wellarchitected.types.tag_map.TagMap"]
    """<p>Tags to associate to a lens.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImportLensInput) -> dict:
    out: dict = {}
    if "lens_alias" in value:
        out["LensAlias"] = value["lens_alias"]
    if "json_string" in value:
        out["JSONString"] = value["json_string"]
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    if "tags" in value:
        import aws_sdk_wellarchitected.types.tag_map

        out["Tags"] = aws_sdk_wellarchitected.types.tag_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> ImportLensInput:
    out: ImportLensInput = {}  # type: ignore[typeddict-item]
    if "LensAlias" in data:
        out["lens_alias"] = data["LensAlias"]
    if "JSONString" in data:
        out["json_string"] = data["JSONString"]
    if "ClientRequestToken" in data:
        out["client_request_token"] = data["ClientRequestToken"]
    if "Tags" in data:
        import aws_sdk_wellarchitected.types.tag_map

        out["tags"] = aws_sdk_wellarchitected.types.tag_map.deserialize_json(
            data["Tags"]
        )
    return out
