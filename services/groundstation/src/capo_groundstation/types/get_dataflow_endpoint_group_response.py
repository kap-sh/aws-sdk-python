"""Generated from Smithy shape ``com.amazonaws.groundstation#GetDataflowEndpointGroupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_groundstation.types.dataflow_endpoint_group_arn
    import capo_groundstation.types.dataflow_endpoint_group_duration_in_seconds
    import capo_groundstation.types.endpoint_details_list
    import capo_groundstation.types.tags_map
    import capo_groundstation.types.uuid


class GetDataflowEndpointGroupResponse(TypedDict, closed=True):
    dataflow_endpoint_group_id: NotRequired["capo_groundstation.types.uuid.Uuid"]
    """<p>UUID of a dataflow endpoint group.</p>"""
    dataflow_endpoint_group_arn: NotRequired[
        "capo_groundstation.types.dataflow_endpoint_group_arn.DataflowEndpointGroupArn"
    ]
    """<p>ARN of a dataflow endpoint group.</p>"""
    endpoints_details: NotRequired[
        "capo_groundstation.types.endpoint_details_list.EndpointDetailsList"
    ]
    """<p>Details of a dataflow endpoint.</p>"""
    tags: NotRequired["capo_groundstation.types.tags_map.TagsMap"]
    """<p>Tags assigned to a dataflow endpoint group.</p>"""
    contact_pre_pass_duration_seconds: NotRequired[
        "capo_groundstation.types.dataflow_endpoint_group_duration_in_seconds.DataflowEndpointGroupDurationInSeconds"
    ]
    """<p>Amount of time, in seconds, before a contact starts that the Ground Station Dataflow Endpoint Group will be in a <code>PREPASS</code> state. A Ground Station Dataflow Endpoint Group State Change event will be emitted when the Dataflow Endpoint Group enters and exits the <code>PREPASS</code> state.</p>"""
    contact_post_pass_duration_seconds: NotRequired[
        "capo_groundstation.types.dataflow_endpoint_group_duration_in_seconds.DataflowEndpointGroupDurationInSeconds"
    ]
    """<p>Amount of time, in seconds, after a contact ends that the Ground Station Dataflow Endpoint Group will be in a <code>POSTPASS</code> state. A Ground Station Dataflow Endpoint Group State Change event will be emitted when the Dataflow Endpoint Group enters and exits the <code>POSTPASS</code> state.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDataflowEndpointGroupResponse) -> dict:
    out: dict = {}
    if "dataflow_endpoint_group_id" in value:
        out["dataflowEndpointGroupId"] = value["dataflow_endpoint_group_id"]
    if "dataflow_endpoint_group_arn" in value:
        out["dataflowEndpointGroupArn"] = value["dataflow_endpoint_group_arn"]
    if "endpoints_details" in value:
        import capo_groundstation.types.endpoint_details_list

        out["endpointsDetails"] = (
            capo_groundstation.types.endpoint_details_list.serialize_json(
                value["endpoints_details"]
            )
        )
    if "tags" in value:
        import capo_groundstation.types.tags_map

        out["tags"] = capo_groundstation.types.tags_map.serialize_json(value["tags"])
    if "contact_pre_pass_duration_seconds" in value:
        out["contactPrePassDurationSeconds"] = value[
            "contact_pre_pass_duration_seconds"
        ]
    if "contact_post_pass_duration_seconds" in value:
        out["contactPostPassDurationSeconds"] = value[
            "contact_post_pass_duration_seconds"
        ]
    return out


def deserialize_json(data: dict) -> GetDataflowEndpointGroupResponse:
    out: GetDataflowEndpointGroupResponse = {}  # type: ignore[typeddict-item]
    if "dataflowEndpointGroupId" in data:
        out["dataflow_endpoint_group_id"] = data["dataflowEndpointGroupId"]
    if "dataflowEndpointGroupArn" in data:
        out["dataflow_endpoint_group_arn"] = data["dataflowEndpointGroupArn"]
    if "endpointsDetails" in data:
        import capo_groundstation.types.endpoint_details_list

        out["endpoints_details"] = (
            capo_groundstation.types.endpoint_details_list.deserialize_json(
                data["endpointsDetails"]
            )
        )
    if "tags" in data:
        import capo_groundstation.types.tags_map

        out["tags"] = capo_groundstation.types.tags_map.deserialize_json(data["tags"])
    if "contactPrePassDurationSeconds" in data:
        out["contact_pre_pass_duration_seconds"] = data["contactPrePassDurationSeconds"]
    if "contactPostPassDurationSeconds" in data:
        out["contact_post_pass_duration_seconds"] = data[
            "contactPostPassDurationSeconds"
        ]
    return out
