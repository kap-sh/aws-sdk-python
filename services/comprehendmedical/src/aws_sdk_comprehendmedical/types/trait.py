"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#Trait``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_comprehendmedical.types.attribute_name
    import aws_sdk_comprehendmedical.types.float


class Trait(TypedDict, closed=True):
    name: NotRequired["aws_sdk_comprehendmedical.types.attribute_name.AttributeName"]
    """<p> Provides a name or contextual description about the trait. </p>"""
    score: NotRequired["aws_sdk_comprehendmedical.types.float.Float"]
    """<p> The level of confidence that Amazon Comprehend Medical has in the accuracy of this trait.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Trait) -> dict:
    out: dict = {}
    if "name" in value:
        import aws_sdk_comprehendmedical.types.attribute_name

        out["Name"] = (
            aws_sdk_comprehendmedical.types.attribute_name.serialize_aws_json_1_1(
                value["name"]
            )
        )
    if "score" in value:
        out["Score"] = value["score"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Trait:
    out: Trait = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        import aws_sdk_comprehendmedical.types.attribute_name

        out["name"] = (
            aws_sdk_comprehendmedical.types.attribute_name.deserialize_aws_json_1_1(
                data["Name"]
            )
        )
    if "Score" in data:
        out["score"] = data["Score"]
    return out
