"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#GetWorkgroupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_redshift_serverless.errors import DeserializationError

if TYPE_CHECKING:
    import capo_redshift_serverless.types.workgroup


class GetWorkgroupResponse(TypedDict, closed=True):
    workgroup: "capo_redshift_serverless.types.workgroup.Workgroup"
    """<p>The returned workgroup object.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetWorkgroupResponse) -> dict:
    out: dict = {}
    import capo_redshift_serverless.types.workgroup

    out["workgroup"] = capo_redshift_serverless.types.workgroup.serialize_aws_json_1_1(
        value["workgroup"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetWorkgroupResponse:
    out: GetWorkgroupResponse = {}  # type: ignore[typeddict-item]
    if "workgroup" in data:
        import capo_redshift_serverless.types.workgroup

        out["workgroup"] = (
            capo_redshift_serverless.types.workgroup.deserialize_aws_json_1_1(
                data["workgroup"]
            )
        )
    else:
        raise DeserializationError("GetWorkgroupResponse.workgroup required")
    return out
