"""Generated from Smithy shape ``com.amazonaws.devicefarm#ListTestGridSessionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_device_farm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.date_time
    import aws_sdk_device_farm.types.device_farm_arn
    import aws_sdk_device_farm.types.max_page_size
    import aws_sdk_device_farm.types.pagination_token
    import aws_sdk_device_farm.types.test_grid_session_status


class ListTestGridSessionsRequest(TypedDict):
    project_arn: "aws_sdk_device_farm.types.device_farm_arn.DeviceFarmArn"
    """<p>ARN of a <a>TestGridProject</a>.</p>"""
    status: NotRequired[
        "aws_sdk_device_farm.types.test_grid_session_status.TestGridSessionStatus"
    ]
    """<p>Return only sessions in this state.</p>"""
    creation_time_after: NotRequired["aws_sdk_device_farm.types.date_time.DateTime"]
    """<p>Return only sessions created after this time.</p>"""
    creation_time_before: NotRequired["aws_sdk_device_farm.types.date_time.DateTime"]
    """<p>Return only sessions created before this time.</p>"""
    end_time_after: NotRequired["aws_sdk_device_farm.types.date_time.DateTime"]
    """<p>Return only sessions that ended after this time.</p>"""
    end_time_before: NotRequired["aws_sdk_device_farm.types.date_time.DateTime"]
    """<p>Return only sessions that ended before this time.</p>"""
    max_result: NotRequired["aws_sdk_device_farm.types.max_page_size.MaxPageSize"]
    """<p>Return only this many results at a time.</p>"""
    next_token: NotRequired[
        "aws_sdk_device_farm.types.pagination_token.PaginationToken"
    ]
    """<p>Pagination token.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTestGridSessionsRequest) -> dict:
    out: dict = {}
    out["projectArn"] = value["project_arn"]
    if "status" in value:
        import aws_sdk_device_farm.types.test_grid_session_status

        out["status"] = (
            aws_sdk_device_farm.types.test_grid_session_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "creation_time_after" in value:
        import aws_sdk_device_farm.types.date_time

        out["creationTimeAfter"] = (
            aws_sdk_device_farm.types.date_time.serialize_aws_json_1_1(
                value["creation_time_after"]
            )
        )
    if "creation_time_before" in value:
        import aws_sdk_device_farm.types.date_time

        out["creationTimeBefore"] = (
            aws_sdk_device_farm.types.date_time.serialize_aws_json_1_1(
                value["creation_time_before"]
            )
        )
    if "end_time_after" in value:
        import aws_sdk_device_farm.types.date_time

        out["endTimeAfter"] = (
            aws_sdk_device_farm.types.date_time.serialize_aws_json_1_1(
                value["end_time_after"]
            )
        )
    if "end_time_before" in value:
        import aws_sdk_device_farm.types.date_time

        out["endTimeBefore"] = (
            aws_sdk_device_farm.types.date_time.serialize_aws_json_1_1(
                value["end_time_before"]
            )
        )
    if "max_result" in value:
        out["maxResult"] = value["max_result"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTestGridSessionsRequest:
    out: ListTestGridSessionsRequest = {}  # type: ignore[typeddict-item]
    if "projectArn" in data:
        out["project_arn"] = data["projectArn"]
    else:
        raise DeserializationError("ListTestGridSessionsRequest.project_arn required")
    if "status" in data:
        import aws_sdk_device_farm.types.test_grid_session_status

        out["status"] = (
            aws_sdk_device_farm.types.test_grid_session_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    if "creationTimeAfter" in data:
        import aws_sdk_device_farm.types.date_time

        out["creation_time_after"] = (
            aws_sdk_device_farm.types.date_time.deserialize_aws_json_1_1(
                data["creationTimeAfter"]
            )
        )
    if "creationTimeBefore" in data:
        import aws_sdk_device_farm.types.date_time

        out["creation_time_before"] = (
            aws_sdk_device_farm.types.date_time.deserialize_aws_json_1_1(
                data["creationTimeBefore"]
            )
        )
    if "endTimeAfter" in data:
        import aws_sdk_device_farm.types.date_time

        out["end_time_after"] = (
            aws_sdk_device_farm.types.date_time.deserialize_aws_json_1_1(
                data["endTimeAfter"]
            )
        )
    if "endTimeBefore" in data:
        import aws_sdk_device_farm.types.date_time

        out["end_time_before"] = (
            aws_sdk_device_farm.types.date_time.deserialize_aws_json_1_1(
                data["endTimeBefore"]
            )
        )
    if "maxResult" in data:
        out["max_result"] = data["maxResult"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
