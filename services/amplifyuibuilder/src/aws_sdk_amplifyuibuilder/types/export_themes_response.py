"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#ExportThemesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_amplifyuibuilder.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_amplifyuibuilder.types.theme_list


class ExportThemesResponse(TypedDict):
    entities: "aws_sdk_amplifyuibuilder.types.theme_list.ThemeList"
    """<p>Represents the configuration of the exported themes.</p>"""
    next_token: NotRequired["str"]
    """<p>The pagination token that's included if more results are available.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExportThemesResponse) -> dict:
    out: dict = {}
    import aws_sdk_amplifyuibuilder.types.theme_list

    out["entities"] = aws_sdk_amplifyuibuilder.types.theme_list.serialize_json(
        value["entities"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ExportThemesResponse:
    out: ExportThemesResponse = {}  # type: ignore[typeddict-item]
    if "entities" in data:
        import aws_sdk_amplifyuibuilder.types.theme_list

        out["entities"] = aws_sdk_amplifyuibuilder.types.theme_list.deserialize_json(
            data["entities"]
        )
    else:
        raise DeserializationError("ExportThemesResponse.entities required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
