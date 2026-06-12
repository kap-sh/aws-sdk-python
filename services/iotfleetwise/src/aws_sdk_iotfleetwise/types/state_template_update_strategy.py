"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#StateTemplateUpdateStrategy``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_iotfleetwise.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.on_change_state_template_update_strategy
    import aws_sdk_iotfleetwise.types.periodic_state_template_update_strategy


class _StateTemplateUpdateStrategy_periodic(TypedDict):
    periodic: "aws_sdk_iotfleetwise.types.periodic_state_template_update_strategy.PeriodicStateTemplateUpdateStrategy"


class _StateTemplateUpdateStrategy_onChange(TypedDict):
    onChange: "aws_sdk_iotfleetwise.types.on_change_state_template_update_strategy.OnChangeStateTemplateUpdateStrategy"


StateTemplateUpdateStrategy: TypeAlias = (
    _StateTemplateUpdateStrategy_periodic | _StateTemplateUpdateStrategy_onChange
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StateTemplateUpdateStrategy) -> dict:
    if "periodic" in value:
        import aws_sdk_iotfleetwise.types.periodic_state_template_update_strategy

        return {
            "periodic": aws_sdk_iotfleetwise.types.periodic_state_template_update_strategy.serialize_aws_json_1_0(
                value["periodic"]
            )
        }
    elif "onChange" in value:
        import aws_sdk_iotfleetwise.types.on_change_state_template_update_strategy

        return {
            "onChange": aws_sdk_iotfleetwise.types.on_change_state_template_update_strategy.serialize_aws_json_1_0(
                value["onChange"]
            )
        }
    else:
        raise SerializationError("StateTemplateUpdateStrategy: no variant present")


def deserialize_aws_json_1_0(data: dict) -> StateTemplateUpdateStrategy:
    if "periodic" in data:
        import aws_sdk_iotfleetwise.types.periodic_state_template_update_strategy

        return {
            "periodic": aws_sdk_iotfleetwise.types.periodic_state_template_update_strategy.deserialize_aws_json_1_0(
                data["periodic"]
            )
        }
    elif "onChange" in data:
        import aws_sdk_iotfleetwise.types.on_change_state_template_update_strategy

        return {
            "onChange": aws_sdk_iotfleetwise.types.on_change_state_template_update_strategy.deserialize_aws_json_1_0(
                data["onChange"]
            )
        }
    else:
        raise DeserializationError(
            "StateTemplateUpdateStrategy: no recognized variant key"
        )
