"""Generated from Smithy shape ``com.amazonaws.medicalimaging#ListDatastoresResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medical_imaging.types.datastore_summaries
    import aws_sdk_medical_imaging.types.next_token


class ListDatastoresResponse(TypedDict, closed=True):
    datastore_summaries: NotRequired[
        "aws_sdk_medical_imaging.types.datastore_summaries.DatastoreSummaries"
    ]
    """<p>The list of summaries of data stores.</p>"""
    next_token: NotRequired["aws_sdk_medical_imaging.types.next_token.NextToken"]
    """<p>The pagination token used to retrieve the list of data stores on the next page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDatastoresResponse) -> dict:
    out: dict = {}
    if "datastore_summaries" in value:
        import aws_sdk_medical_imaging.types.datastore_summaries

        out["datastoreSummaries"] = (
            aws_sdk_medical_imaging.types.datastore_summaries.serialize_json(
                value["datastore_summaries"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDatastoresResponse:
    out: ListDatastoresResponse = {}  # type: ignore[typeddict-item]
    if "datastoreSummaries" in data:
        import aws_sdk_medical_imaging.types.datastore_summaries

        out["datastore_summaries"] = (
            aws_sdk_medical_imaging.types.datastore_summaries.deserialize_json(
                data["datastoreSummaries"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
