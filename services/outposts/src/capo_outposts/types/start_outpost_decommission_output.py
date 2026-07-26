"""Generated from Smithy shape ``com.amazonaws.outposts#StartOutpostDecommissionOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_outposts.types.blocking_resource_type_list
    import capo_outposts.types.decommission_request_status


class StartOutpostDecommissionOutput(TypedDict, closed=True):
    status: NotRequired[
        "capo_outposts.types.decommission_request_status.DecommissionRequestStatus"
    ]
    """<p>The status of the decommission request.</p>"""
    blocking_resource_types: NotRequired[
        "capo_outposts.types.blocking_resource_type_list.BlockingResourceTypeList"
    ]
    """<p>The resources still associated with the Outpost that you are decommissioning.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartOutpostDecommissionOutput) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_outposts.types.decommission_request_status

        out["Status"] = capo_outposts.types.decommission_request_status.serialize_json(
            value["status"]
        )
    if "blocking_resource_types" in value:
        import capo_outposts.types.blocking_resource_type_list

        out["BlockingResourceTypes"] = (
            capo_outposts.types.blocking_resource_type_list.serialize_json(
                value["blocking_resource_types"]
            )
        )
    return out


def deserialize_json(data: dict) -> StartOutpostDecommissionOutput:
    out: StartOutpostDecommissionOutput = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import capo_outposts.types.decommission_request_status

        out["status"] = (
            capo_outposts.types.decommission_request_status.deserialize_json(
                data["Status"]
            )
        )
    if "BlockingResourceTypes" in data:
        import capo_outposts.types.blocking_resource_type_list

        out["blocking_resource_types"] = (
            capo_outposts.types.blocking_resource_type_list.deserialize_json(
                data["BlockingResourceTypes"]
            )
        )
    return out
