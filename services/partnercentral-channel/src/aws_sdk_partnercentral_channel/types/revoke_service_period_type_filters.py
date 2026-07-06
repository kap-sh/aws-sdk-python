"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#RevokeServicePeriodTypeFilters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_partnercentral_channel.types.service_period_type_list


class RevokeServicePeriodTypeFilters(TypedDict, closed=True):
    service_period_types: NotRequired[
        "aws_sdk_partnercentral_channel.types.service_period_type_list.ServicePeriodTypeList"
    ]
    """<p>Filter by service period types.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RevokeServicePeriodTypeFilters) -> dict:
    out: dict = {}
    if "service_period_types" in value:
        import aws_sdk_partnercentral_channel.types.service_period_type_list

        out["servicePeriodTypes"] = (
            aws_sdk_partnercentral_channel.types.service_period_type_list.serialize_aws_json_1_0(
                value["service_period_types"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> RevokeServicePeriodTypeFilters:
    out: RevokeServicePeriodTypeFilters = {}  # type: ignore[typeddict-item]
    if "servicePeriodTypes" in data:
        import aws_sdk_partnercentral_channel.types.service_period_type_list

        out["service_period_types"] = (
            aws_sdk_partnercentral_channel.types.service_period_type_list.deserialize_aws_json_1_0(
                data["servicePeriodTypes"]
            )
        )
    return out
