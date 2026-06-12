"""Generated from Smithy shape ``com.amazonaws.bcmdashboards#DashboardReference``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bcm_dashboards.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bcm_dashboards.types.dashboard_arn
    import aws_sdk_bcm_dashboards.types.dashboard_name
    import aws_sdk_bcm_dashboards.types.dashboard_type
    import aws_sdk_bcm_dashboards.types.description
    import aws_sdk_bcm_dashboards.types.generic_time_stamp


class DashboardReference(TypedDict):
    arn: "aws_sdk_bcm_dashboards.types.dashboard_arn.DashboardArn"
    """<p>The ARN of the referenced dashboard.</p>"""
    name: "aws_sdk_bcm_dashboards.types.dashboard_name.DashboardName"
    """<p>The name of the referenced dashboard.</p>"""
    description: NotRequired["aws_sdk_bcm_dashboards.types.description.Description"]
    """<p>The description of the referenced dashboard.</p>"""
    type: "aws_sdk_bcm_dashboards.types.dashboard_type.DashboardType"
    """<p>The dashboard type.</p>"""
    created_at: "aws_sdk_bcm_dashboards.types.generic_time_stamp.GenericTimeStamp"
    """<p>The timestamp when the dashboard was created.</p>"""
    updated_at: "aws_sdk_bcm_dashboards.types.generic_time_stamp.GenericTimeStamp"
    """<p>The timestamp when the dashboard was last modified.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DashboardReference) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    import aws_sdk_bcm_dashboards.types.dashboard_type

    out["type"] = aws_sdk_bcm_dashboards.types.dashboard_type.serialize_aws_json_1_0(
        value["type"]
    )
    import aws_sdk_bcm_dashboards.types.generic_time_stamp

    out["createdAt"] = (
        aws_sdk_bcm_dashboards.types.generic_time_stamp.serialize_aws_json_1_0(
            value["created_at"]
        )
    )
    import aws_sdk_bcm_dashboards.types.generic_time_stamp

    out["updatedAt"] = (
        aws_sdk_bcm_dashboards.types.generic_time_stamp.serialize_aws_json_1_0(
            value["updated_at"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> DashboardReference:
    out: DashboardReference = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("DashboardReference.arn required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("DashboardReference.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "type" in data:
        import aws_sdk_bcm_dashboards.types.dashboard_type

        out["type"] = (
            aws_sdk_bcm_dashboards.types.dashboard_type.deserialize_aws_json_1_0(
                data["type"]
            )
        )
    else:
        raise DeserializationError("DashboardReference.type required")
    if "createdAt" in data:
        import aws_sdk_bcm_dashboards.types.generic_time_stamp

        out["created_at"] = (
            aws_sdk_bcm_dashboards.types.generic_time_stamp.deserialize_aws_json_1_0(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("DashboardReference.created_at required")
    if "updatedAt" in data:
        import aws_sdk_bcm_dashboards.types.generic_time_stamp

        out["updated_at"] = (
            aws_sdk_bcm_dashboards.types.generic_time_stamp.deserialize_aws_json_1_0(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError("DashboardReference.updated_at required")
    return out
