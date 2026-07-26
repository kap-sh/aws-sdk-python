"""Generated from Smithy shape ``com.amazonaws.servicediscovery#ServiceSummariesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_servicediscovery.types.service_summary

ServiceSummariesList: TypeAlias = list[
    "capo_servicediscovery.types.service_summary.ServiceSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceSummariesList) -> list:
    import capo_servicediscovery.types.service_summary

    out: list = []
    for item in value:
        out.append(
            capo_servicediscovery.types.service_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ServiceSummariesList:
    import capo_servicediscovery.types.service_summary

    out: ServiceSummariesList = []
    for item in data:
        out.append(
            capo_servicediscovery.types.service_summary.deserialize_aws_json_1_1(item)
        )
    return out
