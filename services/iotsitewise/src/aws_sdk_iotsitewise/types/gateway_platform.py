"""Generated from Smithy shape ``com.amazonaws.iotsitewise#GatewayPlatform``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.greengrass
    import aws_sdk_iotsitewise.types.greengrass_v2
    import aws_sdk_iotsitewise.types.siemens_ie


class GatewayPlatform(TypedDict):
    greengrass: NotRequired["aws_sdk_iotsitewise.types.greengrass.Greengrass"]
    """<p>A gateway that runs on IoT Greengrass.</p>"""
    greengrass_v2: NotRequired["aws_sdk_iotsitewise.types.greengrass_v2.GreengrassV2"]
    """<p>A gateway that runs on IoT Greengrass V2.</p>"""
    siemens_ie: NotRequired["aws_sdk_iotsitewise.types.siemens_ie.SiemensIE"]
    """<p>A SiteWise Edge gateway that runs on a Siemens Industrial Edge Device.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GatewayPlatform) -> dict:
    out: dict = {}
    if "greengrass" in value:
        import aws_sdk_iotsitewise.types.greengrass

        out["greengrass"] = aws_sdk_iotsitewise.types.greengrass.serialize_json(
            value["greengrass"]
        )
    if "greengrass_v2" in value:
        import aws_sdk_iotsitewise.types.greengrass_v2

        out["greengrassV2"] = aws_sdk_iotsitewise.types.greengrass_v2.serialize_json(
            value["greengrass_v2"]
        )
    if "siemens_ie" in value:
        import aws_sdk_iotsitewise.types.siemens_ie

        out["siemensIE"] = aws_sdk_iotsitewise.types.siemens_ie.serialize_json(
            value["siemens_ie"]
        )
    return out


def deserialize_json(data: dict) -> GatewayPlatform:
    out: GatewayPlatform = {}  # type: ignore[typeddict-item]
    if "greengrass" in data:
        import aws_sdk_iotsitewise.types.greengrass

        out["greengrass"] = aws_sdk_iotsitewise.types.greengrass.deserialize_json(
            data["greengrass"]
        )
    if "greengrassV2" in data:
        import aws_sdk_iotsitewise.types.greengrass_v2

        out["greengrass_v2"] = aws_sdk_iotsitewise.types.greengrass_v2.deserialize_json(
            data["greengrassV2"]
        )
    if "siemensIE" in data:
        import aws_sdk_iotsitewise.types.siemens_ie

        out["siemens_ie"] = aws_sdk_iotsitewise.types.siemens_ie.deserialize_json(
            data["siemensIE"]
        )
    return out
