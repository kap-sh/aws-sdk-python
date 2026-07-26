"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#FilterLifeCycleStage``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.stage

FilterLifeCycleStage: TypeAlias = list["capo_partnercentral_selling.types.stage.Stage"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FilterLifeCycleStage) -> list:
    import capo_partnercentral_selling.types.stage

    out: list = []
    for item in value:
        out.append(capo_partnercentral_selling.types.stage.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> FilterLifeCycleStage:
    import capo_partnercentral_selling.types.stage

    out: FilterLifeCycleStage = []
    for item in data:
        out.append(
            capo_partnercentral_selling.types.stage.deserialize_aws_json_1_0(item)
        )
    return out
