"""Generated from Smithy shape ``com.amazonaws.medicalimaging#SearchImageSetsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_medical_imaging.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_medical_imaging.types.image_sets_metadata_summaries
    import aws_sdk_medical_imaging.types.next_token
    import aws_sdk_medical_imaging.types.sort


class SearchImageSetsResponse(TypedDict, closed=True):
    image_sets_metadata_summaries: "aws_sdk_medical_imaging.types.image_sets_metadata_summaries.ImageSetsMetadataSummaries"
    """<p>The model containing the image set results.</p>"""
    sort: NotRequired["aws_sdk_medical_imaging.types.sort.Sort"]
    """<p>The sort order for image set search results.</p>"""
    next_token: NotRequired["aws_sdk_medical_imaging.types.next_token.NextToken"]
    """<p>The token for pagination results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchImageSetsResponse) -> dict:
    out: dict = {}
    import aws_sdk_medical_imaging.types.image_sets_metadata_summaries

    out["imageSetsMetadataSummaries"] = (
        aws_sdk_medical_imaging.types.image_sets_metadata_summaries.serialize_json(
            value["image_sets_metadata_summaries"]
        )
    )
    if "sort" in value:
        import aws_sdk_medical_imaging.types.sort

        out["sort"] = aws_sdk_medical_imaging.types.sort.serialize_json(value["sort"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> SearchImageSetsResponse:
    out: SearchImageSetsResponse = {}  # type: ignore[typeddict-item]
    if "imageSetsMetadataSummaries" in data:
        import aws_sdk_medical_imaging.types.image_sets_metadata_summaries

        out["image_sets_metadata_summaries"] = (
            aws_sdk_medical_imaging.types.image_sets_metadata_summaries.deserialize_json(
                data["imageSetsMetadataSummaries"]
            )
        )
    else:
        raise DeserializationError(
            "SearchImageSetsResponse.image_sets_metadata_summaries required"
        )
    if "sort" in data:
        import aws_sdk_medical_imaging.types.sort

        out["sort"] = aws_sdk_medical_imaging.types.sort.deserialize_json(data["sort"])
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
