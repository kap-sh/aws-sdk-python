"""Generated from Smithy shape ``com.amazonaws.cloudtrail#GetTrailResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudtrail.types.trail


class GetTrailResponse(TypedDict, closed=True):
    trail: NotRequired["capo_cloudtrail.types.trail.Trail"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetTrailResponse) -> dict:
    out: dict = {}
    if "trail" in value:
        import capo_cloudtrail.types.trail

        out["Trail"] = capo_cloudtrail.types.trail.serialize_aws_json_1_1(
            value["trail"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetTrailResponse:
    out: GetTrailResponse = {}  # type: ignore[typeddict-item]
    if "Trail" in data:
        import capo_cloudtrail.types.trail

        out["trail"] = capo_cloudtrail.types.trail.deserialize_aws_json_1_1(
            data["Trail"]
        )
    return out
