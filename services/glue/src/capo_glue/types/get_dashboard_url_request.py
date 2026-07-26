"""Generated from Smithy shape ``com.amazonaws.glue#GetDashboardUrlRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.glue_resource_type
    import capo_glue.types.name_string
    import capo_glue.types.orchestration_name_string


class GetDashboardUrlRequest(TypedDict, closed=True):
    resource_id: "capo_glue.types.name_string.NameString"
    """<p>The unique identifier of the resource for which to retrieve the dashboard URL.</p>"""
    resource_type: "capo_glue.types.glue_resource_type.GlueResourceType"
    """<p>The type of the resource. Valid values are <code>SESSION</code> and <code>JOB</code>.</p>"""
    request_origin: NotRequired[
        "capo_glue.types.orchestration_name_string.OrchestrationNameString"
    ]
    """<p>The origin of the request. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDashboardUrlRequest) -> dict:
    out: dict = {}
    out["ResourceId"] = value["resource_id"]
    import capo_glue.types.glue_resource_type

    out["ResourceType"] = capo_glue.types.glue_resource_type.serialize_aws_json_1_1(
        value["resource_type"]
    )
    if "request_origin" in value:
        out["RequestOrigin"] = value["request_origin"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDashboardUrlRequest:
    out: GetDashboardUrlRequest = {}  # type: ignore[typeddict-item]
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    else:
        raise DeserializationError("GetDashboardUrlRequest.resource_id required")
    if "ResourceType" in data:
        import capo_glue.types.glue_resource_type

        out["resource_type"] = (
            capo_glue.types.glue_resource_type.deserialize_aws_json_1_1(
                data["ResourceType"]
            )
        )
    else:
        raise DeserializationError("GetDashboardUrlRequest.resource_type required")
    if "RequestOrigin" in data:
        out["request_origin"] = data["RequestOrigin"]
    return out
