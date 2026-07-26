"""Generated from Smithy shape ``com.amazonaws.evs#UpdateEnvironmentConnectorResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_evs.types.connector


class UpdateEnvironmentConnectorResponse(TypedDict, closed=True):
    connector: NotRequired["capo_evs.types.connector.Connector"]
    """<p>A description of the updated connector.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateEnvironmentConnectorResponse) -> dict:
    out: dict = {}
    if "connector" in value:
        import capo_evs.types.connector

        out["connector"] = capo_evs.types.connector.serialize_aws_json_1_0(
            value["connector"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateEnvironmentConnectorResponse:
    out: UpdateEnvironmentConnectorResponse = {}  # type: ignore[typeddict-item]
    if "connector" in data:
        import capo_evs.types.connector

        out["connector"] = capo_evs.types.connector.deserialize_aws_json_1_0(
            data["connector"]
        )
    return out
