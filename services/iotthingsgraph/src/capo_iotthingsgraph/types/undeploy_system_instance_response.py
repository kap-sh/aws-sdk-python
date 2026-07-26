"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#UndeploySystemInstanceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotthingsgraph.types.system_instance_summary


class UndeploySystemInstanceResponse(TypedDict, closed=True):
    summary: NotRequired[
        "capo_iotthingsgraph.types.system_instance_summary.SystemInstanceSummary"
    ]
    """<p>An object that contains summary information about the system instance that was removed from its target.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UndeploySystemInstanceResponse) -> dict:
    out: dict = {}
    if "summary" in value:
        import capo_iotthingsgraph.types.system_instance_summary

        out["summary"] = (
            capo_iotthingsgraph.types.system_instance_summary.serialize_aws_json_1_1(
                value["summary"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UndeploySystemInstanceResponse:
    out: UndeploySystemInstanceResponse = {}  # type: ignore[typeddict-item]
    if "summary" in data:
        import capo_iotthingsgraph.types.system_instance_summary

        out["summary"] = (
            capo_iotthingsgraph.types.system_instance_summary.deserialize_aws_json_1_1(
                data["summary"]
            )
        )
    return out
