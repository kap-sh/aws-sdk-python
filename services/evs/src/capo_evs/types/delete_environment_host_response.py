"""Generated from Smithy shape ``com.amazonaws.evs#DeleteEnvironmentHostResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_evs.types.environment_summary
    import capo_evs.types.host


class DeleteEnvironmentHostResponse(TypedDict, closed=True):
    environment_summary: NotRequired[
        "capo_evs.types.environment_summary.EnvironmentSummary"
    ]
    """<p>A summary of the environment that the host was deleted from.</p>"""
    host: NotRequired["capo_evs.types.host.Host"]
    """<p>A description of the deleted host.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteEnvironmentHostResponse) -> dict:
    out: dict = {}
    if "environment_summary" in value:
        import capo_evs.types.environment_summary

        out["environmentSummary"] = (
            capo_evs.types.environment_summary.serialize_aws_json_1_0(
                value["environment_summary"]
            )
        )
    if "host" in value:
        import capo_evs.types.host

        out["host"] = capo_evs.types.host.serialize_aws_json_1_0(value["host"])
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteEnvironmentHostResponse:
    out: DeleteEnvironmentHostResponse = {}  # type: ignore[typeddict-item]
    if "environmentSummary" in data:
        import capo_evs.types.environment_summary

        out["environment_summary"] = (
            capo_evs.types.environment_summary.deserialize_aws_json_1_0(
                data["environmentSummary"]
            )
        )
    if "host" in data:
        import capo_evs.types.host

        out["host"] = capo_evs.types.host.deserialize_aws_json_1_0(data["host"])
    return out
