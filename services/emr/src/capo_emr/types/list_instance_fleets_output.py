"""Generated from Smithy shape ``com.amazonaws.emr#ListInstanceFleetsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr.types.instance_fleet_list
    import capo_emr.types.marker


class ListInstanceFleetsOutput(TypedDict, closed=True):
    instance_fleets: NotRequired["capo_emr.types.instance_fleet_list.InstanceFleetList"]
    """<p>The list of instance fleets for the cluster and given filters.</p>"""
    marker: NotRequired["capo_emr.types.marker.Marker"]
    """<p>The pagination token that indicates the next set of results to retrieve.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListInstanceFleetsOutput) -> dict:
    out: dict = {}
    if "instance_fleets" in value:
        import capo_emr.types.instance_fleet_list

        out["InstanceFleets"] = (
            capo_emr.types.instance_fleet_list.serialize_aws_json_1_1(
                value["instance_fleets"]
            )
        )
    if "marker" in value:
        out["Marker"] = value["marker"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListInstanceFleetsOutput:
    out: ListInstanceFleetsOutput = {}  # type: ignore[typeddict-item]
    if "InstanceFleets" in data:
        import capo_emr.types.instance_fleet_list

        out["instance_fleets"] = (
            capo_emr.types.instance_fleet_list.deserialize_aws_json_1_1(
                data["InstanceFleets"]
            )
        )
    if "Marker" in data:
        out["marker"] = data["Marker"]
    return out
