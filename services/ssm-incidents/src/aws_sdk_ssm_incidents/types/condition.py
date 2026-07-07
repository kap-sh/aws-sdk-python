"""Generated from Smithy shape ``com.amazonaws.ssmincidents#Condition``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_ssm_incidents.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_ssm_incidents.types.attribute_value_list


class _Condition_before(TypedDict, closed=True):
    before: "datetime.datetime"


class _Condition_after(TypedDict, closed=True):
    after: "datetime.datetime"


class _Condition_equals(TypedDict, closed=True):
    equals: "aws_sdk_ssm_incidents.types.attribute_value_list.AttributeValueList"


Condition: TypeAlias = _Condition_before | _Condition_after | _Condition_equals


# --- restJson1 ser/de ---
def serialize_json(value: Condition) -> dict:
    if "before" in value:
        import aws_sdk_ssm_incidents.types._prelude.timestamp

        return {
            "before": aws_sdk_ssm_incidents.types._prelude.timestamp.serialize_json(
                value["before"]
            )
        }
    elif "after" in value:
        import aws_sdk_ssm_incidents.types._prelude.timestamp

        return {
            "after": aws_sdk_ssm_incidents.types._prelude.timestamp.serialize_json(
                value["after"]
            )
        }
    elif "equals" in value:
        import aws_sdk_ssm_incidents.types.attribute_value_list

        return {
            "equals": aws_sdk_ssm_incidents.types.attribute_value_list.serialize_json(
                value["equals"]
            )
        }
    else:
        raise SerializationError("Condition: no variant present")


def deserialize_json(data: dict) -> Condition:
    if "before" in data:
        import aws_sdk_ssm_incidents.types._prelude.timestamp

        return {
            "before": aws_sdk_ssm_incidents.types._prelude.timestamp.deserialize_json(
                data["before"]
            )
        }
    elif "after" in data:
        import aws_sdk_ssm_incidents.types._prelude.timestamp

        return {
            "after": aws_sdk_ssm_incidents.types._prelude.timestamp.deserialize_json(
                data["after"]
            )
        }
    elif "equals" in data:
        import aws_sdk_ssm_incidents.types.attribute_value_list

        return {
            "equals": aws_sdk_ssm_incidents.types.attribute_value_list.deserialize_json(
                data["equals"]
            )
        }
    else:
        raise DeserializationError("Condition: no recognized variant key")
