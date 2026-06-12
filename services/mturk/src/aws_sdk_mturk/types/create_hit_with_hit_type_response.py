"""Generated from Smithy shape ``com.amazonaws.mturk#CreateHITWithHITTypeResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mturk.types.hit


class CreateHITWithHITTypeResponse(TypedDict):
    hit: NotRequired["aws_sdk_mturk.types.hit.HIT"]
    """<p> Contains the newly created HIT data. For a description of the HIT data structure as it appears in responses, see the HIT Data Structure documentation. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateHITWithHITTypeResponse) -> dict:
    out: dict = {}
    if "hit" in value:
        import aws_sdk_mturk.types.hit

        out["HIT"] = aws_sdk_mturk.types.hit.serialize_aws_json_1_1(value["hit"])
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateHITWithHITTypeResponse:
    out: CreateHITWithHITTypeResponse = {}  # type: ignore[typeddict-item]
    if "HIT" in data:
        import aws_sdk_mturk.types.hit

        out["hit"] = aws_sdk_mturk.types.hit.deserialize_aws_json_1_1(data["HIT"])
    return out
