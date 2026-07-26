"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#DeleteWorkgroupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_redshift_serverless.errors import DeserializationError

if TYPE_CHECKING:
    import capo_redshift_serverless.types.workgroup


class DeleteWorkgroupResponse(TypedDict, closed=True):
    workgroup: "capo_redshift_serverless.types.workgroup.Workgroup"
    """<p>The deleted workgroup object.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteWorkgroupResponse) -> dict:
    out: dict = {}
    import capo_redshift_serverless.types.workgroup

    out["workgroup"] = capo_redshift_serverless.types.workgroup.serialize_aws_json_1_1(
        value["workgroup"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteWorkgroupResponse:
    out: DeleteWorkgroupResponse = {}  # type: ignore[typeddict-item]
    if "workgroup" in data:
        import capo_redshift_serverless.types.workgroup

        out["workgroup"] = (
            capo_redshift_serverless.types.workgroup.deserialize_aws_json_1_1(
                data["workgroup"]
            )
        )
    else:
        raise DeserializationError("DeleteWorkgroupResponse.workgroup required")
    return out
