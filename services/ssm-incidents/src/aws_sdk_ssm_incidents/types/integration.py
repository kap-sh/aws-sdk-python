"""Generated from Smithy shape ``com.amazonaws.ssmincidents#Integration``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_ssm_incidents.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_ssm_incidents.types.pager_duty_configuration


class _Integration_pagerDutyConfiguration(TypedDict):
    pagerDutyConfiguration: (
        "aws_sdk_ssm_incidents.types.pager_duty_configuration.PagerDutyConfiguration"
    )


Integration: TypeAlias = _Integration_pagerDutyConfiguration


# --- restJson1 ser/de ---
def serialize_json(value: Integration) -> dict:
    if "pagerDutyConfiguration" in value:
        import aws_sdk_ssm_incidents.types.pager_duty_configuration

        return {
            "pagerDutyConfiguration": aws_sdk_ssm_incidents.types.pager_duty_configuration.serialize_json(
                value["pagerDutyConfiguration"]
            )
        }
    else:
        raise SerializationError("Integration: no variant present")


def deserialize_json(data: dict) -> Integration:
    if "pagerDutyConfiguration" in data:
        import aws_sdk_ssm_incidents.types.pager_duty_configuration

        return {
            "pagerDutyConfiguration": aws_sdk_ssm_incidents.types.pager_duty_configuration.deserialize_json(
                data["pagerDutyConfiguration"]
            )
        }
    else:
        raise DeserializationError("Integration: no recognized variant key")
