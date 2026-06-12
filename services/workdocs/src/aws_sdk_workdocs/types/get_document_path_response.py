"""Generated from Smithy shape ``com.amazonaws.workdocs#GetDocumentPathResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workdocs.types.resource_path


class GetDocumentPathResponse(TypedDict):
    path: NotRequired["aws_sdk_workdocs.types.resource_path.ResourcePath"]
    """<p>The path information.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDocumentPathResponse) -> dict:
    out: dict = {}
    if "path" in value:
        import aws_sdk_workdocs.types.resource_path

        out["Path"] = aws_sdk_workdocs.types.resource_path.serialize_json(value["path"])
    return out


def deserialize_json(data: dict) -> GetDocumentPathResponse:
    out: GetDocumentPathResponse = {}  # type: ignore[typeddict-item]
    if "Path" in data:
        import aws_sdk_workdocs.types.resource_path

        out["path"] = aws_sdk_workdocs.types.resource_path.deserialize_json(
            data["Path"]
        )
    return out
