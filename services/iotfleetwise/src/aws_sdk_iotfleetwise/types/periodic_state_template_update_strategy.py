"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#PeriodicStateTemplateUpdateStrategy``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iotfleetwise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.time_period


class PeriodicStateTemplateUpdateStrategy(TypedDict):
    state_template_update_rate: "aws_sdk_iotfleetwise.types.time_period.TimePeriod"


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PeriodicStateTemplateUpdateStrategy) -> dict:
    out: dict = {}
    import aws_sdk_iotfleetwise.types.time_period

    out["stateTemplateUpdateRate"] = (
        aws_sdk_iotfleetwise.types.time_period.serialize_aws_json_1_0(
            value["state_template_update_rate"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> PeriodicStateTemplateUpdateStrategy:
    out: PeriodicStateTemplateUpdateStrategy = {}  # type: ignore[typeddict-item]
    if "stateTemplateUpdateRate" in data:
        import aws_sdk_iotfleetwise.types.time_period

        out["state_template_update_rate"] = (
            aws_sdk_iotfleetwise.types.time_period.deserialize_aws_json_1_0(
                data["stateTemplateUpdateRate"]
            )
        )
    else:
        raise DeserializationError(
            "PeriodicStateTemplateUpdateStrategy.state_template_update_rate required"
        )
    return out
