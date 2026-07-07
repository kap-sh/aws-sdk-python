"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#CreateSystemInstanceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iotthingsgraph.types.system_instance_summary


class CreateSystemInstanceResponse(TypedDict, closed=True):
    summary: NotRequired[
        "aws_sdk_iotthingsgraph.types.system_instance_summary.SystemInstanceSummary"
    ]
    """<p>The summary object that describes the new system instance.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateSystemInstanceResponse) -> dict:
    out: dict = {}
    if "summary" in value:
        import aws_sdk_iotthingsgraph.types.system_instance_summary

        out["summary"] = (
            aws_sdk_iotthingsgraph.types.system_instance_summary.serialize_aws_json_1_1(
                value["summary"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateSystemInstanceResponse:
    out: CreateSystemInstanceResponse = {}  # type: ignore[typeddict-item]
    if "summary" in data:
        import aws_sdk_iotthingsgraph.types.system_instance_summary

        out["summary"] = (
            aws_sdk_iotthingsgraph.types.system_instance_summary.deserialize_aws_json_1_1(
                data["summary"]
            )
        )
    return out
