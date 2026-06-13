"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#ListWorkgroupsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_redshift_serverless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_redshift_serverless.types.workgroup_list


class ListWorkgroupsResponse(TypedDict):
    next_token: NotRequired["str"]
    """<p> If <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. To retrieve the next page, make the call again using the returned token.</p>"""
    workgroups: "aws_sdk_redshift_serverless.types.workgroup_list.WorkgroupList"
    """<p>The returned array of workgroups.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListWorkgroupsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import aws_sdk_redshift_serverless.types.workgroup_list

    out["workgroups"] = (
        aws_sdk_redshift_serverless.types.workgroup_list.serialize_aws_json_1_1(
            value["workgroups"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListWorkgroupsResponse:
    out: ListWorkgroupsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "workgroups" in data:
        import aws_sdk_redshift_serverless.types.workgroup_list

        out["workgroups"] = (
            aws_sdk_redshift_serverless.types.workgroup_list.deserialize_aws_json_1_1(
                data["workgroups"]
            )
        )
    else:
        raise DeserializationError("ListWorkgroupsResponse.workgroups required")
    return out
