"""Generated from Smithy shape ``com.amazonaws.snowdevicemanagement#InstanceSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import aws_sdk_snow_device_management.types.instance


class InstanceSummary(TypedDict, closed=True):
    instance: NotRequired["aws_sdk_snow_device_management.types.instance.Instance"]
    """<p>A structure containing details about the instance.</p>"""
    last_updated_at: NotRequired["datetime.datetime"]
    """<p>When the instance summary was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InstanceSummary) -> dict:
    out: dict = {}
    if "instance" in value:
        import aws_sdk_snow_device_management.types.instance

        out["instance"] = aws_sdk_snow_device_management.types.instance.serialize_json(
            value["instance"]
        )
    if "last_updated_at" in value:
        import aws_sdk_snow_device_management.types._prelude.timestamp

        out["lastUpdatedAt"] = (
            aws_sdk_snow_device_management.types._prelude.timestamp.serialize_json(
                value["last_updated_at"]
            )
        )
    return out


def deserialize_json(data: dict) -> InstanceSummary:
    out: InstanceSummary = {}  # type: ignore[typeddict-item]
    if "instance" in data:
        import aws_sdk_snow_device_management.types.instance

        out["instance"] = (
            aws_sdk_snow_device_management.types.instance.deserialize_json(
                data["instance"]
            )
        )
    if "lastUpdatedAt" in data:
        import aws_sdk_snow_device_management.types._prelude.timestamp

        out["last_updated_at"] = (
            aws_sdk_snow_device_management.types._prelude.timestamp.deserialize_json(
                data["lastUpdatedAt"]
            )
        )
    return out
