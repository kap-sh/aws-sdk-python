"""Generated from Smithy shape ``com.amazonaws.medialive#ListSdiSourcesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__list_of_sdi_source_summary
    import aws_sdk_medialive.types.__string


class ListSdiSourcesResponse(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_medialive.types.__string.__string"]
    sdi_sources: NotRequired[
        "aws_sdk_medialive.types.__list_of_sdi_source_summary.__listOfSdiSourceSummary"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: ListSdiSourcesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "sdi_sources" in value:
        import aws_sdk_medialive.types.__list_of_sdi_source_summary

        out["sdiSources"] = (
            aws_sdk_medialive.types.__list_of_sdi_source_summary.serialize_json(
                value["sdi_sources"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListSdiSourcesResponse:
    out: ListSdiSourcesResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "sdiSources" in data:
        import aws_sdk_medialive.types.__list_of_sdi_source_summary

        out["sdi_sources"] = (
            aws_sdk_medialive.types.__list_of_sdi_source_summary.deserialize_json(
                data["sdiSources"]
            )
        )
    return out
