"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#ExportComponentsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_amplifyuibuilder.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_amplifyuibuilder.types.component_list


class ExportComponentsResponse(TypedDict, closed=True):
    entities: "aws_sdk_amplifyuibuilder.types.component_list.ComponentList"
    """<p>Represents the configuration of the exported components.</p>"""
    next_token: NotRequired["str"]
    """<p>The pagination token that's included if more results are available.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExportComponentsResponse) -> dict:
    out: dict = {}
    import aws_sdk_amplifyuibuilder.types.component_list

    out["entities"] = aws_sdk_amplifyuibuilder.types.component_list.serialize_json(
        value["entities"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ExportComponentsResponse:
    out: ExportComponentsResponse = {}  # type: ignore[typeddict-item]
    if "entities" in data:
        import aws_sdk_amplifyuibuilder.types.component_list

        out["entities"] = (
            aws_sdk_amplifyuibuilder.types.component_list.deserialize_json(
                data["entities"]
            )
        )
    else:
        raise DeserializationError("ExportComponentsResponse.entities required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
