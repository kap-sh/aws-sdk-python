"""Generated from Smithy shape ``com.amazonaws.mturk#CreateHITResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mturk.types.hit


class CreateHITResponse(TypedDict, closed=True):
    hit: NotRequired["capo_mturk.types.hit.HIT"]
    """<p> Contains the newly created HIT data. For a description of the HIT data structure as it appears in responses, see the HIT Data Structure documentation. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateHITResponse) -> dict:
    out: dict = {}
    if "hit" in value:
        import capo_mturk.types.hit

        out["HIT"] = capo_mturk.types.hit.serialize_aws_json_1_1(value["hit"])
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateHITResponse:
    out: CreateHITResponse = {}  # type: ignore[typeddict-item]
    if "HIT" in data:
        import capo_mturk.types.hit

        out["hit"] = capo_mturk.types.hit.deserialize_aws_json_1_1(data["HIT"])
    return out
