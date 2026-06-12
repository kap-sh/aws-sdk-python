"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#UndeploySystemInstanceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iotthingsgraph.types.system_instance_summary


class UndeploySystemInstanceResponse(TypedDict):
    summary: NotRequired[
        "aws_sdk_iotthingsgraph.types.system_instance_summary.SystemInstanceSummary"
    ]
    """<p>An object that contains summary information about the system instance that was removed from its target.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UndeploySystemInstanceResponse) -> dict:
    out: dict = {}
    if "summary" in value:
        import aws_sdk_iotthingsgraph.types.system_instance_summary

        out["summary"] = (
            aws_sdk_iotthingsgraph.types.system_instance_summary.serialize_aws_json_1_1(
                value["summary"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UndeploySystemInstanceResponse:
    out: UndeploySystemInstanceResponse = {}  # type: ignore[typeddict-item]
    if "summary" in data:
        import aws_sdk_iotthingsgraph.types.system_instance_summary

        out["summary"] = (
            aws_sdk_iotthingsgraph.types.system_instance_summary.deserialize_aws_json_1_1(
                data["summary"]
            )
        )
    return out
