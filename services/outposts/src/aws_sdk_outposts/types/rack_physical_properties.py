"""Generated from Smithy shape ``com.amazonaws.outposts#RackPhysicalProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_outposts.types.fiber_optic_cable_type
    import aws_sdk_outposts.types.maximum_supported_weight_lbs
    import aws_sdk_outposts.types.optical_standard
    import aws_sdk_outposts.types.power_connector
    import aws_sdk_outposts.types.power_draw_kva
    import aws_sdk_outposts.types.power_feed_drop
    import aws_sdk_outposts.types.power_phase
    import aws_sdk_outposts.types.uplink_count
    import aws_sdk_outposts.types.uplink_gbps


class RackPhysicalProperties(TypedDict, closed=True):
    power_draw_kva: NotRequired["aws_sdk_outposts.types.power_draw_kva.PowerDrawKva"]
    """<p>The power draw available at the hardware placement position for the rack. </p>"""
    power_phase: NotRequired["aws_sdk_outposts.types.power_phase.PowerPhase"]
    """<p>The power option that you can provide for hardware.</p>"""
    power_connector: NotRequired[
        "aws_sdk_outposts.types.power_connector.PowerConnector"
    ]
    """<p>The power connector for the hardware. </p>"""
    power_feed_drop: NotRequired["aws_sdk_outposts.types.power_feed_drop.PowerFeedDrop"]
    """<p>The position of the power feed.</p>"""
    uplink_gbps: NotRequired["aws_sdk_outposts.types.uplink_gbps.UplinkGbps"]
    """<p>The uplink speed the rack supports for the connection to the Region. </p>"""
    uplink_count: NotRequired["aws_sdk_outposts.types.uplink_count.UplinkCount"]
    """<p>The number of uplinks each Outpost network device.</p>"""
    fiber_optic_cable_type: NotRequired[
        "aws_sdk_outposts.types.fiber_optic_cable_type.FiberOpticCableType"
    ]
    """<p>The type of fiber used to attach the Outpost to the network. </p>"""
    optical_standard: NotRequired[
        "aws_sdk_outposts.types.optical_standard.OpticalStandard"
    ]
    r"""<p>The type of optical standard used to attach the Outpost to the network. This field is dependent on uplink speed, fiber type, and distance to the upstream device. For more information about networking requirements for racks, see <a href=\"https://docs.aws.amazon.com/outposts/latest/userguide/outposts-requirements.html#facility-networking\">Network</a> in the Amazon Web Services Outposts User Guide. </p>"""
    maximum_supported_weight_lbs: NotRequired[
        "aws_sdk_outposts.types.maximum_supported_weight_lbs.MaximumSupportedWeightLbs"
    ]
    """<p>The maximum rack weight that this site can support. <code>NO_LIMIT</code> is over 2000 lbs (907 kg). </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RackPhysicalProperties) -> dict:
    out: dict = {}
    if "power_draw_kva" in value:
        import aws_sdk_outposts.types.power_draw_kva

        out["PowerDrawKva"] = aws_sdk_outposts.types.power_draw_kva.serialize_json(
            value["power_draw_kva"]
        )
    if "power_phase" in value:
        import aws_sdk_outposts.types.power_phase

        out["PowerPhase"] = aws_sdk_outposts.types.power_phase.serialize_json(
            value["power_phase"]
        )
    if "power_connector" in value:
        import aws_sdk_outposts.types.power_connector

        out["PowerConnector"] = aws_sdk_outposts.types.power_connector.serialize_json(
            value["power_connector"]
        )
    if "power_feed_drop" in value:
        import aws_sdk_outposts.types.power_feed_drop

        out["PowerFeedDrop"] = aws_sdk_outposts.types.power_feed_drop.serialize_json(
            value["power_feed_drop"]
        )
    if "uplink_gbps" in value:
        import aws_sdk_outposts.types.uplink_gbps

        out["UplinkGbps"] = aws_sdk_outposts.types.uplink_gbps.serialize_json(
            value["uplink_gbps"]
        )
    if "uplink_count" in value:
        import aws_sdk_outposts.types.uplink_count

        out["UplinkCount"] = aws_sdk_outposts.types.uplink_count.serialize_json(
            value["uplink_count"]
        )
    if "fiber_optic_cable_type" in value:
        import aws_sdk_outposts.types.fiber_optic_cable_type

        out["FiberOpticCableType"] = (
            aws_sdk_outposts.types.fiber_optic_cable_type.serialize_json(
                value["fiber_optic_cable_type"]
            )
        )
    if "optical_standard" in value:
        import aws_sdk_outposts.types.optical_standard

        out["OpticalStandard"] = aws_sdk_outposts.types.optical_standard.serialize_json(
            value["optical_standard"]
        )
    if "maximum_supported_weight_lbs" in value:
        import aws_sdk_outposts.types.maximum_supported_weight_lbs

        out["MaximumSupportedWeightLbs"] = (
            aws_sdk_outposts.types.maximum_supported_weight_lbs.serialize_json(
                value["maximum_supported_weight_lbs"]
            )
        )
    return out


def deserialize_json(data: dict) -> RackPhysicalProperties:
    out: RackPhysicalProperties = {}  # type: ignore[typeddict-item]
    if "PowerDrawKva" in data:
        import aws_sdk_outposts.types.power_draw_kva

        out["power_draw_kva"] = aws_sdk_outposts.types.power_draw_kva.deserialize_json(
            data["PowerDrawKva"]
        )
    if "PowerPhase" in data:
        import aws_sdk_outposts.types.power_phase

        out["power_phase"] = aws_sdk_outposts.types.power_phase.deserialize_json(
            data["PowerPhase"]
        )
    if "PowerConnector" in data:
        import aws_sdk_outposts.types.power_connector

        out["power_connector"] = (
            aws_sdk_outposts.types.power_connector.deserialize_json(
                data["PowerConnector"]
            )
        )
    if "PowerFeedDrop" in data:
        import aws_sdk_outposts.types.power_feed_drop

        out["power_feed_drop"] = (
            aws_sdk_outposts.types.power_feed_drop.deserialize_json(
                data["PowerFeedDrop"]
            )
        )
    if "UplinkGbps" in data:
        import aws_sdk_outposts.types.uplink_gbps

        out["uplink_gbps"] = aws_sdk_outposts.types.uplink_gbps.deserialize_json(
            data["UplinkGbps"]
        )
    if "UplinkCount" in data:
        import aws_sdk_outposts.types.uplink_count

        out["uplink_count"] = aws_sdk_outposts.types.uplink_count.deserialize_json(
            data["UplinkCount"]
        )
    if "FiberOpticCableType" in data:
        import aws_sdk_outposts.types.fiber_optic_cable_type

        out["fiber_optic_cable_type"] = (
            aws_sdk_outposts.types.fiber_optic_cable_type.deserialize_json(
                data["FiberOpticCableType"]
            )
        )
    if "OpticalStandard" in data:
        import aws_sdk_outposts.types.optical_standard

        out["optical_standard"] = (
            aws_sdk_outposts.types.optical_standard.deserialize_json(
                data["OpticalStandard"]
            )
        )
    if "MaximumSupportedWeightLbs" in data:
        import aws_sdk_outposts.types.maximum_supported_weight_lbs

        out["maximum_supported_weight_lbs"] = (
            aws_sdk_outposts.types.maximum_supported_weight_lbs.deserialize_json(
                data["MaximumSupportedWeightLbs"]
            )
        )
    return out
