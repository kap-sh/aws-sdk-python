"""Generated from Smithy shape ``com.amazonaws.servicequotas#QuotaPeriod``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_service_quotas.types.period_unit
    import aws_sdk_service_quotas.types.period_value


class QuotaPeriod(TypedDict):
    period_value: NotRequired["aws_sdk_service_quotas.types.period_value.PeriodValue"]
    """<p>The value associated with the reported <code>PeriodUnit</code>.</p>"""
    period_unit: NotRequired["aws_sdk_service_quotas.types.period_unit.PeriodUnit"]
    """<p>The time unit.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QuotaPeriod) -> dict:
    out: dict = {}
    if "period_value" in value:
        out["PeriodValue"] = value["period_value"]
    if "period_unit" in value:
        import aws_sdk_service_quotas.types.period_unit

        out["PeriodUnit"] = (
            aws_sdk_service_quotas.types.period_unit.serialize_aws_json_1_1(
                value["period_unit"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> QuotaPeriod:
    out: QuotaPeriod = {}  # type: ignore[typeddict-item]
    if "PeriodValue" in data:
        out["period_value"] = data["PeriodValue"]
    if "PeriodUnit" in data:
        import aws_sdk_service_quotas.types.period_unit

        out["period_unit"] = (
            aws_sdk_service_quotas.types.period_unit.deserialize_aws_json_1_1(
                data["PeriodUnit"]
            )
        )
    return out
