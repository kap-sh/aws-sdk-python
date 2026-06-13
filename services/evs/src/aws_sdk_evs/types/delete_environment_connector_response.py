"""Generated from Smithy shape ``com.amazonaws.evs#DeleteEnvironmentConnectorResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_evs.types.connector
    import aws_sdk_evs.types.environment_summary


class DeleteEnvironmentConnectorResponse(TypedDict):
    connector: NotRequired["aws_sdk_evs.types.connector.Connector"]
    """<p>A description of the deleted connector.</p>"""
    environment_summary: NotRequired[
        "aws_sdk_evs.types.environment_summary.EnvironmentSummary"
    ]
    """<p>A summary of the environment that the connector was deleted from.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteEnvironmentConnectorResponse) -> dict:
    out: dict = {}
    if "connector" in value:
        import aws_sdk_evs.types.connector

        out["connector"] = aws_sdk_evs.types.connector.serialize_aws_json_1_0(
            value["connector"]
        )
    if "environment_summary" in value:
        import aws_sdk_evs.types.environment_summary

        out["environmentSummary"] = (
            aws_sdk_evs.types.environment_summary.serialize_aws_json_1_0(
                value["environment_summary"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteEnvironmentConnectorResponse:
    out: DeleteEnvironmentConnectorResponse = {}  # type: ignore[typeddict-item]
    if "connector" in data:
        import aws_sdk_evs.types.connector

        out["connector"] = aws_sdk_evs.types.connector.deserialize_aws_json_1_0(
            data["connector"]
        )
    if "environmentSummary" in data:
        import aws_sdk_evs.types.environment_summary

        out["environment_summary"] = (
            aws_sdk_evs.types.environment_summary.deserialize_aws_json_1_0(
                data["environmentSummary"]
            )
        )
    return out
