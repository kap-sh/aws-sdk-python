"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#NextStepsHistory``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_partnercentral_selling.errors import DeserializationError

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.date_time


class NextStepsHistory(TypedDict, closed=True):
    value: "str"
    """<p>Indicates the step's execution details.</p>"""
    time: "capo_partnercentral_selling.types.date_time.DateTime"
    """<p>Indicates the step execution time.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: NextStepsHistory) -> dict:
    out: dict = {}
    out["Value"] = value["value"]
    import capo_partnercentral_selling.types.date_time

    out["Time"] = capo_partnercentral_selling.types.date_time.serialize_aws_json_1_0(
        value["time"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> NextStepsHistory:
    out: NextStepsHistory = {}  # type: ignore[typeddict-item]
    if "Value" in data:
        out["value"] = data["Value"]
    else:
        raise DeserializationError("NextStepsHistory.value required")
    if "Time" in data:
        import capo_partnercentral_selling.types.date_time

        out["time"] = (
            capo_partnercentral_selling.types.date_time.deserialize_aws_json_1_0(
                data["Time"]
            )
        )
    else:
        raise DeserializationError("NextStepsHistory.time required")
    return out
