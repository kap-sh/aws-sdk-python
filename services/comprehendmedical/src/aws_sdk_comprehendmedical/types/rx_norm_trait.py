"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#RxNormTrait``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_comprehendmedical.types.float
    import aws_sdk_comprehendmedical.types.rx_norm_trait_name


class RxNormTrait(TypedDict):
    name: NotRequired[
        "aws_sdk_comprehendmedical.types.rx_norm_trait_name.RxNormTraitName"
    ]
    """<p>Provides a name or contextual description about the trait.</p>"""
    score: NotRequired["aws_sdk_comprehendmedical.types.float.Float"]
    """<p>The level of confidence that Amazon Comprehend Medical has in the accuracy of the detected trait.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RxNormTrait) -> dict:
    out: dict = {}
    if "name" in value:
        import aws_sdk_comprehendmedical.types.rx_norm_trait_name

        out["Name"] = (
            aws_sdk_comprehendmedical.types.rx_norm_trait_name.serialize_aws_json_1_1(
                value["name"]
            )
        )
    if "score" in value:
        out["Score"] = value["score"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RxNormTrait:
    out: RxNormTrait = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        import aws_sdk_comprehendmedical.types.rx_norm_trait_name

        out["name"] = (
            aws_sdk_comprehendmedical.types.rx_norm_trait_name.deserialize_aws_json_1_1(
                data["Name"]
            )
        )
    if "Score" in data:
        out["score"] = data["Score"]
    return out
