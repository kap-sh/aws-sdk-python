"""Generated from Smithy shape ``com.amazonaws.pinpoint#SegmentDemographics``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.set_dimension


class SegmentDemographics(TypedDict, closed=True):
    app_version: NotRequired["aws_sdk_pinpoint.types.set_dimension.SetDimension"]
    """<p>The app version criteria for the segment.</p>"""
    channel: NotRequired["aws_sdk_pinpoint.types.set_dimension.SetDimension"]
    """<p>The channel criteria for the segment.</p>"""
    device_type: NotRequired["aws_sdk_pinpoint.types.set_dimension.SetDimension"]
    """<p>The device type criteria for the segment.</p>"""
    make: NotRequired["aws_sdk_pinpoint.types.set_dimension.SetDimension"]
    """<p>The device make criteria for the segment.</p>"""
    model: NotRequired["aws_sdk_pinpoint.types.set_dimension.SetDimension"]
    """<p>The device model criteria for the segment.</p>"""
    platform: NotRequired["aws_sdk_pinpoint.types.set_dimension.SetDimension"]
    """<p>The device platform criteria for the segment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SegmentDemographics) -> dict:
    out: dict = {}
    if "app_version" in value:
        import aws_sdk_pinpoint.types.set_dimension

        out["AppVersion"] = aws_sdk_pinpoint.types.set_dimension.serialize_json(
            value["app_version"]
        )
    if "channel" in value:
        import aws_sdk_pinpoint.types.set_dimension

        out["Channel"] = aws_sdk_pinpoint.types.set_dimension.serialize_json(
            value["channel"]
        )
    if "device_type" in value:
        import aws_sdk_pinpoint.types.set_dimension

        out["DeviceType"] = aws_sdk_pinpoint.types.set_dimension.serialize_json(
            value["device_type"]
        )
    if "make" in value:
        import aws_sdk_pinpoint.types.set_dimension

        out["Make"] = aws_sdk_pinpoint.types.set_dimension.serialize_json(value["make"])
    if "model" in value:
        import aws_sdk_pinpoint.types.set_dimension

        out["Model"] = aws_sdk_pinpoint.types.set_dimension.serialize_json(
            value["model"]
        )
    if "platform" in value:
        import aws_sdk_pinpoint.types.set_dimension

        out["Platform"] = aws_sdk_pinpoint.types.set_dimension.serialize_json(
            value["platform"]
        )
    return out


def deserialize_json(data: dict) -> SegmentDemographics:
    out: SegmentDemographics = {}  # type: ignore[typeddict-item]
    if "AppVersion" in data:
        import aws_sdk_pinpoint.types.set_dimension

        out["app_version"] = aws_sdk_pinpoint.types.set_dimension.deserialize_json(
            data["AppVersion"]
        )
    if "Channel" in data:
        import aws_sdk_pinpoint.types.set_dimension

        out["channel"] = aws_sdk_pinpoint.types.set_dimension.deserialize_json(
            data["Channel"]
        )
    if "DeviceType" in data:
        import aws_sdk_pinpoint.types.set_dimension

        out["device_type"] = aws_sdk_pinpoint.types.set_dimension.deserialize_json(
            data["DeviceType"]
        )
    if "Make" in data:
        import aws_sdk_pinpoint.types.set_dimension

        out["make"] = aws_sdk_pinpoint.types.set_dimension.deserialize_json(
            data["Make"]
        )
    if "Model" in data:
        import aws_sdk_pinpoint.types.set_dimension

        out["model"] = aws_sdk_pinpoint.types.set_dimension.deserialize_json(
            data["Model"]
        )
    if "Platform" in data:
        import aws_sdk_pinpoint.types.set_dimension

        out["platform"] = aws_sdk_pinpoint.types.set_dimension.deserialize_json(
            data["Platform"]
        )
    return out
