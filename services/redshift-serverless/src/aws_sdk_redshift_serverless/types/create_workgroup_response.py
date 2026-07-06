"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#CreateWorkgroupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_redshift_serverless.types.workgroup


class CreateWorkgroupResponse(TypedDict, closed=True):
    workgroup: NotRequired["aws_sdk_redshift_serverless.types.workgroup.Workgroup"]
    """<p>The created workgroup object.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateWorkgroupResponse) -> dict:
    out: dict = {}
    if "workgroup" in value:
        import aws_sdk_redshift_serverless.types.workgroup

        out["workgroup"] = (
            aws_sdk_redshift_serverless.types.workgroup.serialize_aws_json_1_1(
                value["workgroup"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateWorkgroupResponse:
    out: CreateWorkgroupResponse = {}  # type: ignore[typeddict-item]
    if "workgroup" in data:
        import aws_sdk_redshift_serverless.types.workgroup

        out["workgroup"] = (
            aws_sdk_redshift_serverless.types.workgroup.deserialize_aws_json_1_1(
                data["workgroup"]
            )
        )
    return out
