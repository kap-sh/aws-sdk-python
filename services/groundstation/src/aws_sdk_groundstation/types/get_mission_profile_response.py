"""Generated from Smithy shape ``com.amazonaws.groundstation#GetMissionProfileResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.aws_region
    import aws_sdk_groundstation.types.config_arn
    import aws_sdk_groundstation.types.dataflow_edge_list
    import aws_sdk_groundstation.types.duration_in_seconds
    import aws_sdk_groundstation.types.kms_key
    import aws_sdk_groundstation.types.mission_profile_arn
    import aws_sdk_groundstation.types.positive_duration_in_seconds
    import aws_sdk_groundstation.types.role_arn
    import aws_sdk_groundstation.types.safe_name
    import aws_sdk_groundstation.types.tags_map
    import aws_sdk_groundstation.types.uuid


class GetMissionProfileResponse(TypedDict):
    mission_profile_id: NotRequired["aws_sdk_groundstation.types.uuid.Uuid"]
    """<p>UUID of a mission profile.</p>"""
    mission_profile_arn: NotRequired[
        "aws_sdk_groundstation.types.mission_profile_arn.MissionProfileArn"
    ]
    """<p>ARN of a mission profile.</p>"""
    name: NotRequired["aws_sdk_groundstation.types.safe_name.SafeName"]
    """<p>Name of a mission profile.</p>"""
    region: NotRequired["aws_sdk_groundstation.types.aws_region.AWSRegion"]
    """<p>Region of a mission profile.</p>"""
    contact_pre_pass_duration_seconds: NotRequired[
        "aws_sdk_groundstation.types.duration_in_seconds.DurationInSeconds"
    ]
    """<p>Amount of time prior to contact start you'd like to receive a CloudWatch event indicating an upcoming pass.</p>"""
    contact_post_pass_duration_seconds: NotRequired[
        "aws_sdk_groundstation.types.duration_in_seconds.DurationInSeconds"
    ]
    """<p>Amount of time after a contact ends that you'd like to receive a CloudWatch event indicating the pass has finished.</p>"""
    minimum_viable_contact_duration_seconds: NotRequired[
        "aws_sdk_groundstation.types.positive_duration_in_seconds.PositiveDurationInSeconds"
    ]
    """<p>Smallest amount of time in seconds that you'd like to see for an available contact. AWS Ground Station will not present you with contacts shorter than this duration.</p>"""
    dataflow_edges: NotRequired[
        "aws_sdk_groundstation.types.dataflow_edge_list.DataflowEdgeList"
    ]
    """<p>A list of lists of ARNs. Each list of ARNs is an edge, with a <i>from</i> <code> Config</code> and a <i>to</i> <code>Config</code>.</p>"""
    tracking_config_arn: NotRequired["aws_sdk_groundstation.types.config_arn.ConfigArn"]
    """<p>ARN of a tracking <code>Config</code>.</p>"""
    telemetry_sink_config_arn: NotRequired[
        "aws_sdk_groundstation.types.config_arn.ConfigArn"
    ]
    """<p>ARN of a telemetry sink <code>Config</code>.</p>"""
    tags: NotRequired["aws_sdk_groundstation.types.tags_map.TagsMap"]
    """<p>Tags assigned to a mission profile.</p>"""
    streams_kms_key: NotRequired["aws_sdk_groundstation.types.kms_key.KmsKey"]
    """<p>KMS key to use for encrypting streams.</p>"""
    streams_kms_role: NotRequired["aws_sdk_groundstation.types.role_arn.RoleArn"]
    """<p>Role to use for encrypting streams with KMS key.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMissionProfileResponse) -> dict:
    out: dict = {}
    if "mission_profile_id" in value:
        out["missionProfileId"] = value["mission_profile_id"]
    if "mission_profile_arn" in value:
        out["missionProfileArn"] = value["mission_profile_arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "region" in value:
        out["region"] = value["region"]
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
        import aws_sdk_groundstation.types.dataflow_edge_list

        out["dataflowEdges"] = (
            aws_sdk_groundstation.types.dataflow_edge_list.serialize_json(
                value["dataflow_edges"]
            )
        )
    if "tracking_config_arn" in value:
        out["trackingConfigArn"] = value["tracking_config_arn"]
    if "telemetry_sink_config_arn" in value:
        out["telemetrySinkConfigArn"] = value["telemetry_sink_config_arn"]
    if "tags" in value:
        import aws_sdk_groundstation.types.tags_map

        out["tags"] = aws_sdk_groundstation.types.tags_map.serialize_json(value["tags"])
    if "streams_kms_key" in value:
        import aws_sdk_groundstation.types.kms_key

        out["streamsKmsKey"] = aws_sdk_groundstation.types.kms_key.serialize_json(
            value["streams_kms_key"]
        )
    if "streams_kms_role" in value:
        out["streamsKmsRole"] = value["streams_kms_role"]
    return out


def deserialize_json(data: dict) -> GetMissionProfileResponse:
    out: GetMissionProfileResponse = {}  # type: ignore[typeddict-item]
    if "missionProfileId" in data:
        out["mission_profile_id"] = data["missionProfileId"]
    if "missionProfileArn" in data:
        out["mission_profile_arn"] = data["missionProfileArn"]
    if "name" in data:
        out["name"] = data["name"]
    if "region" in data:
        out["region"] = data["region"]
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
        import aws_sdk_groundstation.types.dataflow_edge_list

        out["dataflow_edges"] = (
            aws_sdk_groundstation.types.dataflow_edge_list.deserialize_json(
                data["dataflowEdges"]
            )
        )
    if "trackingConfigArn" in data:
        out["tracking_config_arn"] = data["trackingConfigArn"]
    if "telemetrySinkConfigArn" in data:
        out["telemetry_sink_config_arn"] = data["telemetrySinkConfigArn"]
    if "tags" in data:
        import aws_sdk_groundstation.types.tags_map

        out["tags"] = aws_sdk_groundstation.types.tags_map.deserialize_json(
            data["tags"]
        )
    if "streamsKmsKey" in data:
        import aws_sdk_groundstation.types.kms_key

        out["streams_kms_key"] = aws_sdk_groundstation.types.kms_key.deserialize_json(
            data["streamsKmsKey"]
        )
    if "streamsKmsRole" in data:
        out["streams_kms_role"] = data["streamsKmsRole"]
    return out
