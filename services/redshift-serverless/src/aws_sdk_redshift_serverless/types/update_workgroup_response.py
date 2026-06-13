"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#UpdateWorkgroupResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_redshift_serverless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_redshift_serverless.types.workgroup


class UpdateWorkgroupResponse(TypedDict):
    workgroup: "aws_sdk_redshift_serverless.types.workgroup.Workgroup"
    """<p>The updated workgroup object.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateWorkgroupResponse) -> dict:
    out: dict = {}
    import aws_sdk_redshift_serverless.types.workgroup

    out["workgroup"] = (
        aws_sdk_redshift_serverless.types.workgroup.serialize_aws_json_1_1(
            value["workgroup"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateWorkgroupResponse:
    out: UpdateWorkgroupResponse = {}  # type: ignore[typeddict-item]
    if "workgroup" in data:
        import aws_sdk_redshift_serverless.types.workgroup

        out["workgroup"] = (
            aws_sdk_redshift_serverless.types.workgroup.deserialize_aws_json_1_1(
                data["workgroup"]
            )
        )
    else:
        raise DeserializationError("UpdateWorkgroupResponse.workgroup required")
    return out
