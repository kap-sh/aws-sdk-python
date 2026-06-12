"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#SignalFetchConfig``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_iotfleetwise.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.condition_based_signal_fetch_config
    import aws_sdk_iotfleetwise.types.time_based_signal_fetch_config


class _SignalFetchConfig_timeBased(TypedDict):
    timeBased: "aws_sdk_iotfleetwise.types.time_based_signal_fetch_config.TimeBasedSignalFetchConfig"


class _SignalFetchConfig_conditionBased(TypedDict):
    conditionBased: "aws_sdk_iotfleetwise.types.condition_based_signal_fetch_config.ConditionBasedSignalFetchConfig"


SignalFetchConfig: TypeAlias = (
    _SignalFetchConfig_timeBased | _SignalFetchConfig_conditionBased
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SignalFetchConfig) -> dict:
    if "timeBased" in value:
        import aws_sdk_iotfleetwise.types.time_based_signal_fetch_config

        return {
            "timeBased": aws_sdk_iotfleetwise.types.time_based_signal_fetch_config.serialize_aws_json_1_0(
                value["timeBased"]
            )
        }
    elif "conditionBased" in value:
        import aws_sdk_iotfleetwise.types.condition_based_signal_fetch_config

        return {
            "conditionBased": aws_sdk_iotfleetwise.types.condition_based_signal_fetch_config.serialize_aws_json_1_0(
                value["conditionBased"]
            )
        }
    else:
        raise SerializationError("SignalFetchConfig: no variant present")


def deserialize_aws_json_1_0(data: dict) -> SignalFetchConfig:
    if "timeBased" in data:
        import aws_sdk_iotfleetwise.types.time_based_signal_fetch_config

        return {
            "timeBased": aws_sdk_iotfleetwise.types.time_based_signal_fetch_config.deserialize_aws_json_1_0(
                data["timeBased"]
            )
        }
    elif "conditionBased" in data:
        import aws_sdk_iotfleetwise.types.condition_based_signal_fetch_config

        return {
            "conditionBased": aws_sdk_iotfleetwise.types.condition_based_signal_fetch_config.deserialize_aws_json_1_0(
                data["conditionBased"]
            )
        }
    else:
        raise DeserializationError("SignalFetchConfig: no recognized variant key")
