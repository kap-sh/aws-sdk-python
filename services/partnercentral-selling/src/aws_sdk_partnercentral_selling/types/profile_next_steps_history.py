"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#ProfileNextStepsHistory``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_partnercentral_selling.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_selling.types.date_time


class ProfileNextStepsHistory(TypedDict, closed=True):
    value: "str"
    """<p>Represents the details of the next step recorded, such as follow-up actions or decisions made. This field helps in tracking progress and ensuring alignment with project goals.</p>"""
    time: "aws_sdk_partnercentral_selling.types.date_time.DateTime"
    """<p>Indicates the date and time when a particular next step was recorded or planned. This helps in managing the timeline for the opportunity.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProfileNextStepsHistory) -> dict:
    out: dict = {}
    out["Value"] = value["value"]
    import aws_sdk_partnercentral_selling.types.date_time

    out["Time"] = aws_sdk_partnercentral_selling.types.date_time.serialize_aws_json_1_0(
        value["time"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ProfileNextStepsHistory:
    out: ProfileNextStepsHistory = {}  # type: ignore[typeddict-item]
    if "Value" in data:
        out["value"] = data["Value"]
    else:
        raise DeserializationError("ProfileNextStepsHistory.value required")
    if "Time" in data:
        import aws_sdk_partnercentral_selling.types.date_time

        out["time"] = (
            aws_sdk_partnercentral_selling.types.date_time.deserialize_aws_json_1_0(
                data["Time"]
            )
        )
    else:
        raise DeserializationError("ProfileNextStepsHistory.time required")
    return out
