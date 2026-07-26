"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#StartServicePeriodTypeFilters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_channel.types.service_period_type_list


class StartServicePeriodTypeFilters(TypedDict, closed=True):
    service_period_types: NotRequired[
        "capo_partnercentral_channel.types.service_period_type_list.ServicePeriodTypeList"
    ]
    """<p>Filter by service period types.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StartServicePeriodTypeFilters) -> dict:
    out: dict = {}
    if "service_period_types" in value:
        import capo_partnercentral_channel.types.service_period_type_list

        out["servicePeriodTypes"] = (
            capo_partnercentral_channel.types.service_period_type_list.serialize_aws_json_1_0(
                value["service_period_types"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> StartServicePeriodTypeFilters:
    out: StartServicePeriodTypeFilters = {}  # type: ignore[typeddict-item]
    if "servicePeriodTypes" in data:
        import capo_partnercentral_channel.types.service_period_type_list

        out["service_period_types"] = (
            capo_partnercentral_channel.types.service_period_type_list.deserialize_aws_json_1_0(
                data["servicePeriodTypes"]
            )
        )
    return out
