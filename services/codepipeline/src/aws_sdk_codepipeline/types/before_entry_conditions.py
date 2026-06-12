"""Generated from Smithy shape ``com.amazonaws.codepipeline#BeforeEntryConditions``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_codepipeline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.condition_list


class BeforeEntryConditions(TypedDict):
    conditions: "aws_sdk_codepipeline.types.condition_list.ConditionList"
    """<p>The conditions that are configured as entry conditions.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BeforeEntryConditions) -> dict:
    out: dict = {}
    import aws_sdk_codepipeline.types.condition_list

    out["conditions"] = (
        aws_sdk_codepipeline.types.condition_list.serialize_aws_json_1_1(
            value["conditions"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> BeforeEntryConditions:
    out: BeforeEntryConditions = {}  # type: ignore[typeddict-item]
    if "conditions" in data:
        import aws_sdk_codepipeline.types.condition_list

        out["conditions"] = (
            aws_sdk_codepipeline.types.condition_list.deserialize_aws_json_1_1(
                data["conditions"]
            )
        )
    else:
        raise DeserializationError("BeforeEntryConditions.conditions required")
    return out
