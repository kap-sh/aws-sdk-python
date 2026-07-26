"""Generated from Smithy shape ``com.amazonaws.emr#PlacementType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr.types.xml_string
    import capo_emr.types.xml_string_max_len256_list


class PlacementType(TypedDict, closed=True):
    availability_zone: NotRequired["capo_emr.types.xml_string.XmlString"]
    """<p>The Amazon EC2 Availability Zone for the cluster. <code>AvailabilityZone</code> is used for uniform instance groups, while <code>AvailabilityZones</code> (plural) is used for instance fleets.</p>"""
    availability_zones: NotRequired[
        "capo_emr.types.xml_string_max_len256_list.XmlStringMaxLen256List"
    ]
    """<p>When multiple Availability Zones are specified, Amazon EMR evaluates them and launches instances in the optimal Availability Zone. <code>AvailabilityZones</code> is used for instance fleets, while <code>AvailabilityZone</code> (singular) is used for uniform instance groups.</p> <note> <p>The instance fleet configuration is available only in Amazon EMR releases 4.8.0 and later, excluding 5.0.x versions.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PlacementType) -> dict:
    out: dict = {}
    if "availability_zone" in value:
        out["AvailabilityZone"] = value["availability_zone"]
    if "availability_zones" in value:
        import capo_emr.types.xml_string_max_len256_list

        out["AvailabilityZones"] = (
            capo_emr.types.xml_string_max_len256_list.serialize_aws_json_1_1(
                value["availability_zones"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PlacementType:
    out: PlacementType = {}  # type: ignore[typeddict-item]
    if "AvailabilityZone" in data:
        out["availability_zone"] = data["AvailabilityZone"]
    if "AvailabilityZones" in data:
        import capo_emr.types.xml_string_max_len256_list

        out["availability_zones"] = (
            capo_emr.types.xml_string_max_len256_list.deserialize_aws_json_1_1(
                data["AvailabilityZones"]
            )
        )
    return out
