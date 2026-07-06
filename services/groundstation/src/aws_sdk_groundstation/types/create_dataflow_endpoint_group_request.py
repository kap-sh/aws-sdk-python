"""Generated from Smithy shape ``com.amazonaws.groundstation#CreateDataflowEndpointGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_groundstation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.dataflow_endpoint_group_duration_in_seconds
    import aws_sdk_groundstation.types.endpoint_details_list
    import aws_sdk_groundstation.types.tags_map


class CreateDataflowEndpointGroupRequest(TypedDict, closed=True):
    endpoint_details: (
        "aws_sdk_groundstation.types.endpoint_details_list.EndpointDetailsList"
    )
    r"""<p>Endpoint details of each endpoint in the dataflow endpoint group. All dataflow endpoints within a single dataflow endpoint group must be of the same type. You cannot mix <a href=\"https://docs.aws.amazon.com/ground-station/latest/APIReference/API_AwsGroundStationAgentEndpoint.html\"> AWS Ground Station Agent endpoints</a> with <a href=\"https://docs.aws.amazon.com/ground-station/latest/APIReference/API_DataflowEndpoint.html\">Dataflow endpoints</a> in the same group. If your use case requires both types of endpoints, you must create separate dataflow endpoint groups for each type. </p>"""
    tags: NotRequired["aws_sdk_groundstation.types.tags_map.TagsMap"]
    """<p>Tags of a dataflow endpoint group.</p>"""
    contact_pre_pass_duration_seconds: NotRequired[
        "aws_sdk_groundstation.types.dataflow_endpoint_group_duration_in_seconds.DataflowEndpointGroupDurationInSeconds"
    ]
    r"""<p> Amount of time, in seconds, before a contact starts that the Ground Station Dataflow Endpoint Group will be in a <code>PREPASS</code> state. A <a href=\"https://docs.aws.amazon.com/ground-station/latest/ug/monitoring.automating-events.html\">Ground Station Dataflow Endpoint Group State Change event</a> will be emitted when the Dataflow Endpoint Group enters and exits the <code>PREPASS</code> state. </p>"""
    contact_post_pass_duration_seconds: NotRequired[
        "aws_sdk_groundstation.types.dataflow_endpoint_group_duration_in_seconds.DataflowEndpointGroupDurationInSeconds"
    ]
    r"""<p> Amount of time, in seconds, after a contact ends that the Ground Station Dataflow Endpoint Group will be in a <code>POSTPASS</code> state. A <a href=\"https://docs.aws.amazon.com/ground-station/latest/ug/monitoring.automating-events.html\">Ground Station Dataflow Endpoint Group State Change event</a> will be emitted when the Dataflow Endpoint Group enters and exits the <code>POSTPASS</code> state. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDataflowEndpointGroupRequest) -> dict:
    out: dict = {}
    import aws_sdk_groundstation.types.endpoint_details_list

    out["endpointDetails"] = (
        aws_sdk_groundstation.types.endpoint_details_list.serialize_json(
            value["endpoint_details"]
        )
    )
    if "tags" in value:
        import aws_sdk_groundstation.types.tags_map

        out["tags"] = aws_sdk_groundstation.types.tags_map.serialize_json(value["tags"])
    if "contact_pre_pass_duration_seconds" in value:
        out["contactPrePassDurationSeconds"] = value[
            "contact_pre_pass_duration_seconds"
        ]
    if "contact_post_pass_duration_seconds" in value:
        out["contactPostPassDurationSeconds"] = value[
            "contact_post_pass_duration_seconds"
        ]
    return out


def deserialize_json(data: dict) -> CreateDataflowEndpointGroupRequest:
    out: CreateDataflowEndpointGroupRequest = {}  # type: ignore[typeddict-item]
    if "endpointDetails" in data:
        import aws_sdk_groundstation.types.endpoint_details_list

        out["endpoint_details"] = (
            aws_sdk_groundstation.types.endpoint_details_list.deserialize_json(
                data["endpointDetails"]
            )
        )
    else:
        raise DeserializationError(
            "CreateDataflowEndpointGroupRequest.endpoint_details required"
        )
    if "tags" in data:
        import aws_sdk_groundstation.types.tags_map

        out["tags"] = aws_sdk_groundstation.types.tags_map.deserialize_json(
            data["tags"]
        )
    if "contactPrePassDurationSeconds" in data:
        out["contact_pre_pass_duration_seconds"] = data["contactPrePassDurationSeconds"]
    if "contactPostPassDurationSeconds" in data:
        out["contact_post_pass_duration_seconds"] = data[
            "contactPostPassDurationSeconds"
        ]
    return out
