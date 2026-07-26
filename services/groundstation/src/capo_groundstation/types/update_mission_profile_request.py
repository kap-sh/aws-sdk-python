"""Generated from Smithy shape ``com.amazonaws.groundstation#UpdateMissionProfileRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_groundstation.types.config_arn
    import capo_groundstation.types.dataflow_edge_list
    import capo_groundstation.types.duration_in_seconds
    import capo_groundstation.types.kms_key
    import capo_groundstation.types.positive_duration_in_seconds
    import capo_groundstation.types.role_arn
    import capo_groundstation.types.safe_name
    import capo_groundstation.types.uuid


class UpdateMissionProfileRequest(TypedDict, closed=True):
    mission_profile_id: "capo_groundstation.types.uuid.Uuid"
    """<p>UUID of a mission profile.</p>"""
    name: NotRequired["capo_groundstation.types.safe_name.SafeName"]
    """<p>Name of a mission profile.</p>"""
    contact_pre_pass_duration_seconds: NotRequired[
        "capo_groundstation.types.duration_in_seconds.DurationInSeconds"
    ]
    """<p>Amount of time after a contact ends that you'd like to receive a Ground Station Contact State Change event indicating the pass has finished.</p>"""
    contact_post_pass_duration_seconds: NotRequired[
        "capo_groundstation.types.duration_in_seconds.DurationInSeconds"
    ]
    """<p>Amount of time after a contact ends that you'd like to receive a Ground Station Contact State Change event indicating the pass has finished.</p>"""
    minimum_viable_contact_duration_seconds: NotRequired[
        "capo_groundstation.types.positive_duration_in_seconds.PositiveDurationInSeconds"
    ]
    """<p>Smallest amount of time in seconds that you'd like to see for an available contact. AWS Ground Station will not present you with contacts shorter than this duration.</p>"""
    dataflow_edges: NotRequired[
        "capo_groundstation.types.dataflow_edge_list.DataflowEdgeList"
    ]
    """<p>A list of lists of ARNs. Each list of ARNs is an edge, with a <i>from</i> <code> Config</code> and a <i>to</i> <code>Config</code>.</p>"""
    tracking_config_arn: NotRequired["capo_groundstation.types.config_arn.ConfigArn"]
    """<p>ARN of a tracking <code>Config</code>.</p>"""
    telemetry_sink_config_arn: NotRequired[
        "capo_groundstation.types.config_arn.ConfigArn"
    ]
    """<p>ARN of a telemetry sink <code>Config</code>.</p>"""
    streams_kms_key: NotRequired["capo_groundstation.types.kms_key.KmsKey"]
    """<p>KMS key to use for encrypting streams.</p>"""
    streams_kms_role: NotRequired["capo_groundstation.types.role_arn.RoleArn"]
    """<p>Role to use for encrypting streams with KMS key.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateMissionProfileRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "contact_pre_pass_duration_seconds" in value:
        out["contactPrePassDurationSeconds"] = value[
            "contact_pre_pass_duration_seconds"
        ]
    if "contact_post_pass_duration_seconds" in value:
        out["contactPostPassDurationSeconds"] = value[
            "contact_post_pass_duration_seconds"
        ]
    if "minimum_viable_contact_duration_seconds" in value:
        out["minimumViableContactDurationSeconds"] = value[
            "minimum_viable_contact_duration_seconds"
        ]
    if "dataflow_edges" in value:
        import capo_groundstation.types.dataflow_edge_list

        out["dataflowEdges"] = (
            capo_groundstation.types.dataflow_edge_list.serialize_json(
                value["dataflow_edges"]
            )
        )
    if "tracking_config_arn" in value:
        out["trackingConfigArn"] = value["tracking_config_arn"]
    if "telemetry_sink_config_arn" in value:
        out["telemetrySinkConfigArn"] = value["telemetry_sink_config_arn"]
    if "streams_kms_key" in value:
        import capo_groundstation.types.kms_key

        out["streamsKmsKey"] = capo_groundstation.types.kms_key.serialize_json(
            value["streams_kms_key"]
        )
    if "streams_kms_role" in value:
        out["streamsKmsRole"] = value["streams_kms_role"]
    return out


def deserialize_json(data: dict) -> UpdateMissionProfileRequest:
    out: UpdateMissionProfileRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "contactPrePassDurationSeconds" in data:
        out["contact_pre_pass_duration_seconds"] = data["contactPrePassDurationSeconds"]
    if "contactPostPassDurationSeconds" in data:
        out["contact_post_pass_duration_seconds"] = data[
            "contactPostPassDurationSeconds"
        ]
    if "minimumViableContactDurationSeconds" in data:
        out["minimum_viable_contact_duration_seconds"] = data[
            "minimumViableContactDurationSeconds"
        ]
    if "dataflowEdges" in data:
        import capo_groundstation.types.dataflow_edge_list

        out["dataflow_edges"] = (
            capo_groundstation.types.dataflow_edge_list.deserialize_json(
                data["dataflowEdges"]
            )
        )
    if "trackingConfigArn" in data:
        out["tracking_config_arn"] = data["trackingConfigArn"]
    if "telemetrySinkConfigArn" in data:
        out["telemetry_sink_config_arn"] = data["telemetrySinkConfigArn"]
    if "streamsKmsKey" in data:
        import capo_groundstation.types.kms_key

        out["streams_kms_key"] = capo_groundstation.types.kms_key.deserialize_json(
            data["streamsKmsKey"]
        )
    if "streamsKmsRole" in data:
        out["streams_kms_role"] = data["streamsKmsRole"]
    return out
