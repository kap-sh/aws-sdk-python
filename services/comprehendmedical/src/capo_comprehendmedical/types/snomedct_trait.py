"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#SNOMEDCTTrait``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehendmedical.types.float
    import capo_comprehendmedical.types.snomedct_trait_name


class SNOMEDCTTrait(TypedDict, closed=True):
    name: NotRequired[
        "capo_comprehendmedical.types.snomedct_trait_name.SNOMEDCTTraitName"
    ]
    """<p> The name or contextual description of a detected trait. </p>"""
    score: NotRequired["capo_comprehendmedical.types.float.Float"]
    """<p> The level of confidence that Amazon Comprehend Medical has in the accuracy of a detected trait. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SNOMEDCTTrait) -> dict:
    out: dict = {}
    if "name" in value:
        import capo_comprehendmedical.types.snomedct_trait_name

        out["Name"] = (
            capo_comprehendmedical.types.snomedct_trait_name.serialize_aws_json_1_1(
                value["name"]
            )
        )
    if "score" in value:
        out["Score"] = value["score"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SNOMEDCTTrait:
    out: SNOMEDCTTrait = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        import capo_comprehendmedical.types.snomedct_trait_name

        out["name"] = (
            capo_comprehendmedical.types.snomedct_trait_name.deserialize_aws_json_1_1(
                data["Name"]
            )
        )
    if "Score" in data:
        out["score"] = data["Score"]
    return out
