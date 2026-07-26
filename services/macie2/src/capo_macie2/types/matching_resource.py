"""Generated from Smithy shape ``com.amazonaws.macie2#MatchingResource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_macie2.types.matching_bucket


class MatchingResource(TypedDict, closed=True):
    matching_bucket: NotRequired["capo_macie2.types.matching_bucket.MatchingBucket"]
    """<p>The details of an S3 bucket that Amazon Macie monitors and analyzes for your account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MatchingResource) -> dict:
    out: dict = {}
    if "matching_bucket" in value:
        import capo_macie2.types.matching_bucket

        out["matchingBucket"] = capo_macie2.types.matching_bucket.serialize_json(
            value["matching_bucket"]
        )
    return out


def deserialize_json(data: dict) -> MatchingResource:
    out: MatchingResource = {}  # type: ignore[typeddict-item]
    if "matchingBucket" in data:
        import capo_macie2.types.matching_bucket

        out["matching_bucket"] = capo_macie2.types.matching_bucket.deserialize_json(
            data["matchingBucket"]
        )
    return out
