"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#ValidityPeriod``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_pca_connector_ad.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pca_connector_ad.types.validity_period_type


class ValidityPeriod(TypedDict):
    period_type: (
        "aws_sdk_pca_connector_ad.types.validity_period_type.ValidityPeriodType"
    )
    """<p>The unit of time. You can select hours, days, weeks, months, and years.</p>"""
    period: "int"
    """<p>The numeric value for the validity period.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidityPeriod) -> dict:
    out: dict = {}
    import aws_sdk_pca_connector_ad.types.validity_period_type

    out["PeriodType"] = (
        aws_sdk_pca_connector_ad.types.validity_period_type.serialize_json(
            value["period_type"]
        )
    )
    out["Period"] = value["period"]
    return out


def deserialize_json(data: dict) -> ValidityPeriod:
    out: ValidityPeriod = {}  # type: ignore[typeddict-item]
    if "PeriodType" in data:
        import aws_sdk_pca_connector_ad.types.validity_period_type

        out["period_type"] = (
            aws_sdk_pca_connector_ad.types.validity_period_type.deserialize_json(
                data["PeriodType"]
            )
        )
    else:
        raise DeserializationError("ValidityPeriod.period_type required")
    if "Period" in data:
        out["period"] = data["Period"]
    else:
        raise DeserializationError("ValidityPeriod.period required")
    return out
