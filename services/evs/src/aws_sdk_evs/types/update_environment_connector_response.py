"""Generated from Smithy shape ``com.amazonaws.evs#UpdateEnvironmentConnectorResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_evs.types.connector


class UpdateEnvironmentConnectorResponse(TypedDict):
    connector: NotRequired["aws_sdk_evs.types.connector.Connector"]
    """<p>A description of the updated connector.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateEnvironmentConnectorResponse) -> dict:
    out: dict = {}
    if "connector" in value:
        import aws_sdk_evs.types.connector

        out["connector"] = aws_sdk_evs.types.connector.serialize_aws_json_1_0(
            value["connector"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateEnvironmentConnectorResponse:
    out: UpdateEnvironmentConnectorResponse = {}  # type: ignore[typeddict-item]
    if "connector" in data:
        import aws_sdk_evs.types.connector

        out["connector"] = aws_sdk_evs.types.connector.deserialize_aws_json_1_0(
            data["connector"]
        )
    return out
