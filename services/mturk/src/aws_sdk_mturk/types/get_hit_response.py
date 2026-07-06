"""Generated from Smithy shape ``com.amazonaws.mturk#GetHITResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mturk.types.hit


class GetHITResponse(TypedDict, closed=True):
    hit: NotRequired["aws_sdk_mturk.types.hit.HIT"]
    """<p> Contains the requested HIT data.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetHITResponse) -> dict:
    out: dict = {}
    if "hit" in value:
        import aws_sdk_mturk.types.hit

        out["HIT"] = aws_sdk_mturk.types.hit.serialize_aws_json_1_1(value["hit"])
    return out


def deserialize_aws_json_1_1(data: dict) -> GetHITResponse:
    out: GetHITResponse = {}  # type: ignore[typeddict-item]
    if "HIT" in data:
        import aws_sdk_mturk.types.hit

        out["hit"] = aws_sdk_mturk.types.hit.deserialize_aws_json_1_1(data["HIT"])
    return out
