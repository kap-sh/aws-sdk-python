"""Generated from Smithy shape ``com.amazonaws.dataexchange#AssetConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dataexchange.types.list_of_tag


class AssetConfiguration(TypedDict):
    tags: NotRequired["aws_sdk_dataexchange.types.list_of_tag.ListOfTag"]
    """<p>The tags to be applied to assets created by the job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetConfiguration) -> dict:
    out: dict = {}
    if "tags" in value:
        import aws_sdk_dataexchange.types.list_of_tag

        out["Tags"] = aws_sdk_dataexchange.types.list_of_tag.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> AssetConfiguration:
    out: AssetConfiguration = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import aws_sdk_dataexchange.types.list_of_tag

        out["tags"] = aws_sdk_dataexchange.types.list_of_tag.deserialize_json(
            data["Tags"]
        )
    return out
