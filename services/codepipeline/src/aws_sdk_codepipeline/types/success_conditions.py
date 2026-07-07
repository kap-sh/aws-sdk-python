"""Generated from Smithy shape ``com.amazonaws.codepipeline#SuccessConditions``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_codepipeline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.condition_list


class SuccessConditions(TypedDict, closed=True):
    conditions: "aws_sdk_codepipeline.types.condition_list.ConditionList"
    """<p>The conditions that are success conditions.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SuccessConditions) -> dict:
    out: dict = {}
    import aws_sdk_codepipeline.types.condition_list

    out["conditions"] = (
        aws_sdk_codepipeline.types.condition_list.serialize_aws_json_1_1(
            value["conditions"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> SuccessConditions:
    out: SuccessConditions = {}  # type: ignore[typeddict-item]
    if "conditions" in data:
        import aws_sdk_codepipeline.types.condition_list

        out["conditions"] = (
            aws_sdk_codepipeline.types.condition_list.deserialize_aws_json_1_1(
                data["conditions"]
            )
        )
    else:
        raise DeserializationError("SuccessConditions.conditions required")
    return out
