"""Generated from Smithy shape ``com.amazonaws.appsync#OpenSearchServiceDataSourceConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_appsync.errors import DeserializationError

if TYPE_CHECKING:
    import capo_appsync.types.string


class OpenSearchServiceDataSourceConfig(TypedDict, closed=True):
    endpoint: "capo_appsync.types.string.String"
    """<p>The endpoint.</p>"""
    aws_region: "capo_appsync.types.string.String"
    """<p>The Amazon Web Services Region.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OpenSearchServiceDataSourceConfig) -> dict:
    out: dict = {}
    out["endpoint"] = value["endpoint"]
    out["awsRegion"] = value["aws_region"]
    return out


def deserialize_json(data: dict) -> OpenSearchServiceDataSourceConfig:
    out: OpenSearchServiceDataSourceConfig = {}  # type: ignore[typeddict-item]
    if "endpoint" in data:
        out["endpoint"] = data["endpoint"]
    else:
        raise DeserializationError(
            "OpenSearchServiceDataSourceConfig.endpoint required"
        )
    if "awsRegion" in data:
        out["aws_region"] = data["awsRegion"]
    else:
        raise DeserializationError(
            "OpenSearchServiceDataSourceConfig.aws_region required"
        )
    return out
