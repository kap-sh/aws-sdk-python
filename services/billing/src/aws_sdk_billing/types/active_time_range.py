"""Generated from Smithy shape ``com.amazonaws.billing#ActiveTimeRange``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_billing.errors import DeserializationError

if TYPE_CHECKING:
    import datetime


class ActiveTimeRange(TypedDict, closed=True):
    active_after_inclusive: "datetime.datetime"
    """<p>The inclusive time range start date.</p>"""
    active_before_inclusive: "datetime.datetime"
    """<p> The inclusive time range end date. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ActiveTimeRange) -> dict:
    out: dict = {}
    import aws_sdk_billing.types._prelude.timestamp

    out["activeAfterInclusive"] = (
        aws_sdk_billing.types._prelude.timestamp.serialize_aws_json_1_0(
            value["active_after_inclusive"]
        )
    )
    import aws_sdk_billing.types._prelude.timestamp

    out["activeBeforeInclusive"] = (
        aws_sdk_billing.types._prelude.timestamp.serialize_aws_json_1_0(
            value["active_before_inclusive"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ActiveTimeRange:
    out: ActiveTimeRange = {}  # type: ignore[typeddict-item]
    if "activeAfterInclusive" in data:
        import aws_sdk_billing.types._prelude.timestamp

        out["active_after_inclusive"] = (
            aws_sdk_billing.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["activeAfterInclusive"]
            )
        )
    else:
        raise DeserializationError("ActiveTimeRange.active_after_inclusive required")
    if "activeBeforeInclusive" in data:
        import aws_sdk_billing.types._prelude.timestamp

        out["active_before_inclusive"] = (
            aws_sdk_billing.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["activeBeforeInclusive"]
            )
        )
    else:
        raise DeserializationError("ActiveTimeRange.active_before_inclusive required")
    return out
