"""Generated from Smithy shape ``com.amazonaws.devopsagent#PagerDutyConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.email_address
    import aws_sdk_devops_agent.types.pager_duty_services_list


class PagerDutyConfiguration(TypedDict):
    services: (
        "aws_sdk_devops_agent.types.pager_duty_services_list.PagerDutyServicesList"
    )
    """<p>List of Pagerduty service available for the association.</p>"""
    customer_email: "aws_sdk_devops_agent.types.email_address.EmailAddress"
    """<p>Email to be used in Pagerduty API header</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PagerDutyConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_devops_agent.types.pager_duty_services_list

    out["services"] = (
        aws_sdk_devops_agent.types.pager_duty_services_list.serialize_json(
            value["services"]
        )
    )
    out["customerEmail"] = value["customer_email"]
    return out


def deserialize_json(data: dict) -> PagerDutyConfiguration:
    out: PagerDutyConfiguration = {}  # type: ignore[typeddict-item]
    if "services" in data:
        import aws_sdk_devops_agent.types.pager_duty_services_list

        out["services"] = (
            aws_sdk_devops_agent.types.pager_duty_services_list.deserialize_json(
                data["services"]
            )
        )
    else:
        raise DeserializationError("PagerDutyConfiguration.services required")
    if "customerEmail" in data:
        out["customer_email"] = data["customerEmail"]
    else:
        raise DeserializationError("PagerDutyConfiguration.customer_email required")
    return out
